from flask import Flask, render_template, redirect
from scripts import db_session
from getter import get_data


pages_html = {"items": ("items.html", {'title': 'Items', 'items': lambda: get_data("db/mars_workers.db", 'items')})}


def define_html_file(page):
    return render_template(pages_html[page][0], pages_html[page][1].items())