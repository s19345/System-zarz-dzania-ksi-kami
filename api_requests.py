import urllib.request
import json
from typing import Any

from config_loader import load_config
from logger import set_up_logger

CONFIG = load_config("config.json")

logger = set_up_logger(__name__)


def normalize_string(text: str) -> str:
    """changes all letter to lowercase and removes spaces"""
    return text.lower().replace(" ", "")


def get_openlibrary_data(title: str, author_full_name: str) -> dict[str, Any] | None:
    """downloads data from api for a certain book by title and author"""
    query = title.replace(" ", "+")
    url = CONFIG.get("search_url").format(query=query)
    with urllib.request.urlopen(url) as response:
        if response.status != 200:
            logger.error(f"Error fetching data from API with status code: {response.status}")
            return None
        data = response.read()
    json_data = json.loads(data.decode())
    for data in json_data["docs"]:
        if normalize_string(data.get("title")) == normalize_string(title) and normalize_string(
                data.get("author_name", [None])[0]) == normalize_string(author_full_name):
            first_publish_year = data.get("first_publish_year")
            edition_count = data.get("edition_count")
            author_key = data.get("author_key", [None])[0]
            bio = get_author_bio(author_key) if author_key else None
            data = {
                "first_publish_year": first_publish_year,
                "edition_count": edition_count,
                "bio": bio
            }

            logger.debug(f"Found data for title: {title}, author: {author_full_name}")
            logger.debug(f"Data: {data}")
            return data
    return None


def get_author_bio(author_key: str) -> str:
    """downloads a bio for a certain author by author_key"""
    url = CONFIG.get("author_url").format(author=author_key)
    with urllib.request.urlopen(url) as response:
        data = response.read()
    json_data = json.loads(data.decode())
    bio = json_data.get("bio")
    return bio
