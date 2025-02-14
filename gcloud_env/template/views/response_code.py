import json
from flask import Response

class OKStatus:
    status_code = 200

    def __init__(self, msg: str, data: list = [], mimetype="application/json"):
        
        self.msg = {"message": msg, "data": data} if len(data) != 0 else {"message": msg}        
        self.resp = Response(json.dumps(self.msg), status=self.status_code, mimetype=mimetype)
    
    def get_response(self) -> Response:
        return self.resp

class Created:
    status_code = 201

    def __init__(self, msg: str, mimetype="application/json"):
        
        self.msg = {"message": msg}        
        self.resp = Response(json.dumps(self.msg), status=self.status_code, mimetype=mimetype)
    
    def get_response(self) -> Response:
        return self.resp


class BadRequest:
    status_code = 400

    def __init__(self, msg: str, mimetype="application/json"):
        
        self.msg = {"message": msg}        
        self.resp = Response(json.dumps(self.msg), status=self.status_code, mimetype=mimetype)
    
    def get_response(self) -> Response:
        return self.resp

class InternalServerError:
    status_code = 500

    def __init__(self, msg: str, mimetype="application/json"):
        
        self.msg = {"message": msg}        
        self.resp = Response(json.dumps(self.msg), status=self.status_code, mimetype=mimetype)
    
    def get_response(self) -> Response:
        return self.resp