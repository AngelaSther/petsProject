import os, uuid
from app import app, db
from flask import render_template, redirect, url_for, request, session
from werkzeug.utils import secure_filename

from sqlalchemy.exc import IntegrityError


@app.route('/ongs', methods=["GET", "POST"])
def ongs():
  return render_template('ongs.html')