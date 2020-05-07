import pandas as pd
import numpy as np
import sys

from src.preprocess.utils.Imputation.ZeroImputator import ZeroImputator

sys.path.append('../../../../../')


def test_action():
    # Create dummy dataframe
    test_df = pd.DataFrame({'foo': [1.0, 2.0, np.nan, np.nan, 4.0, 5.0]})
    result_df = pd.DataFrame({'foo': [1.0, 2.0, 0.0, 0.0, 4.0, 5.0]})

    # test mean imputator
    mean_imputator = ZeroImputator()
    mean_imputator.impute(test_df, 'foo')

    assert test_df.equals(result_df)


