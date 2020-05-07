import pandas as pd
import sys

sys.path.append('../../')

from src.models.ModelRegister import ModelRegister
from src.models.AIC.AIC import AIC
from src.models.SimpleLm.SimpleLm import SimpleLm
from src.models.StepWise.StepWise import StepWise
from src.utils.Exporter.ExportFactory import ExportFactory
from src.utils.Exporter.ExportManager import ExportManager
from src.utils.Importer.ImporterFactory import ImporterFactory
from src.utils.Importer.ImporterManager import ImporterManager


class Model:
    def __init__(self, exec_plan: dict):
        self._exec_plan = exec_plan

    def exec(self):
        """
        train model base on the experiments from execution plan
        :return:
        """
        # get source
        importer = ImporterFactory('csv').generate()
        importer_manager = ImporterManager(importer)
        data = importer_manager.exec(self._exec_plan['source_dir'])[0]

        # -----
        # import model and register model in command container
        #  TODO: import module dynamically
        # -----
        model_map = {
            'AIC': AIC,
            'StepWise': StepWise,
            'SimpleLm': SimpleLm
        }

        model_register = ModelRegister()

        for model in  self._exec_plan['experiments']:
            model_name = model['name']
            model_register.register(model_name, model_map[model_name],  self._exec_plan['predictor_name'],
                                    self._exec_plan['response_name'])

        # -----
        # Train model from register container
        # -----
        model_table = {}
        for model in self._exec_plan['experiments']:
            result = model_register.exec(model['name'], data, model['criteria'])

            # concat model name from criteria and model type
            if len(model['criteria'].items()) == 0:
                criteria = ''
                model_name = model['name']
            else:
                key, value = list(model['criteria'].items())[0]
                criteria = key + ' ' + str(value)
                model_name = model['name'] + '_' + str(value)

            model_exporter = ExportFactory('model').generate()
            exporter = ExportManager(model_exporter)
            exporter.exec(result[0], self._exec_plan['models_target']['dir'], model_name)

            model_table[model_name] = [self._exec_plan['response_name'], '/'.join(result[1]), criteria]

        # Construct model information csv file
        model_table = pd.DataFrame.from_dict(model_table, orient='index', columns=['response', 'predictors', 'criteria'])
        model_table = model_table.reset_index()
        model_table.columns = ['model_name', 'response', 'predictors', 'criteria']

        # export the result to model folder
        exporter = ExportFactory('csv').generate()
        export_manager = ExportManager(exporter)
        export_manager.exec(model_table, self._exec_plan['summary_target']['dir'], self._exec_plan['summary_target']['name'])
        print('=== Finish modeling ===')


if __name__ == '__main__':
    print('### Model Main ###')

    model_exec_plan = {
        'source_dir': [{
            'dir': '../../data/split/',
            'files': ['training.csv']
        }],
        'models_target': {
            'dir': '../../data/model/models',
        },
        'summary_target': {
            'dir': '../../data/model',
            'name': 'covid19_models_summary'
        },
        'predictor_name': ["Health.expenditures....of.GDP.","Literacy....",
                           "Physicians.density..physicians.1.000.population.",
                           "Obesity - adult prevalence rate (%)","Life expectancy at birth (years)",
                           "H_bed_density","Imigrate_Rate","Pop_Density",
                           "GDP - per capita (PPP) (US$)", "Unemployment rate (%)"],
        'response_name': ['Recovery Rate'],
        'experiments': [{
            'name': 'AIC',
            'criteria': {}
        }, {
            'name': 'SimpleLm',
            'criteria': {}
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.1
            }
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.01
            }
        }, {
            'name': 'StepWise',
            'criteria': {
                'p_value': 0.02
            }
        }, ]
    }

    model = Model(model_exec_plan)
    model.exec()

