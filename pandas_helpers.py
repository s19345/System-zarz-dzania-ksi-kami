import pandas as pd

df = pd.read_excel(io="./new_data/example_input_file.xlsx")
print(df.head())

def remove_internal(data_frame: pd.DataFrame) -> pd.DataFrame:
    """removing all columns containing "internal" word"""
    for i in data_frame.columns:
        if "internal" in i:
            data_frame.drop(i, axis=1, inplace=True)
    return data_frame

remove_internal(df)

def capital_letters(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """reformatting authors' names to always start with a capital letter"""
    if set(columns).issubset(set(data_frame.columns)):
        for column in columns:
            data_frame[column] = data_frame[column].str.capitalize()
        return data_frame

