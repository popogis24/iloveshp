
from iloveshp.utils.file_utils import FileUtils
from iloveshp.config.settings import Settings

def main():
    input_path = 'path/to/input/shapefile.shp'
    output_path = 'path/to/output/shapefile.geojson'
    
    FileUtils.ensure_directory_exists(Settings.get_data_dir())

if __name__ == '__main__':
    main()
