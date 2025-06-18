import pandas as pd
from flask import Flask, jsonify, Response


def create_api(data_frame: pd.DataFrame) -> Flask:
    app = Flask(__name__)

    @app.route("/")
    def index():
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
    def search_books_by_author(author: str) -> Response:
        if data_frame is None:
            return jsonify({"error": "No data found"}), 500
        author = author.lower()
        df_author_name = (data_frame["Name"].str.strip() + data_frame["Surname"].str.strip()).str.lower()
        matches = data_frame[df_author_name == author]
        matches = matches[["Title", "Name", "Surname", "first_publish_year", "edition_count"]]
        if matches.empty:
            return jsonify({"error": "No books found"}), 404
        else:
            return jsonify(matches.to_dict(orient="records"))  # todo do sprawdzenia czy default value bedzie ok

    @app.route("/books")
    def get_all_books():
        if data_frame is None:
            return jsonify({"error": "Data not loaded"}), 500
        print(data_frame.columns)
        result = data_frame[["Title", "Name", "Surname", "first_publish_year", "edition_count"]]

        return jsonify(result.to_dict(orient="records"))

    @app.route("/books/search/<keyword>")
    def search_books_by_title(keyword: str) -> Response:
        if data_frame is None:
            return jsonify({"error": "Data not loaded"}), 500
        keyword = keyword.lower()
        matches = data_frame[data_frame["Title"].str.lower().str.contains(keyword)]
        result = matches[["Title", "Name", "Surname", "first_publish_year", "edition_count"]]
        return jsonify(result.to_dict(orient="records"))

    return app
