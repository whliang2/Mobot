import sys
sys.path.append('../../../')

from src.utils.Interface.FactoryInterface import FactoryInterface
from src.utils.Exporter.CsvExporter import CsvExporter
from src.utils.Exporter.ModelExporter import ModelExporter


class ExportFactory(FactoryInterface):
    """
        Manufacture the exporter object by name
        :return exporter object
    """
    def __init__(self, object_name: str):
        self._object_name = object_name

    def generate(self):
        try:
            export_map = {
                'csv': CsvExporter,
                'model': ModelExporter
            }
            return export_map[self._object_name]()

        except Exception as e:
            print('<<< ExporterFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None
