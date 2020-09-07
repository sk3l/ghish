import logging

from requests import Session
from requests.exceptions import RequestException

LOG = logging.getLogger("ghish")


class HttpResultSet:

    def __init__(self):
        self._data = []

    def append(self, jsonobj):
        if isinstance(jsonobj, dict):
            self._data.append(jsonobj)
        elif isinstance(jsonobj, list):
            self._data.extend(jsonobj)
        else:
            raise Exception("Non-JSON compatible object in HttpResultSet()")

    def size(self):
        return len(self._data)

    def data(self):
        return self._data

    def __getitem__(self, index):
        return self._data[index]


class GhishHttpAgent:
    def __init__(self, url, token=None, read_only=True):
        self._base_url = url
        self._token = token
        self._read_only = read_only
        self._session = None

    # CONTEXT MANAGER HERE vvvvvv
    def __enter__(self):
        self.open()
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def send_get(self, url, query_params=None, http_headers=None):
        try:
            LOG.debug("Calling GhishApiAgent.send_get()")
            self._session.params = query_params

            results = HttpResultSet()
            next_url = f"{self._base_url}/{url}"
            while True:
                response = self._session.get(next_url)
                results.append(response.json())

                if "Link" not in response.headers:
                    break

                links = self._parse_http_links(response.headers["Link"])

                next_url = None
                for link in links:
                    if link[1] == 'next':
                        next_url = link[0]
                        break

                if not next_url:
                    break

            return results
        except RequestException as err:
            LOG.error(f"Error in send_get():{err}")

    def send_post(self, url, query_params=None, http_headers=None):
        try:
            LOG.debug("Calling GhishApiAgent.send_post()")
            if not self._checkReadOnly("send_post"):
                return None
            else:
                self._session.params = query_params
                return self._session.post(f"{self._base_url}/{url}", query_params)
        except RequestException as err:
            LOG.error(f"Error in send_post():{err}")

    def send_patch(self, url, query_params=None, http_headers=None):

        try:
            LOG.debug("Calling GhishApiAgent.send_patch()")
            if not self._checkReadOnly("send_patch"):
                return None
            else:
                self._session.params = query_params
                return self._session.patch(f"{self._base_url}/{url}", query_params)
        except RequestException as err:
            LOG.error(f"Error in send_patch():{err}")

    def send_delete(self, url, query_params=None, http_headers=None):
        try:
            LOG.debug("Calling GhishApiAgent.send_delete()")
            if not self._checkReadOnly("send_delete"):
                return None
            else:
                self._session.params = query_params
                return self._session.delete(f"{self._base_url}/{url}", query_params)
        except RequestException as err:
            LOG.error(f"Error in send_delete():{err}")

    def open(self):
        if not self._session:
            self._session = Session()
            self._session.headers["Authorization"] = f"token {self._token}"

    def close(self):
        if self._session:
            self._session.close()

    def _checkReadOnly(self, funcname):
        if self._read_only:
            LOG.warn(f"Skipped GhishApiAgent.{funcname}; read-only mode.")
        return self._read_only

    def _parse_http_links(self, linkstr):
        link_list = linkstr.split(",")

        links = []
        for link in link_list:
            # Get the next url
            url_opn = link.index("<")
            url_cls = link.index(">")
            url = link[url_opn+1:url_cls]

            # Get url kind (next, last, etc)
            param_strt = link.rindex("=")
            param = link[param_strt+1:].lstrip('"').rstrip('"')

            links.append((url, param, ))

        return links
