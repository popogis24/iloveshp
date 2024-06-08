class ReaderFactory:
    @staticmethod
    def create_reader(file_type, file_path):
        if file_type == 'shapefile':
            from .shapefile_reader import ShapefileReader
            return ShapefileReader(file_path)
        elif file_type == 'geojson':
            from .geojson_reader import GeoJSONReader
            return GeoJSONReader(file_path)
        else:
            raise ValueError(f"Unknown file type: {file_type}")
