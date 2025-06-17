import os
import re
from typing import Pattern

import pandas as pd

from api_requests import get_openlibrary_data
from config_loader import load_config

CONFIG = load_config("config.json")

def remove_internal(data_frame: pd.DataFrame) -> pd.DataFrame:
    """removing all columns containing "internal" word"""
    for i in data_frame.columns:
        if "internal" in i:
            data_frame.drop(i, axis=1, inplace=True)
    return data_frame


def capital_letters(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    # todo st. james nie zadziala
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
    directory = CONFIG["watched_dir"]
    if file.endswith(".xlsx"):
        return pd.read_excel(os.path.join(directory, file))
    elif file.endswith(".csv"):
        return pd.read_csv(os.path.join(directory, file))
    else:
        raise ValueError("File extension must be .csv or .xlsx")


def delete_file(file: str) -> None:
    directory = CONFIG["watched_dir"]
    filepath = os.path.join(directory, file)
    try:
        os.remove(filepath)
    except FileNotFoundError:
        print(f"File {filepath} not found.")
    except PermissionError:
        print(f"Permission for removing {filepath} denied")


def filter_data_frame_by_publisher_and_author(data_frame: pd.DataFrame) -> pd.DataFrame:
    # todo moze zmodyfikowac funkcje aby byla reuzywalna
    publisher_filter = data_frame['Publisher'].isin(('Random house', 'Penguin random house'))
    author_filter = (data_frame['Name'] == 'Stephen') & (data_frame['Surname'] == 'King')
    return data_frame[publisher_filter | author_filter]

def remove_empty_records(data_frame: pd.DataFrame) -> pd.DataFrame:
    data_frame.dropna(how='any', inplace=True)
    return data_frame

def save_to_cache(data_frame: pd.DataFrame, file) -> None:
    directory = CONFIG.get("cache_dir")
    file_name_without_extension = os.path.splitext(file)[0]
    cached_filename = f"{file_name_without_extension}.pkl"
    data_frame.to_pickle(os.path.join(directory, cached_filename))

def load_cache(file) -> pd.DataFrame | None:
    directory = CONFIG.get("cache_dir")
    os.makedirs(directory, exist_ok=True)
    file_name_without_extension = os.path.splitext(file)[0]
    cached_filename = f"{file_name_without_extension}.pkl"
    try:
        return pd.read_pickle(os.path.join(directory, cached_filename))
    except FileNotFoundError:
        print(f"File {cached_filename} not found in cache.")


def add_data_to_dataframe(data_frame: pd.DataFrame) -> pd.DataFrame:
    for idx, row in data_frame.iterrows():
        title = row["Title"]
        name = row["Name"]
        surname = row["Surname"]
        author_full_name = name + " " + surname
        api_data = get_openlibrary_data(title, author_full_name)
        if api_data is not None:
            for key, value in api_data.items():
                if not value:
                    value = pd.NA
                else:
                    data_frame.at[idx, key] = value
    print(data_frame.head())
    data_frame.to_csv("zmeczona.csv")
    return data_frame










