from model.person import Person

person = Person()

class User():
    def check_presence(self, data):
        username = data.get('username')
        password = data.get('password')

        user = Person.query.filter_by(email=username, password=password).first()
        
        if user:
            return user.id
        else:
            "Unknown User"