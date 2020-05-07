import typing as Any
import sys

sys.path.append('../../')

from src.utils.Exporter.ExportInterface import ExportInterface


class CsvExporter(ExportInterface):

    @staticmethod
    def save_file(target: Any, target_dir: str, file_name: str):
        try:
            target.to_csv(f'{target_dir}/{file_name}.csv')
            print(f'Export {file_name}.csv to {target_dir} successfully!')
        except Exception as e:
            # append empty list if error happened
            print(e)
