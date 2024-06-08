from abc import ABC, abstractmethod

class Reader(ABC):
    def __init__(self, file_path):
        self.file_path = file_path

    @abstractmethod
    def validate(self):
        """
        Read the data from the file.
        """
        pass

    @abstractmethod
    def open(self):
        """
        Open the file.
        """
        pass
