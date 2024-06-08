import os
from iloveshp.core.converter.converter_abs import Converter
from iloveshp.database.db_manager import DBManager

class MergeTables(Converter):
    """
    Convert TABLE to KMZ.
    The table is in Postgresql.
    """
    def __init__(self, table, db_connection):
        self.table = table
        self.db_connection = db_connection
    
    def find_in_database(self):
        """
        Find the table in the database.
        """
        if self.table in self.db_connection.get_tables():
            print(f"Table {self.table} found in the database")
        else:
            print(f"Table {self.table} not found in the database")
        
 
    
if __name__ == '__main__':
    table = 'biome'
    env_path = '/Users/andersonstolfi/Documents/coding/iloveshp/.env'
    shapefile = '/Users/andersonstolfi/Documents/coding/iloveshp/tests/vector_files/input/lm_bioma_250.shp'
    db_connection = DBManager(env_path)
    db_connection.connect()
    db_connection.insert_shapefile(table, shapefile)
    converter = KMZConverter(table, db_connection)
    converter.find_in_database()
    converter.convert()
    db_connection.close_connection()