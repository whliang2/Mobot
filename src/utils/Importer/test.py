import sys
sys.path.append('../../../')

from src.utils.Importer.ImporterManager import ImporterManager
from src.utils.Importer.ImporterFactory import ImporterFactory


if __name__ == '__main__':
    # importer_object = ImporterFactory('csv').generate()
    # importer_manager = ImporterManager(importer_object)
    # files = [{
    #     'dir': '../../../data/source/',
    #     'files': ['he_li_pd.csv', 'death_recovery_gdp_unemp_withnan.csv']
    # }, {
    #     'dir': '../../../data/preprocessed/',
    #     'files': ['covid_19.csv']
    # }]
    # importer_manager.exec(files)
    # print(importer_manager.exec(files))

    files = [{
        'dir': '../../../data/model/models/',
        'files': ["sklearn_AIC.pkl"]
    }]

    fetcher_object = ImporterFactory('model').generate()
    importer_manager = ImporterManager(fetcher_object)
    aic_model_test = importer_manager.exec(files)
    print(aic_model_test)





