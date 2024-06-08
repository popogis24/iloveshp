import os

class Settings:
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    DATA_DIR = os.path.join(BASE_DIR, 'data')
    LOG_FILE = os.path.join(BASE_DIR, 'logs', 'iloveshp.log')

    @staticmethod
    def get_base_dir():
        """
        Returns the base directory of the project.
        """
        return Settings.BASE_DIR

    @staticmethod
    def get_data_dir():
        """
        Returns the data directory of the project.
        """
        return Settings.DATA_DIR

    @staticmethod
    def get_log_file():
        """
        Returns the log file path.
        """
        return Settings.LOG_FILE
