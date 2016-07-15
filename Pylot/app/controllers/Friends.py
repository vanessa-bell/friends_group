"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *

class Friends(Controller):
    def __init__(self, action):
        super(Friends, self).__init__(action)
        """
        This is an example of loading a model.
        Every controller has access to the load_model method.
        """
        self.load_model('FriendsModel')
        self.db = self._app.db

        """
        
        This is an example of a controller method that will load a view for the client 

        """
   
    def index(self):
        all_friends = self.models['FriendsModel'].get_all_friends()
        return self.load_view('index.html', all_friends=all_friends)

    def create(self, method='POST'):
        b = request.form
        friend = self.models['FriendsModel'].create(b)
        return redirect('/')

    def edit(self, id):
        friend = self.models['FriendsModel'].show(id)
        return self.load_view('edit.html', friend = friend[0])

    def delete(self, id, method='POST'):
        friend = self.models['FriendsModel'].delete(id)
        return redirect ('/')

    def show(self, id): 
        friend = self.models['FriendsModel'].show(id)
        return self.load_view('profile.html', friend = friend[0])

    def update(self, id, methods='POST'):
        a = request.form
        friend = self.models['FriendsModel'].update(id,a)
        return redirect('/')

    def confirm(self, id):
        friend = self.models['FriendsModel'].show(id)
        return self.load_view('confirm.html', friend = friend[0])

