import os

class FileUtils:
    @staticmethod
    def ensure_directory_exists(path):
        """
        Ensures that the specified directory exists. If it doesn't, creates it.

        Args:
            path (str): Path to the directory.
        """
        if not os.path.exists(path):
            os.makedirs(path)
            print(f"Directory {path} created.")
        else:
            print(f"Directory {path} already exists.")
