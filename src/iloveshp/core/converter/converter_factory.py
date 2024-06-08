class ReaderFactory:
    @staticmethod
    def create_converter(converter_type):
        if converter_type == 'kmz':
            from .kmz_converter import KMZConverter
            return KMZConverter()
        else:
            raise ValueError(f"Unknown converter type: {converter_type}")
