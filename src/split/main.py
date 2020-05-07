import sys
sys.path.append('../../')

from src.split.SplitFactory import SplitFactory
from src.split.SplitManager import SplitManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager


class Split:
    def __init__(self, exec_plan: dict):
        self._exec_plan = exec_plan

    def exec(self) -> None:
        """
        Split data into test training set and save into split folder
        :return: None
        """

        # ----------
        # get data from preprocessed file
        # ----------
        importer_object = ImporterFactory('csv').generate()
        importer_manager = ImporterManager(importer_object)
        data = importer_manager.exec(self._exec_plan['source_dir'])[0]

        # ----------
        # split data
        # ----------
        splitter = SplitFactory(self._exec_plan['method']).generate()
        training, testing = SplitManager(splitter).exec(data, self._exec_plan['criteria'])

        # ----------
        # save file
        # ----------
        loader = ExportFactory('csv').generate()
        saver = ExportManager(loader)
        saver.exec(training.reset_index(drop=True), self._exec_plan['target']['dir'], 'training')
        saver.exec(testing.reset_index(drop=True), self._exec_plan['target']['dir'], 'testing')
        print('=== Finished split ===')



if __name__ == '__main__':
    print('### Split Main File ###')
    split_exec_plan = {
        'source_dir': [{
            'dir': '../../data/preprocessed/',
            'files': ['covid19_preprocessed.csv']
        }],
        'target': {
            'dir': '../../data/split'
        },
        'method': 'ratio',
        'criteria': {
            'ratio': 0.8
            # "column_name" : "criteria column",
            # "train_values": ["Training data value1", ""Training data value2""],
            # "test_values": ["Testing data value1"]
        }
    }

    # init split object
    splitter = Split(split_exec_plan)
    splitter.exec()


