import pandas as pd
import sys
from sklearn.datasets import make_blobs
from sklearn.neighbors import KernelDensity
from sklearn.model_selection import GridSearchCV
import numpy as np

sys.path.append('../../../../')

from src.preprocess.utils.Imputation.ImputatorInterface import ImputatorInterface



class KDEImputator(ImputatorInterface):
    """
        Substitute missing value by random value based on Kernel Density Estimation (KDE)
    """
    def impute(self, data: pd.DataFrame, column_name: str) -> None:
        # Create test-data
        data_x, data_y = make_blobs(n_samples=100, n_features=1, centers=7, cluster_std=0.5, random_state=0)

        # Fit KDE (cross-validation used!)
        params = {'bandwidth': data[column_name].dropna().to_numpy()}
        print(data[column_name].dropna().to_numpy())
        grid = GridSearchCV(KernelDensity(bandwidth=0.5), params)
        grid.fit(data_x)
        kde = grid.best_estimator_

        # Resample
        N_POINTS_RESAMPLE = 1
        data[column_name] = data[column_name].apply(lambda x: kde.sample(N_POINTS_RESAMPLE)[0][0] if pd.isnull(x) else x)





if __name__ == '__main__':
    print('### KDEImputator ###')
    kde = KDEImputator()
    df = pd.DataFrame([[3, 2, np.nan, 0],
                   [3, 4, np.nan, 1],
                   [3, np.nan, np.nan, 5],
                   [np.nan, 3, np.nan, 4]],
                  columns=list('ABCD'))
    print(df)
    kde.impute(df, 'A')
    print(df)