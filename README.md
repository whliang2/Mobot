# IS590_Final_Project - Mobot
Description : This porpose of building this project is to create a data science pipe line application,
and functionality will include from the data collection, data cleaning and all the way to the model evaluation.

Team Members : Teng Yung Lin, Wen Hsuan Liang, Yu Chen Su

# How to use

1. Create conda environment (**Mobot**) from `environmnet.yml` file using `conda env create -f environment.yml`. Conda command should be pre-install.
2. Rename `exection_plan.yaml.template` into `exection_plan.yaml`
3. Edit the detail of `exection_plan.yaml`
    - Source file directory
    - Imputation, transformation methods
    - Train, test split method
4. Run `python init.py` to construct the folder structure for Mobot project
5. Run `python main.py` to execute the experiments
6. The result file will be inside `./data/estimate` folder which shows the model performance of each experiment.

## Dataset :
1. Index Mundi (https://www.indexmundi.com/) 
2. World Meter (https://www.worldometers.info/coronavirus/)

## Reference :
1. Jason Brownlee (2019), Probabilistic Model Selection with AIC, BIC, and MDL, Retrieved from https://machinelearningmastery.com/probabilistic-model-selection-measures/
2. Greg (2013),Is there a library function for Root mean square error (RMSE) in python?, Retrieved from Stack overflow
https://stackoverflow.com/questions/17197492/is-there-a-library-function-for-root-mean-square-error-rmse-in-python
3. Kavindu Dodanduwa (2018), python exception message capturing, Retrieved from Stack overflow
https://stackoverflow.com/questions/4690600/python-exception-message-capturing
4. Jason Brownlee (2016), Save and Load Machine Learning Models in Python with scikit-learn, Retrieved from
https://machinelearningmastery.com/save-load-machine-learning-models-python-scikit-learn/
5. Kamon Ayeva, Sakis Kasampalis (2018), Mastering Python Design Patterns - Second Edition
6. Baran Köseoğlu (2020), Structure Your Data Science Projects - Develop collaborative and reproducible data science projects
https://towardsdatascience.com/structure-your-data-science-projects-6c6c8653c16a
7. Bruno Oliveira (2018), pytest Quick Start Guide




