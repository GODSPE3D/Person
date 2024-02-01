from datetime import datetime
from flask import make_response, jsonify


class customResponse:
    def __init__(self):
        self.status_code = 200
        self.message = ""
        self.url = ""
        self.timestamp = datetime.now()
        self.list = []
        self.person = {}
    
    def createResponse(self):
        return make_response(jsonify({"data": self.list, "message": self.message, "status_code": self.status_code}))
    
    def createIdResponse(self):
        print(self.person, self.status_code)
        return make_response(jsonify({"data": self.person, "message": self.message, "status_code": self.status_code}))