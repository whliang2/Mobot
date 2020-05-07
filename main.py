import yaml

from src.Pipeline import Pipeline

if __name__ == '__main__':
    print('### Mobot ###')

    with open('execution_plan.yaml') as file:
        execution_plan = yaml.load(file, Loader=yaml.FullLoader)

    pipeline = Pipeline(execution_plan)
    pipeline.exec()
