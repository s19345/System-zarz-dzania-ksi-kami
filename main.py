import json
import sys
import logging
from pathlib import Path

from watchdog.observers import Observer
from watchdog.events import LoggingEventHandler, FileSystemEventHandler

def load_config(file):
    with open(file) as f:
        return json.load(f)

# class FileHandler(FileSystemEventHandler):
#     def on_created(self, event):
#         filepath = Path(config["WATCHED_DIR"])
#         if filepath.suffix in ['.csv', '.xlsx']:
#             print(f"Znaleziono plik: {filepath.name}")

if __name__ == "__main__":
    pass
    # config = load_config("config.json")
    # event_handler = LoggingEventHandler()
    # observer = Observer()
    # # observer.schedule(event_handler, path, recursive=True)
    # observer.start()
    # try:
    #     while observer.is_alive():
    #         observer.join(1)
    # finally:
    #     observer.stop()
    #     observer.join()
