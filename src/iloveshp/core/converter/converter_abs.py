from abc import ABC, abstractmethod

class Converter(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def find_in_database(self, table_name):
        """
        Find the file in the database.
        """
        pass

    @abstractmethod
    def convert(self):
        """
        Convert the file.
        """
        pass