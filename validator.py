import pandas as pd

import glob
from chardet.universaldetector import UniversalDetector


def detecting_encoding(input_path):
    detector = UniversalDetector()

    for filename in glob.glob(f'{input_path}'):

        detector.reset()
        for line in open(filename, 'rb'):
            detector.feed(line)
            if detector.done: break
        detector.close()
        encode = detector.result['encoding']

        return encode


def filter(input_path, outputfilename):
    read_data = pd.read_csv(f'{input_path}', encoding="UTF-16LE", sep="\t")

    read_data = read_data.loc[:, ~read_data.columns.str.contains('^Unnamed')]

    for column_name in read_data.iloc[:, 7:23]:
        read_data[column_name].fillna('Null', inplace=True)
    column_names = []
    for column_name in read_data.iloc[:, 5:23]:
        column_names.append(column_name)

    search_values = ['New', 'Null', '.']

    combining_values = dict(zip(column_names, ([index] for index in search_values)))

    read_data_new = read_data[read_data[column_names].isin(combining_values).any(axis=1)]



    # after filteration csv file will be generated containing the keys whoose status is new or any cell is empty
    read_data_new.to_csv(f'{outputfilename}', encoding="UTF-16LE", sep=",", index=False)

