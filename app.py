from flask import Flask, render_template, request
from flask_flatpages import FlatPages, pygments_style_defs
from flask_paginate import Pagination, get_page_args

# Configs
DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'
FLATPAGES_MARKDOWN_EXTENSIONS = ['codehilite', 'tables']
FLATPAGES_EXTENSION_CONFIGS = {
    'codehilite': {
        'linenums': True
    }
}

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)

def get_posts(posts, offset=0, per_page=5):
    return posts[offset: offset + per_page]

@app.route('/')
def index():
    posts = sorted(pages, reverse=True, key=lambda p: p.meta['date'])
    page, per_page, offset = get_page_args(page_parameter='page', per_page_parameter='per_page')
    total = len(posts)   
    pagination_posts = get_posts(posts=posts, offset=offset, per_page=per_page)
    pagination = Pagination(page=page, per_page=per_page, total=total)
    return render_template('index.html', posts=pagination_posts, page=page, per_page=per_page, pagination=pagination)

@app.route("/<path:path>/")
def page(path):
    page = pages.get_or_404(path)
    return render_template("page.html", page=page, pages=pages)

@app.route('/tag/<string:tag>/')
def tag(tag):
    tagged = [p for p in pages if tag in p.meta.get('tags', [])]
    return render_template('tag.html', pages=tagged, tag=tag)

@app.route('/pygments.css')
def pygments_css():
    return pygments_style_defs('stata-dark'), 200, {'Content-Type': 'text/css'}

if __name__ == "__main__":
    app.run(port=8080)