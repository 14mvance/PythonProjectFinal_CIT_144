from tinydb import TinyDB, where  ## imports tinydb so information can be stored to a ..json file to remember previous users info etc
from tinydb.queries import Query

db = TinyDB('db.json')
table = db.table('students')

class Student:

    def __init__(self, name, id):
        self.name = name
        self.id = id

    def setName(self, name):  ##defining the method that sets the name for each user
    		self.name = name

    def setId(self, id): ## defining the method that sets the id for each user
    		self.id = id

    def getName(self): ## defining the method that gets the name for each user
    		return self.name

    def getId(self): ## defining the method that gets the name for each user
    		return self.id

    def saveToDB(self):  ## defining the method that saves the user's name and id to the .json DB file
        data = {
            'name': self.name,
            'student_id': self.id
        }
        table = db.table('students')
        table.insert(data)

    def saveScore(self, chapter, score):   ### saves highest score for the chapter test that is taken
        student = Query() ## tinyDB construct query
        if len(db.search(student.student_id == self.id)) == 0: ##searches database for the student by student id
            self.saveToDB()


        table.update({"scores" : [{"chapter" : chapter, "score" : score}]}, where('student_id') == self.id)

    def showAllScores(self):
        student = table.get(where("student_id") == self.id)
        scores = student["scores"]

        for score in scores:
            print("chapter", score["chapter"], ":", score["score"])
