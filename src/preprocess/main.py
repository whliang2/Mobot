import sys

sys.path.append('../../')

from src.preprocess.CreateFlatTable import CreateFlatTable
from src.preprocess.Imputation import Imputation
from src.preprocess.Transformation import Transformation
from src.preprocess.PreprocessCommandContainer import PreprocessCommandContainer
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager


class Preprocess:
    def __init__(self, exec_plan: dict):
        self._exec_plan = exec_plan

    def exec(self):
        """
        execute whole preprocess
        """
        # create register container
        preprocess_command_register = PreprocessCommandContainer()

        # --------
        # Register all the preprocess comamand
        # --------
        # TODO: extract merge functions and get source
        preprocess_command_register.register('create_flat_from_csv',
                                             CreateFlatTable(self._exec_plan['source_dir'],
                                                             {'merge_key': 'Country', 'from_type': 'csv'}))
        # register imputation
        imputation_types = [el['type'] for el in self._exec_plan['imputation']]
        for imputation_type in imputation_types:
            preprocess_command_register.register(f'imputation_by_{imputation_type}', Imputation({'type': imputation_type}))

        # register transform
        transform_types = [el['type'] for el in self._exec_plan['transformation']]
        for transform_type in transform_types:
            preprocess_command_register.register(f'transform_by_{transform_type}', Transformation({'type': transform_type}))

        # ----------
        # execute command
        # ----------
        flat_table = preprocess_command_register.get('create_flat_from_csv').exec()

        for imputation in self._exec_plan['imputation']:
            preprocess_command_register.get(f"imputation_by_{imputation['type']}").exec(imputation['columns'], flat_table)

        for transform in self._exec_plan['transformation']:
            preprocess_command_register.get(f"transform_by_{transform['type']}").exec(transform['columns'], flat_table)

        # ----------
        # save file
        # ----------
        loader = ExportFactory('csv').generate()
        saver = ExportManager(loader)
        saver.exec(flat_table, self._exec_plan['target']['dir'], self._exec_plan['target']['file_name'])
        print('=== Finish preprocess ===')



if __name__ == '__main__':
    print('### Preprocess Main file ###')

    preprocess_exec_plan = {
        'source_dir': '../../data/source',
        'target': {
            'file_name': 'covid19_preprocessed',
            'dir': '../../data/preprocessed'
        },
        'imputation': [
            {
                'columns': ['Pop_Density', 'Death Rate', 'Health.expenditures....of.GDP.', 'Literacy....',
                            'Physicians.density..physicians.1.000.population.',
                            'Obesity - adult prevalence rate (%)',
                            'Life expectancy at birth (years)', 'H_bed_density', 'Imigrate_Rate',
                            'Pop_Density', 'Death Rate', 'Recovery Rate'],
                'type': 'mean'
            },
            {
                'columns': ['Literacy....', 'GDP - per capita (PPP) (US$)', 'Unemployment rate (%)'],
                'type': 'zero'
            }
        ],
        'transformation': [
            {
                'columns': ['Pop_Density'],
                'type': 'log'
            },
            {
                'columns': ['Literacy....'],
                'type': 'root_square'
            }
        ]
    }

    preprocessor = Preprocess(preprocess_exec_plan)
    preprocessor.exec()

