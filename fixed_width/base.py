import io
import collections

import struct
import typing


class FixedWidth:
    def __init__(
        self,
        f: io.BytesIO,
        format: str,
        fieldnames: typing.List[str] = None,
        use_first_row_for_fieldnames: bool = None,
        encoding: str = "utf-8",
    ) -> None:
        """
        Intended to be as compatible with the python stdlib csv module
        as much as possible & practical.

        Parameters:

            f:                              file-like object

            format:                         see documentation for struct.Struct

            fieldnames:                     list of strings for the field names

            use_first_row_for_fieldnames:   get fieldnames from the first row
                                            of the file
        """
        if use_first_row_for_fieldnames and fieldnames:
            raise ValueError(
                "Please use either fieldnames, or use_first_row_for_fieldnames"
            )

        self._f = f
        self.format = format
        self._struct = struct.Struct(self.format)
        self.encoding = encoding
        if use_first_row_for_fieldnames:
            self._fieldnames = self._next_row_as_list()
        else:
            self._fieldnames = fieldnames or []

    def __iter__(self) -> "FixedWidth":
        return self

    def __next__(
        self,
    ) -> typing.Union[typing.List[typing.Any], collections.OrderedDict]:
        if self._fieldnames:
            return self._next_row_as_ordereddict()
        return self._next_row_as_list()

    def _next_row_as_ordereddict(self) -> collections.OrderedDict:
        line = self._next_row_as_list()
        return collections.OrderedDict(zip(self._fieldnames, line))

    def _next_row_as_list(self) -> typing.List[str]:
        row: typing.List[str] = []
        while not any(row):
            row = []
            for field in self._struct.unpack_from(next(self._f)):
                if isinstance(field, bytes):
                    row.append(field.strip().decode(self.encoding))
                else:
                    row.append(field)
        return row
