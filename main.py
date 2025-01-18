# +----------------------------------------------------------------------------+
# | CARDUI WORKS v1.0.0
# +----------------------------------------------------------------------------+
# | Copyright (c) 2024 - 2025, CARDUI.COM (www.cardui.com)
# | Vanessa Reteguín <vanessa@reteguin.com>
# | Released under the MIT license
# | www.cardui.com/carduiframework/license/license.txt
# +----------------------------------------------------------------------------+
# | Author.......: Vanessa Reteguín <vanessa@reteguin.com>
# | First release: January 9th, 2025
# | Last update..: January 18th, 2025
# | WhatIs.......: Cardui Web Development (Upgraded Blog) - Main
# +----------------------------------------------------------------------------+

# ------------ Resources / Documentation involved -------------
# Flask Quickstart: https://flask.palletsprojects.com/en/stable/quickstart/
# Jinja Template Designer Documentation: https://jinja.palletsprojects.com/en/stable/templates/

# ------------------------- Libraries -------------------------
from flask import Flask, render_template
import requests
from post import Post

# ------------------------- Variables -------------------------
app = Flask(__name__)

# --------------------------- Code ----------------------------
@app.route('/')
@app.route('/index.html')
def home():
    blog_url = "https://api.npoint.io/c790b4d5cab58020d391"
    blog_response = requests.get(blog_url)
    all_posts = blog_response.json()
    return render_template("index.html", posts=all_posts)

@app.route('/about.html')
def about():
    return render_template("about.html")

@app.route('/contact.html')
def contact():
    return render_template("contact.html")

@app.route('/footer.html')
def footer():
    return render_template("footer.html")

@app.route('/header.html')
def header():
    return render_template("header.html")

@app.route('/blog/<id>')
def post(id):
    chosenPost = Post(id)
    return render_template("post.html", post=chosenPost)

if __name__ == "__main__":
    app.run(debug=True)
