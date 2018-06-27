#!/usr/bin/env python3

import base64
import os
import platform

from flask import Flask, render_template, request, redirect, url_for, session
from model import Donation, Donor


app = Flask(__name__)


@app.route('/')
def home():
    return redirect(url_for('all'))


@app.route('/donations/')
def all():
    donations = Donation.select()
    return render_template('donations.jinja2', donations=donations)


@app.route('/add/')
def not_yet_implemented(donor_name=None):
    return '<h2>Not yet implemented</h2>'


@app.route('/donations/<donor_name>')
def single_donor(donor_name):
    donations = Donation().select().join(Donor).where(Donor.name == donor_name)
    return render_template('donations.jinja2', donations=donations)


@app.route('/showalice/')
def show_alice(donor_name="Alice"):
    donations = Donation().select().join(Donor).where(Donor.name == donor_name)
    return render_template('donations.jinja2', donations=donations)


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 6738))
    # enable 0/0 for heroku
    if platform.system() == 'Darwin':
        # Running on development laptop (do not expose external port).
        # heroku is not expected to run using MacOS
        app.run(host='127.0.0.1', port=port)
    else:
        app.run(host='0.0.0.0', port=port)
