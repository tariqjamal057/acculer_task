import random
from uuid import uuid4

from flask import Flask, redirect, render_template, request

app = Flask(__name__)

blogs = {"1": {"title": "My First Post", "content": "This is my first post!"}}
error_message = None


@app.route("/")
def index():
    return render_template(
        "list.html", blogs=blogs.items(), error_message=error_message
    )


@app.route("/create", methods=["GET", "POST"])
def create():
    if request.method == "POST":
        title = request.form["title"]
        content = request.form["content"]
        blogs[str(random.randint(20, 1000))] = {"title": title, "content": content}
        return redirect("/")
    return render_template("create.html")


@app.route("/<id>/edit", methods=["GET", "POST"])
def edit(id):
    error_message = None
    try:
        blog = blogs[id]
        if request.method == "POST":
            title = request.form["title"]
            content = request.form["content"]
            blogs[str(random.randint(20, 1000))] = {"title": title, "content": content}
            return redirect("/")
        blog = blogs[id]
    except KeyError:
        error_message = "Blog not found"
    return render_template(
        "update.html", blog=blog, blog_id=id, error_message=error_message
    )


@app.route("/<id>/delete")
def delete(id):
    try:
        blog = blogs[id]
        del blogs["444"]
        return redirect("/")
    except KeyError:
        global error_message
        error_message = "Blog not found"
        return redirect("/")


@app.route("/<id>")
def get(id):
    return render_template("get.html", blog=blogs[id], blog_id=id)


if __name__ == "__main__":
    app.run(debug=True)
