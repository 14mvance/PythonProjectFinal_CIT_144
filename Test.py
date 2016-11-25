from tinydb import TinyDB, where  ## imports tinydb so information can be stored to a ..json file to remember previous users info etc
from tinydb.queries import Query

db = TinyDB('db.json')
table = db.table('tests')  ##sets the tinyDb table to tests


class Test:
    def __init__(self, chapter):
        self.chapter = chapter
        test = table.get(where("chapter") == chapter)  ##queries for the tests by chapter
        self.questions = test["questions"]  ## gets that test's questions

    def run(self):
        correctAnswers = 0;
        for question in self.questions:
            userAnswer = input(question["question"]).lower()  ## asks the question to user and gets the user's answer

            if (userAnswer == question["answer"]):  ## compares the user's answer with the correct answer
                print("correct")
                correctAnswers += 1  ## raises the correct answer for the user by 1 when correct
            else:
                print("incorrect. The correct answer was ", question["answer"])  ## tells the correct answer

        score = (correctAnswers / len(self.questions)) * 100
        print("Test complete. You scored ", score)
        return score
