from flask_classful import FlaskView
from flask import render_template, request

class ViewWeb(FlaskView):

    def __init__(self, model):
        self.model = model

    def get(self):
        return render_template("home.html")