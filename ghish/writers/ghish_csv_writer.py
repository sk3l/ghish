import collections
from csv import DictWriter

from .ghish_writer import GhishWriter


class GhishCsvWriter(GhishWriter):
    def __init__(self, file_name, schema_type):
        self._file_name = file_name
        self._schema = schema_type
        self._file = None

    def __enter__(self):
        self._file = open(self._file_name, "w")
        return self

    def __exit__(self, type, value, traceback):
        self._file.close()

    def write(self, ghish_obj):
        schema = self._schema()

        csv_writer = DictWriter(self._file, fieldnames=schema.fields.keys())

        # Write column headers from field names
        csv_writer.writeheader()
        # Write CSV data based on serialized data
        data = schema.dump(ghish_obj)

        if isinstance(data, collections.Sequence):
            for itm in data:
                csv_writer.writerow(itm)
        else:
            csv_writer.writerow(data)
