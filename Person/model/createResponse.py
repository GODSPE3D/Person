from flask import Response, make_response


resp = Response
content = ""
status_code = 0

resp = make_response(content, status_code)