import os
from dotenv import dotenv_values
import psycopg2
from psycopg2 import sql
import fiona

class DBManager:
    def __init__(self, env_path):
        env = dotenv_values(env_path)
        self.db_credentials = {
            'host': env['DB_HOST'],
            'port': env['DB_PORT'],
            'database': env['DB_NAME'],
            'user': env['DB_USER'],
            'password': env['DB_PASSWORD']
        }
        self.conn = None

    def connect(self):
        """Establish a database connection."""
        try:
            self.conn = psycopg2.connect(**self.db_credentials)
            print("Connection established")
        except Exception as e:
            print(f"Error connecting to the database: {e}")

    def close_connection(self):
        """Close the database connection."""
        if self.conn:
            self.conn.close()
            print("Connection closed")

    def get_srid(self, shapefile_path):
        """Get SRID from the shapefile."""
        with fiona.open(shapefile_path) as src:
            return src.crs['init'].split(':')[-1]
        
    def insert_shapefile(self, table, shapefile_path):
        """Insert shapefile into the database."""
        try:
            srid = self.get_srid(shapefile_path)
            import subprocess
            command = [
                'shp2pgsql', '-I', f'-s{srid}', shapefile_path, table
            ]
            psql_command = [
                'psql',
                f"-h{self.db_credentials['host']}",
                f"-p{self.db_credentials['port']}",
                f"-d{self.db_credentials['database']}",
                f"-U{self.db_credentials['user']}",
                '-f', '-'
            ]
            proc1 = subprocess.Popen(command, stdout=subprocess.PIPE)
            proc2 = subprocess.Popen(psql_command, stdin=proc1.stdout, stdout=subprocess.PIPE)
            proc1.stdout.close()
            output, error = proc2.communicate()
            if proc2.returncode == 0:
                print(f"Shapefile {shapefile_path} inserted into table {table} with SRID {srid}")
                return table
            else:
                print(f"Error inserting shapefile: {error}")
                return None
        except Exception as e:
            print(f"Error: {e}")
            return None

    def remove_shapefile(self, table):
        """Remove shapefile from the database."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute(sql.SQL("DROP TABLE IF EXISTS {}").format(sql.Identifier(table)))
                self.conn.commit()
                print(f"Table {table} removed from database")
        except Exception as e:
            print(f"Error removing shapefile: {e}")

    def get_tables(self):
        """Get tables from the database."""
        try:
            with self.conn.cursor() as cursor:
                cursor.execute("SELECT table_name FROM information_schema.tables WHERE table_schema = 'public'")
                tables = cursor.fetchall()
                return [table[0] for table in tables]
        except Exception as e:
            print(f"Error getting tables: {e}")
            return None
if __name__ == '__main__':
    table = 'biomes'
    env_path = '/Users/andersonstolfi/Documents/coding/iloveshp/.env'
    shapefile_path = '/Users/andersonstolfi/Documents/coding/iloveshp/tests/vector_files/input/lm_bioma_250.shp'
    
    db_manager = DBManager(env_path)
    db_manager.connect()
    db_manager.insert_shapefile(table, shapefile_path)
    db_manager.remove_shapefile(table)
    db_manager.close_connection()
