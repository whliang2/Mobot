import sys
import pickle
sys.path.append('../../')

from src.utils.Exporter.ExportInterface import ExportInterface


class ModelExporter(ExportInterface):
    def __init__(self):
        pass

    @staticmethod
    def save_file(target: object, target_dir: str, file_name: str):
        """
        Save the model object to static file in the models folder by identify the package name
        :param target: model object <statsmodel> <skilearn>
        :param target_dir: string 'project model folder'
        :param file_name: string 'model name'
        :return:
        """
        package_name = target.__class__.__module__.split(".")[0]

        if package_name == 'statsmodels':
            target.save(f'{target_dir}/{file_name}')
            print('statsmodels saved...')
        elif package_name == 'sklearn':
            # save sklearn model
            with open(f'{target_dir}/{file_name}', 'wb') as file:
                pickle.dump(target, file)
            print('sklearn saved...')
