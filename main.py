import os
import time
from pathlib import Path

from api import create_api
from pandas_helpers import load_file, check_file, remove_internal, capital_letters, delete_file, \
    filter_data_frame_by_publisher_and_author, remove_empty_records, save_to_cache, load_cache, add_data_to_dataframe
from config_loader import load_config


def format_files(files: list[str]) -> None:
    for file in files:
        if check_file(file):
            df = load_cache(file)
            if df is None:
                try:
                    df = load_file(file)
                except ValueError as e:
                    print(e)
                df = remove_internal(df)
                df = remove_empty_records(df)
                df = capital_letters(df, ['Name', 'Surname'])
                df = filter_data_frame_by_publisher_and_author(df)
                df = add_data_to_dataframe(df)
                save_to_cache(df, file)

            return df
        else:
            delete_file(file)



if __name__ == "__main__":
    config = load_config("config.json")
    watched_dir = Path(config["watched_dir"])
    known_files = os.listdir(watched_dir)
    df = format_files(known_files)
    app = create_api(df)
    app.run(debug=True)

    while True:
        current_files = os.listdir(watched_dir)
        new_files = set(current_files) - set(known_files)
        format_files(new_files)
        known_files.extend(new_files)
        time.sleep(1)

