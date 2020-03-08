from pprint import pformat


class Users:
    def __init__(self, database):
        self.database = database
        self.users_collection = self.database.users

    def get_users(self, user):
        """Returns the current user's object from the users collection"""
        response = [x for x in self.users_collection.find({'username': user.display_name}, {"_id": 0})]
        return pformat(response)

    def insert_user(self, member_data):
        user = {
            'username': member_data.name,
            'discriminator': member_data.discriminator,
            'classes': {
                'fighter': 0,
                'rogue': 0,
                'wizard': 0,
            }
        }

        if not [x for x in self.users_collection.find({'username': member_data.name})]:
            self.users_collection.insert_one(user)
            print(f"User {member_data.name} created.")
