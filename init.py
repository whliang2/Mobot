import os


if __name__ == '__main__':
    print('### Initialization ###')

    # create data folder with pipeline sub directories
    try:
        os.mkdir('./data')
        os.mkdir('./data/preprocessed')
        os.mkdir('./data/split')
        os.mkdir('./data/model')
        os.mkdir('./data/model/models')
        os.mkdir('./data/estimate')
        print('Create data folder successfully!')
    except OSError as error:
        print(error)