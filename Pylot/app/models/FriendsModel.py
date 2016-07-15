""" 
    Sample Model File

    A Model should be in charge of communicating with the Database. 
    Define specific model method that query the database for information.
    Then call upon these model method in your controller.

    Create a model using this template.
"""
from system.core.model import Model

class FriendsModel(Model):
    def __init__(self):
        super(FriendsModel, self).__init__()

    def get_all_friends(self):
        query = "SELECT * FROM friends"
        return self.db.query_db(query)

    def show(self, id):
        query = "SELECT * FROM friends where id = :id"
        data = {
            'id': id
        }
        return self.db.query_db(query, data)

    def update(self, id, a):
        query = "UPDATE friends SET first_name=:first_name, last_name=:last_name, email=:email, updated_at=NOW() WHERE id=:id"
        values = {'first_name': a['first_name'], 'last_name': a['last_name'], 'email': a['email'], 'id': id}
        return self.db.query_db(query, values)

    def delete(self, id):
        query = "DELETE FROM friends WHERE id=:id"
        values = {"id": id}
        return self.db.query_db(query, values)

    def create(self, b):
        query = "INSERT INTO friends (first_name, last_name, email, created_at) VALUES (:first_name, :last_name, :email, NOW())"
        values = {
            "first_name": b['first_name'],
            "last_name": b['last_name'],
            "email": b['email']
        }
        return self.db.query_db(query, values)


    """
    Below is an example of a model method that queries the database for all users in a fictitious application
    
    Every model has access to the "self.db.query_db" method which allows you to interact with the database

    def get_users(self):
        query = "SELECT * from users"
        return self.db.query_db(query)

    def get_user(self):
        query = "SELECT * from users where id = :id"
        data = {'id': 1}
        return self.db.get_one(query, data)

    def add_message(self):
        sql = "INSERT into messages (message, created_at, users_id) values(:message, NOW(), :users_id)"
        data = {'message': 'awesome bro', 'users_id': 1}
        self.db.query_db(sql, data)
        return True
    
    def grab_messages(self):
        query = "SELECT * from messages where users_id = :user_id"
        data = {'user_id':1}
        return self.db.query_db(query, data)

    """