import json
import os
import re
from typing import Pattern

import pandas as pd

def load_config(file):
    with open(file) as f:
        return json.load(f)

CONFIG = load_config("config.json")

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

def check_file(file: str) -> bool:
    """checking if file matches regex patterns in config.json"""
    # todo funkcja do poprawy, rozszerzenia, aby sprawdzac tez nazwy
    allowed_patterns: list[str] = CONFIG["patterns"]
    compiled_patterns: list[Pattern] = [re.compile(p) for p in allowed_patterns]
    for p in compiled_patterns:
        if p.match(file):
            return True
    return False

def load_file(file: str) -> pd.DataFrame:
    directory = CONFIG["WATCHED_DIR"]
    if file.endswith(".xlsx"):
        pd.read_excel(os.path.join(directory, file))
    elif file.endswith(".csv"):
        pd.read_csv(os.path.join(directory, file))
    else:
        raise ValueError("File extension must be .csv or .xlsx")


def delete_file(file: str) -> None:
    directory = CONFIG["WATCHED_DIR"]
    filepath = os.path.join(directory, file)
    try:
        os.remove(filepath)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
    except PermissionError:
        print(f"Permission for removing {filepath} denied")


def filter_data_frame_by_publisher_and_author(data_frame: pd.DataFrame) -> pd.DataFrame:
    # todo moze zmodyfikowac funkcje aby byla reuzywalna
    publisher_filter = data_frame['Publisher'].isin(('Random House', 'Penguin Random House'))
    author_filter = (data_frame['Name'] == ['Stephen']) & (data_frame['Surname'] == ['King'])
    return data_frame(publisher_filter | author_filter)

def remove_empty_records(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame.dropna(how='any', inplace=True)
    return data_frame





