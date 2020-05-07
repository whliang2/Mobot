import sys
sys.path.append('../../../../')

from src.preprocess.utils.Interface.FactoryInterface import FactoryInterface
from src.utils.Importer.CsvFetcher import CsvFetcher
from src.utils.Importer.ModelFetcher import ModelFetcher



class ImporterFactory(FactoryInterface):
    """
        Manufacture the source object by name
        :return source object
    """
    def __init__(self, object_name: str):
        self._object_name = object_name

    def generate(self):
        try:
            source_map = {
                'csv': CsvFetcher,
                'model' : ModelFetcher
            }
            return source_map[self._object_name]()

        except Exception as e:
            print('<<< SourceFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None


if __name__ == "__main__":
    print('### ImporterFactory ###')
    print(ImporterFactory('csv').generate())
