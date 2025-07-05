# app/routes.py

from flask import Blueprint, render_template, request
from app.summarizer import abstractive_summary, extractive_summary

main = Blueprint("main", __name__)

@main.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        text = request.form.get("text")
        method = request.form.get("method")
        if method == "abstractive":
            summary = abstractive_summary(text)
        else:
            summary = extractive_summary(text)
        return render_template("result.html", summary=summary, original=text)
    return render_template("index.html")
