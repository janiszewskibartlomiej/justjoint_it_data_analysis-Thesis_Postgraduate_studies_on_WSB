import glob
from pprint import pprint

import pandas as pd


class DataProcessing:
    def __init__(self):
        self.filename: str = ""
        self.file_path: str = ""
        self.data: pd.DataFrame = pd.DataFrame()

    def load_data(self, filename=None) -> pd.DataFrame:
        self.filename = filename
        pd.set_option('display.max_columns', 30)
        pd.set_option('display.width', 900)
        self.file_path = glob.glob(f"data/{filename or '*'}.csv")
        self.data = pd.read_csv(filepath_or_buffer=self.file_path.__getitem__(-1))
        return self.data

    def save_data(self, file_path) -> str:
        self.data.to_csv(path_or_buf=file_path or f"new_{self.file_path}")
        return file_path or f"new_{self.file_path}"

    def get_obligatory_and_optional_skills(self):
        headers_optional = list()
        set_obligatory = set()
        set_optional = set()
        for row in self.data.iterrows():
            headers_obligatory = [list(data.keys()).__getitem__(0) for data in list(eval((row[1]).Obligatory_skills))]
            set_obligatory.update(headers_obligatory)
            if str((row[1]).Optional_skills) != "nan":
                headers_optional = [list(data.keys()).__getitem__(0) for data in list(eval((row[1]).Optional_skills))]
            set_optional.update(headers_optional)
        return list(set_obligatory), list(set_optional)

    def headers_processing(self) -> list:
        current_headers = self.data.columns.to_list()
        new_headers = current_headers[:4]
        new_headers.append(f"{current_headers[4]}_from")
        new_headers.append(f"{current_headers[4]}_to")
        new_headers.append(f"{current_headers[5]}_from")
        new_headers.append(f"{current_headers[5]}_to")
        obligatory, optional = self.get_obligatory_and_optional_skills()
        new_headers.extend(obligatory)
        new_headers.extend(optional)
        return new_headers


if __name__ == '__main__':
    x = DataProcessing()
    y = x.load_data()
    pprint(x.headers_processing())
    print()
    pprint(len(x.headers_processing()))
