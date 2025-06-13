import json
import os
import sys
import logging
import time
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

def load_config(file):
    with open(file) as f:
        return json.load(f)

def format_file(file: str) -> None:
    print(file, "sformatuj ten plik")


if __name__ == "__main__":
    config = load_config("config.json")
    watched_dir = Path(config["WATCHED_DIR"])
    known_files = os.listdir(watched_dir)
    for file in known_files:
        format_file(file)

    while True:
        current_files = os.listdir(watched_dir)
        new_files = set(current_files) - set(known_files)
        for file in new_files:
            format_file(file)
        known_files.update(new_files)
        time.sleep(1)

