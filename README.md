# Flask Illuminati App

![img](https://raw.githubusercontent.com/the-akira/Flask-Illuminati-App/master/static/Avatar.png)

A simple Illuminati themed Blog made with Flask

## Features

- Markdown Support
- Syntax Highlighting
- Tables
- Tags
- Dates
- Pagination

You can see an example here: **https://flaskilluminati.herokuapp.com**

## Installation

### Clone the Repository

```
git clone https://github.com/the-akira/Flask-Illuminati-App.git
```

### Inside the Main Directory

Create a Virtual Environment

```
python -m venv myvenv
```

Activate the Virtual Environment

```
source myvenv/bin/activate
```

Install Requirements

```
pip install -r requirements.txt
```

Run the Application

```
python app.py
```

In order to change the default number of posts per page you have to change the **per_page** variable in `flask_paginate.__init__.py` file
