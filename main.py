import os
import time
from pathlib import Path

from pandas_helpers import load_config, load_file, check_file, remove_internal, capital_letters, delete_file, \
    filter_data_frame_by_publisher_and_author, remove_empty_records


def format_files(files: list[str]) -> None:
    for file in files:
        if check_file(file):
            try:
                df = load_file(file)
            except ValueError as e:
                print(e)
            df = remove_internal(df)
            df = remove_empty_records(df)
            df = capital_letters(df)
            df = filter_data_frame_by_publisher_and_author(df)
        else:
            delete_file(file)



if __name__ == "__main__":
    config = load_config("config.json")
    watched_dir = Path(config["WATCHED_DIR"])
    known_files = os.listdir(watched_dir)
    format_files(known_files)

    while True:
        current_files = os.listdir(watched_dir)
        new_files = set(current_files) - set(known_files)
        format_files(new_files)
        known_files.extend(new_files)
        time.sleep(1)

