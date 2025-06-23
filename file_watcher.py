import os
from pathlib import Path

import pandas as pd

from logger import set_up_logger
from pandas_helpers import load_cache, load_file, remove_internal, remove_empty_records, capital_letters, \
    filter_data_frame_by_publisher_and_author, add_data_to_dataframe, save_to_cache, check_file, delete_file


class FileWatcher:
    def __init__(self, watched_dir: Path):
        """initializes the FileWatcher with the directory to monitor."""
        self.watched_dir: Path = watched_dir
        self.known_files: set[str] = set()
        self.df: pd.DataFrame = pd.DataFrame()
        self.logger = set_up_logger(__name__)

    def format_file(self, file: str) -> pd.DataFrame:
        """processes a single file: loads, cleans, transforms, and enriches the data."""
        df = load_cache(file)
        if df is None:
            try:
                df = load_file(file)
                df = remove_internal(df)
                df = remove_empty_records(df)
                df = capital_letters(df, ['Name', 'Surname'])
                df = filter_data_frame_by_publisher_and_author(df)
                df = add_data_to_dataframe(df)
                save_to_cache(df, file)
            except ValueError as e:
                self.logger.info(f"File {file} not recognised.")
                return pd.DataFrame()
        return df

    def scan(self) -> pd.DataFrame:
        """scans the watched directory for new valid files, processes them, and updates internal DataFrame."""
        current_files = set(os.listdir(self.watched_dir))
        new_files = current_files - self.known_files
        for file in new_files:
            self.logger.info(f"Scanning {file}...")
            if check_file(file):
                self.df = self.format_file(file)
                self.known_files.add(file)
            else:
                delete_file(file)
                self.logger.info(f"File {file} not recognised and deleted.")

        return self.df
