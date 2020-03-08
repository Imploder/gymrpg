from pprint import pformat


class Exercises:
    """Handles the !exercises command"""
    def __init__(self, database):
        """Sets up the connection to MongoDB"""
        self.database = database
        self.exercises_collection = self.database.exercises

        # Keep lowercase names
        self.exercises = [
            {'name': 'knee pushups', 'points': 1},
            {'name': 'pushups', 'points': 2},
            {'name': 'raised pushups', 'points': 3},
        ]

    def insert_exercises(self):
        """Inserts exercises into the MongoDB database, should only be done to update"""
        print("Dropping collection")
        self.exercises_collection.drop()
        print("Adding Exercises")
        self.exercises_collection.insert_many(self.exercises)

    def get_exercises(self):
        """Returns all exercises from the exercises collection"""
        response = [x for x in self.exercises_collection.find({}, {"_id": 0})]
        return pformat(response)

    def query_exercises(self, search_term):
        """
        Returns the exercises with the given points, or that contains the given name
        :param search_term: The search term to use when querying the MongoDB collection
        """
        if search_term.isnumeric():
            query = {'points': int(search_term)}
            response = [x for x in self.exercises_collection.find(query, {"_id": 0, "name": 1})]

        else:
            search_term = search_term.lower()
            query = {'name': {'$regex': f'^.*{search_term}.*$'}}
            response = [x for x in self.exercises_collection.find(query, {"_id": 0})]

        return pformat(response)



