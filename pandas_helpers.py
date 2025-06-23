import os
import re
from typing import Pattern

import pandas as pd

from logger import set_up_logger
from api_requests import get_openlibrary_data
from config_loader import load_config

logger = set_up_logger(__name__)

CONFIG = load_config("config.json")


def remove_internal(data_frame: pd.DataFrame) -> pd.DataFrame:
    """removing all columns containing "internal" word"""
    for i in data_frame.columns:
        if "internal" in i:
            data_frame.drop(i, axis=1, inplace=True)
            logger.info(f"removing column {i} from DataFrame")
    return data_frame


def capital_letters(data_frame: pd.DataFrame, columns: list[str]) -> pd.DataFrame:
    """reformatting authors' names to always start with a capital letter"""
    if set(columns).issubset(set(data_frame.columns)):
        for column in columns:
            data_frame[column] = data_frame[column].str.capitalize()
            logger.info(f"Capitalizing column {column} in DataFrame")
    return data_frame


def check_file(file: str) -> bool:
    """checking if file matches regex patterns in config.json"""
    allowed_patterns: list[str] = CONFIG["patterns"]
    compiled_patterns: list[Pattern] = [re.compile(p) for p in allowed_patterns]
    logger.info(f"Checking file {file} against patterns")
    for p in compiled_patterns:
        if p.match(file):
            return True
    return False


def load_file(file: str) -> pd.DataFrame | ValueError:
    """loads a .csv or .xlsx file from the watched directory into a DataFrame."""
    directory = CONFIG["watched_dir"]
    if file.endswith(".xlsx"):
        logger.info(f"Loading Excel file: {file}")
        return pd.read_excel(os.path.join(directory, file))
    elif file.endswith(".csv"):
        logger.info(f"Loading CSV file: {file}")
        return pd.read_csv(os.path.join(directory, file))
    else:
        logger.error(f"Unsupported file type: {file}")
        raise ValueError("File extension must be .csv or .xlsx")


def delete_file(file: str) -> None:
    """removes a file from the watched directory if it exists."""
    directory = CONFIG["watched_dir"]
    filepath = os.path.join(directory, file)
    try:
        os.remove(filepath)
        logger.info(f"File {filepath} deleted successfully.")
    except FileNotFoundError:
        logger.error(f"File {filepath} not found.")
    except PermissionError:
        logger.warning(f"Permission for removing {filepath} denied")


def filter_data_frame_by_publisher_and_author(data_frame: pd.DataFrame) -> pd.DataFrame:
    """filters the DataFrame to include only records from specific publishers or books authored by Stephen King."""
    publisher_filter = data_frame['Publisher'].isin(('Random house', 'Penguin random house'))
    author_filter = (data_frame['Name'] == 'Stephen') & (data_frame['Surname'] == 'King')
    logger.info("Filtering DataFrame by publisher and author")
    return data_frame[publisher_filter | author_filter]


def remove_empty_records(data_frame: pd.DataFrame) -> pd.DataFrame:
    """removes rows from the DataFrame that contain any missing values."""
    data_frame.dropna(how='any', inplace=True)
    logger.info("Removing empty records from DataFrame")
    return data_frame


def save_to_cache(data_frame: pd.DataFrame, file) -> None:
    """saves the given DataFrame to a pickle file in the cache directory."""
    directory = CONFIG.get("cache_dir")
    os.makedirs(directory, exist_ok=True)
    file_name_without_extension = os.path.splitext(file)[0]
    cached_filename = f"{file_name_without_extension}.pkl"
    data_frame.to_pickle(os.path.join(directory, cached_filename))
    logger.info(f"DataFrame saved to cache as {cached_filename}")


def load_cache(file) -> pd.DataFrame | None:
    """loads a cached DataFrame from a pickle file if it exists."""
    directory = CONFIG.get("cache_dir")
    file_name_without_extension = os.path.splitext(file)[0]
    cached_filename = f"{file_name_without_extension}.pkl"
    try:
        logger.info(f"Loading DataFrame from cache: {cached_filename}")
        return pd.read_pickle(os.path.join(directory, cached_filename))
    except FileNotFoundError:
        logger.info(f"File {cached_filename} not found in cache.")


def add_data_to_dataframe(data_frame: pd.DataFrame) -> pd.DataFrame:
    """enriches the DataFrame with additional data from the OpenLibrary API
    based on the book title and author's full name."""
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
                data_frame.at[idx, key] = value
    logger.info("Adding additional data to DataFrame from external API")
    return data_frame
