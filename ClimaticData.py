import pandas
import numpy


class ClimaticData:

    @property
    def data(self):
        return self.__data.copy()

    def __init__(self, file: str):
        self.__data = pandas.read_csv(file)

    def set_column_name(self, to_change: str, new_name: str, change_in_file: bool = False):
        if change_in_file:
            self.__data.rename(columns={ to_change: new_name }, inplace=change_in_file)
        else:
            self.__data = self.__data.rename(columns={ to_change: new_name }, inplace=change_in_file)

    def set_columns_names(self, to_change: list, new_names: list, change_in_file: bool = False):
        for i in range(0, len(to_change)):
            self.set_column_name(to_change[i], new_names[i], change_in_file)