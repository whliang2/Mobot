import sys

sys.path.append('../../../../')

from src.preprocess.utils.Interface.FactoryInterface import FactoryInterface
from src.preprocess.utils.Transform.LogTransform import LogTransform
from src.preprocess.utils.Transform.RootSquareTransform import RootSquareTransform


class TransformFactory(FactoryInterface):
    """
        Manufacture the transform object by name
        :return source object
    """

    def __init__(self, transform_name: str):
        self._transform_name = transform_name

    def generate(self):
        try:
            transform_map = {
                'log': LogTransform,
                'root_square': RootSquareTransform
            }
            return transform_map[self._transform_name]()

        except Exception as e:
            print('<<< ImputatorFactory Error >>>')
            print(f'Exception type {e.__class__.__name__}, Invalid param {e}')
            return None


if __name__ == "__main__":
    print('### Transform Factory ###')
    print(TransformFactory('log').generate())
