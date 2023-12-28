from datetime import datetime
# from model.person import Person


class customResponse:
    status_code = 0
    message = ""
    url = ""
    timestamp = datetime.now()
    list = []
    person = dict()


    def __init__(self, status_code, url, message):
        self.status_code = status_code
        self.message = message
        self.url = url
        self.person
        # self.list = personList
        # self.person = person
        # self.url
        # self.message
        # self.list
        # self.status_code
    
    # def showDetails(self):
    #     print(self.status_code, self.message, self.url, self.list, self.person, self.timestamp)