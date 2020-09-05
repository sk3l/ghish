import logging

from requests import Session
from requests.exceptions import RequestException

LOG = logging.getLogger("ghish")


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
            return self._session.get(f"{self._base_url}/{url}")
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
