import io  # noqa: F401
import collections

import struct


class FixedWidth(object):

    def __init__(
            self,
            f,  # type: io.BytesIO
            format,  # type: str
            fieldnames=None,  # type: List[str]
            use_first_row_for_fieldnames=None,  # type: bool
            encoding='utf-8'
            ):  # type: () -> None
        '''
        Intended to be as compatible with the python stdlib csv module
        as much as possible & practical.

        Parameters:

            f:                              file-like object

            format:                         see documentation for struct.Struct

            fieldnames:                     list of strings for the field names

            use_first_row_for_fieldnames:   get fieldnames from the first row
                                            of the file
        '''
        if use_first_row_for_fieldnames and fieldnames:
            raise ValueError("Please use either fieldnames, or "
                             "use_first_row_for_fieldnames")

        self._f = f
        self.format = format
        self._struct = struct.Struct(self.format)
        self.encoding = encoding
        if use_first_row_for_fieldnames:
            self._fieldnames = self._next_row_as_list()
        else:
            self._fieldnames = fieldnames

    def __iter__(self):
        return self

    def __next__(self):  # type: Union[List[Any], collections.OrderedDict]
        if self._fieldnames:
            return self._next_row_as_ordereddict()
        return self._next_row_as_list()

    def _next_row_as_ordereddict(self):  # collections.OrderedDict
        line = self._next_row_as_list()
        return collections.OrderedDict(zip(self._fieldnames, line))

    def _next_row_as_list(self):  # List[Any]
        row = []
        while not any(row):
            row = []
            for field in self._struct.unpack_from(next(self._f)):
                if isinstance(field, bytes):
                    if self.encoding:
                        row.append(field.strip().decode(self.encoding))
                    else:
                        row.append(field.strip())
                else:
                    row.append(field)
        return row
