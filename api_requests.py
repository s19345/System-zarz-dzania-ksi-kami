import urllib.request
import json
from typing import Any

import pandas as pd

from config_loader import load_config

CONFIG = load_config("config.json")


def get_openlibrary_data(title: str, author_full_name: str) -> dict[str, Any]:
    query = title.replace(" ", "+")
    url = CONFIG.get("search_url").format(query=query)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    json_data = json.loads(data.decode())
    for data in json_data["docs"]:
        if data["title"] == title and data["author_name"][0] == author_full_name:
            first_publish_year =  data["first_publish_year"]
            edition_count = data["edition_count"]
            author_key = data["author_key"][0]
            bio = get_author_bio(author_key) if author_key else None
            return {
                "first_publish_year": first_publish_year,
                "edition_count": edition_count,
                "bio": bio
            }
    return None


def get_author_bio(author_key: str) -> str:
    url = CONFIG.get("author_url").format(author=author_key)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    json_data = json.loads(data.decode())
    bio = json_data["bio"]
    return bio

