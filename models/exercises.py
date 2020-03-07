from pprint import pformat


class Exercises:
    def __init__(self, mongo_connector):
        self.mongo_connector = mongo_connector
        self.exercises_db = self.mongo_connector.exercises

        self.exercises = [
            {'name': 'knee pushups', 'points': 1},
            {'name': 'pushups', 'points': 2},
            {'name': 'raised pushups', 'points': 3},
        ]

    def insert_exercises(self):
        """Inserts exercises into the MongoDB database, should only be done once"""
        print("Dropping collection")
        self.exercises_db.exercises.drop()
        print("Adding Exercises")
        self.exercises_db.exercises.insert_many(self.exercises)

    def get_exercises(self):
        response = [x for x in self.exercises_db.exercises.find({}, {"_id": 0})]
        return pformat(response)

    def query_exercises(self, search_term):
        print(search_term)

        if search_term.isnumeric():
            query = {'points': int(search_term)}
            response = [x for x in self.exercises_db.exercises.find(query, {"_id": 0, "name": 1})]

        else:
            search_term = search_term.lower()
            query = {'name': {'$regex': f'^.*{search_term}.*$'}}
            response = [x for x in self.exercises_db.exercises.find(query, {"_id": 0})]

        return pformat(response)



