from flask_classful import FlaskView, route
from flask import render_template, request

from .response_code import *

class ViewAPI(FlaskView):

    def __init__(self, model):
        self.model = model

    @route('/')
    @route('/<name>')
    def get(self, name: str = None):
        user = self.model.get_data(name)
        return OKStatus(f"query ok", user).get_response()

    def post(self, name: str):
        data = request.json
        try:
            self.model.create_document(name, **data)
        except RuntimeError as e:
            return BadRequest(str(e)).get_response()
        except:
            InternalServerError("internal server error").get_response()
        return Created(f"user {name} created").get_response()

    def put(self, name: str):
        data = request.json
        try:
            self.model.modify_document(name, **data)
        except RuntimeError as e:
            return BadRequest(str(e)).get_response()
        except:
            InternalServerError("internal server error").get_response()
        return Created(f"user {name} modify").get_response()
    
    def delete(self, name: str):
        try:
            self.model.delete_document(name)
        except RuntimeError as e:
            return BadRequest(str(e)).get_response()
        except:
            InternalServerError("internal server error").get_response()
        return OKStatus(f"user {name} delete").get_response()