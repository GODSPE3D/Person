from flask import jsonify

class Message():
    def badReq(self):
        return jsonify({
            'error': 'Bad Request',
            'message': 'One or more fields are empty'
        }), 400

    def badLetter(self):
        return jsonify({
            'error': 'Bad Request',
            'message': 'Name and email must contain a minimum of 4 letter'
        }), 400

    def duplicate(self, data):
        return jsonify({
            'error': 'Duplicate Data',
            'similar': "Same " + data
        }), 400

    def success(self):
        return {
            'success': 'Data deleted successfully'
        }

    def failed(self):
        return {
            'failed': "Data doesn't exist"
        }