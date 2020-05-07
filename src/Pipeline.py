import sys

sys.path.append('../')

from src.preprocess.main import Preprocess
from src.split.main import Split
from src.models.main import Model
from src.estimate.main import Estimate


class Pipeline:
    def __init__(self, exec_plan):
        self._exec_plan = exec_plan

    def exec(self):
        pipeline_steps = ['preprocess_plan', 'split_plan', 'model_plan', 'estimate_plan']

        if list(self._exec_plan.keys()) == pipeline_steps:
            preprocessor = Preprocess(self._exec_plan['preprocess_plan'])
            preprocessor.exec()
            splitter = Split(self._exec_plan['split_plan'])
            splitter.exec()
            modeler = Model(self._exec_plan['model_plan'])
            modeler.exec()
            estimator = Estimate(self._exec_plan['estimate_plan'])
            estimator.exec()
            print('!!! === All Done === !!!')
        else:
            print("Error: execution plan step mismatch, please make sure there "
                  "are 'preprocess_plan', 'split_plan', 'model_plan', 'estimate_plan' steps in your plan")


if __name__ == '__main__':
    print('### PipeLine ###')
    execution_plan = {
        'preprocess_plan': {
            'source_dir': '../data/source',
            'target': {
                'file_name': 'covid19_preprocessed',
                'dir': '../data/preprocessed'
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
        },
        'split_plan': {
            'source_dir': [{
                'dir': '../data/preprocessed/',
                'files': ['covid19_preprocessed.csv']
            }],
            'target': {
                'dir': '../data/split'
            },
            'method': 'ratio',
            'criteria': {
                'ratio': 0.8
            }
        },
        'model_plan': {
            'source_dir': [{
                'dir': '../data/split/',
                'files': ['training.csv']
            }],
            'models_target': {
                'dir': '../data/model/models',
            },
            'summary_target': {
                'dir': '../data/model',
                'name': 'covid19_models_summary'
            },
            'predictor_name': ["Health.expenditures....of.GDP.", "Literacy....",
                               "Physicians.density..physicians.1.000.population.",
                               "Obesity - adult prevalence rate (%)", "Life expectancy at birth (years)",
                               "H_bed_density", "Imigrate_Rate", "Pop_Density",
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
        },
        'estimate_plan': {
            'source_dir': [{
                'dir': '../data/split/',
                'files': ['testing.csv']
            }],
            'models_summary': [{
                'dir': '../data/model/',
                'files': ['covid19_models_summary.csv'],
            }],
            'models_dir': '../data/model/models/',
            'summary_target': {
                'dir': '../data/estimate',
                'name': 'estimated_model_data'
            },
        }
    }

    pipeline = Pipeline(execution_plan)
    pipeline.exec()
