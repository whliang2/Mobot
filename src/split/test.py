import pandas as pd
from typing import Tuple


def split(dataframe: pd.DataFrame, key_info_dict :dict ) -> Tuple[pd.DataFrame, pd.DataFrame]:
        key_column = key_info_dict["column_name"]
        train_values = key_info_dict["train_values"]
        test_values = key_info_dict["test_values"]

        train_bool = dataframe[key_column].isin(train_values)
        test_bool = dataframe[key_column].isin(test_values)
        training = dataframe[train_bool]
        testing = dataframe[test_bool]
        return training, testing



if __name__ == '__main__':
    print('### Test ###')

data = {'First_Name':  ["Henry","Andy","Jane"],
        'Last_name': ["Liang", "Lin","Su"],
        'Country_name' :["Taiwan","Taiwan","Japan"]
        }

df_test = pd.DataFrame(data, columns = ['First_Name','Last_name','Country_name'])
# print(df_test)


test_dict = {
        "column_name" : "Country_name",
        "train_values": ["Taiwan"],
        "test_values": ["Japan"]
}



training, testing = split(df_test,test_dict)
print(training)
print(testing)

