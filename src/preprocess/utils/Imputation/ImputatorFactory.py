import sys

sys.path.append('../../../../')

from src.preprocess.utils.Imputation.MeanImputator import MeanImputator
from src.preprocess.utils.Interface.FactoryInterface import FactoryInterface
from src.preprocess.utils.Imputation.MedianImputator import MedianImputator
from src.preprocess.utils.Imputation.ZeroImputator import ZeroImputator
from src.preprocess.utils.Imputation.KDEImputator import KDEImputator


class ImputatorFactory(FactoryInterface):
    """
        Manufacture the imputator object by name
        :return source object
    """
    def __init__(self, object_name: str):
        self._object_name = object_name

    def generate(self) -> object:
        try:
            imputation_map = {
                'mean': MeanImputator,
                'median': MedianImputator,
                'zero': ZeroImputator,
                'kde': KDEImputator
            }
            return imputation_map[self._object_name]()

        except Exception as e:
            print('<<< ImputatorFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None


if __name__ == "__main__":
    print('### Imputator Factory ###')
    print(ImputatorFactory('mean').generate())
