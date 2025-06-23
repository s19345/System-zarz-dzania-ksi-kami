from pathlib import Path

from api import create_api
from file_watcher import FileWatcher
from config_loader import load_config

if __name__ == "__main__":
    config = load_config("config.json")
    watched_dir = Path(config["watched_dir"])
    file_watcher = FileWatcher(watched_dir)
    file_watcher.scan()
    app = create_api(file_watcher)
    app.run(debug=True)
