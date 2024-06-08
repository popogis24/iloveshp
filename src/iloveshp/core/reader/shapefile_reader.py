import os
from osgeo import ogr

from reader_abs import Reader

class ShapefileReader(Reader):
    def __init__(self, file_path):
        super().__init__(file_path)
        self.data = None

    def validate(self):
        """
        Validate the shapefile.
        """
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"File not found: {self.file_path}")
        if not self.file_path.endswith('.shp'):
            raise ValueError(f"Invalid file type: {self.file_path}")
    
    def open(self):
        """
        Open the shapefile.
        """
        driver = ogr.GetDriverByName('ESRI Shapefile')
        shapefile = driver.Open(self.file_path, 0)
    
        return shapefile
    
    def get_feature_layer(self, shapefile):
        """
        Open the layer from the shapefile.
        """
        layer = shapefile.GetLayer()
        return layer
    
    def get_table_as_df(self, shapefile):
        """
        Read the table from the shapefile.
        """
        layer = self.get_feature_layer(shapefile)
        table = []
        for feature in layer:
            row = {}
            for field in feature.keys():
                row[field] = feature.GetField(field)
            table.append(row)
        return table

if __name__ == '__main__':
    input_path = '/Users/andersonstolfi/Documents/coding/iloveshp/tests/reader_tests/input/lm_bioma_250.shp'
    output_path = '/Users/andersonstolfi/Documents/coding/iloveshp/tests/reader_tests/input/lm_bioma_250.geojson'
    
    reader = ShapefileReader(input_path)
    reader.validate()
    layer = reader.open()
    table = reader.get_table_as_df(layer)
    print(layer)
    print(table)