from flask import Flask, jsonify
from flask.typing import ResponseReturnValue
from file_watcher import FileWatcher


def create_api(file_watcher: FileWatcher) -> Flask:
    """creates a Flask API using the data provided by the FileWatcher."""
    app = Flask(__name__)

    @app.before_request
    def update_data_frame():
        """runs FileWatcher class scan method before each request."""
        file_watcher.scan()

    @app.route("/")
    def index():
        """returns a welcome message and a list of available API endpoints."""
        return jsonify(
            {
                "1. message": "Welcome to the Book API!",
                "2. endpoints": {
                    "GET /books/<author>": "Retrieve books by author name",
                    "GET /books": "Retrieve all books",
                    "GET /books/search/<keyword>": "Search books by title keyword"
                }
            })

    @app.route("/books/<author>")
    def search_books_by_author(author: str) -> ResponseReturnValue:
        """returns all books written by a given author."""
        data_frame = file_watcher.df
        if data_frame.empty:
            return jsonify({"error": "No data found"}), 500
        author = author.lower()
        df_author_name = (data_frame["Name"].str.strip() + data_frame["Surname"].str.strip()).str.lower()
        matches = data_frame[df_author_name == author]
        if matches.empty:
            return jsonify({"error": "No books found"}), 404
        else:
            return jsonify(matches.to_dict(orient="records"))

    @app.route("/books")
    def get_all_books() -> ResponseReturnValue:
        """returns all books in data frame"""
        data_frame = file_watcher.df
        if data_frame.empty:
            return jsonify({"error": "Data not loaded"}), 500
        return jsonify(data_frame.to_dict(orient="records"))

    @app.route("/books/search/<keyword>")
    def search_books_by_title(keyword: str) -> ResponseReturnValue:
        """searching books by provided title"""
        data_frame = file_watcher.df
        if data_frame.empty:
            return jsonify({"error": "Data not loaded"}), 500
        keyword = keyword.lower()
        matches = data_frame[data_frame["Title"].str.lower().str.contains(keyword)]
        return jsonify(matches.to_dict(orient="records"))

    return app
