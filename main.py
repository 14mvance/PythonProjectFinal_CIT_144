from Student import Student
from Test import Test

def showScores():
    student.showAllScores()

def takeTest():
    chapter = input("what chapter would you like to test on")
    test = Test(chapter)
    score = test.run()
    student.saveScore(chapter, score)

name = input("What is your name")
id = input("what is your id")
student = Student(name, id)

run = True
while run:
    choice = input("1: take test, 2: show scores, 3: quit")
    if choice == "1":
        takeTest()
    elif choice == "2":
        showScores()
    elif choice == "3":
        print("Thanks for testing!")
        run = False
        break
    else:
        print("invalid choice")














def saveTestToDB(self):
    data = [{
       "chapter": "1",
       "questions": [
           {
               "question": "A _____ is an electronic device that stores and processes data.",
               "answer": "computer"
           },
           {
               "question": "_____ is the physical aspect of the computer that can be touched.",
               "answer": "hardware"
           },
           {
               "question": "_____ is the writing of instructions (i.e., code) for computers to perform",
               "answer": "computer programming"
           },
           {
               "question": "The _____ is a computer's brain.  It retrieves instructions from memory and executes them.",
               "answer": "CPU"
           },
           {
               "question": "A _____ is a binary digit 0 or 1.",
               "answer": "bit"
           },
           {
               "question": "A _____ is a sequence of 8 bits.",
               "answer": "byte"
           },
           {
               "question": "A _____ is an ordered sequence of bytes.",
               "answer": "memory unit"
           },
           {
               "question": "The _____ is a set of primitive instructions built into every computer.",
               "answer": "machine language"
           },
           {
               "question": "_____ is a low-level programing language in which a mnemonic is used to represent each machine-language instruction.",
               "answer": "assembly language"
           },
           {
               "question": "A _____ is a software program that translates the source program into a machine-language program.",
               "answer": "compiler"
           }
       ]
    },
    {
        "chapter": "2",
        "questions": [
            {
                "question": "You can get input using the input function and convert a string into a numberica value using the _____ function",
                "answer": "eval"
            },
            {
                "question": "_____ are the name used for elements in a program",
                "answer": "identifiers"
            },
            {
                "question": "_____ are used to store data in a program",
                "answer": "variables"
            },
            {
                "question": "The _____ sign is used as the assignment operator",
                "answer": "equals"
            },
            {
                "question": "The _____ operators in a Python expression are applied the same way as in an arithmetic expression",
                "answer": "numeric"
            },
            {
                "question": "Python provides _____ that perform numeric operations: + (addition), - (subtraction), * (multiplication), / (division), // (integer division), % (remainder), and ** (exponent).",
                "answer": "assignment operators"
            },
            {
                "question": "There are two types of number data in Python: _____ and real numbers.",
                "answer": "integers"
            },
            {
                "question": "You can convert a _____ to an int using the int(value) function",
                "answer": "float"
            },
            {
                "question": "_____ seeks to analyze the data flow and to identify the system's input and output",
                "answer": "system analysis"
            },
            {
                "question": "_____ is the stage when programmers develop a process for obtaining the output from the input",
                "answer": "system design"
            }
        ]
    },
    {
        "chapter": "3",
        "questions": [
            {
                "question": "You can get input using the input function and convert a string into a numberica value using the _____ function",
                "answer": "eval"
            },
            {
                "question": "_____ are the name used for elements in a program",
                "answer": "identifiers"
            },
            {
                "question": "_____ are used to store data in a program",
                "answer": "variables"
            },
            {
                "question": "The _____ sign is used as the assignment operator",
                "answer": "equals"
            },
            {
                "question": "The _____ operators in a Python expression are applied the same way as in an arithmetic expression",
                "answer": "numeric"
            },
            {
                "question": "Python provides _____ that perform numeric operations: + (addition), - (subtraction), * (multiplication), / (division), // (integer division), % (remainder), and ** (exponent).",
                "answer": "assignment operators"
            },
            {
                "question": "There are two types of number data in Python: _____ and real numbers.",
                "answer": "integers"
            },
            {
                "question": "You can convert a _____ to an int using the int(value) function",
                "answer": "float"
            },
            {
                "question": "_____ seeks to analyze the data flow and to identify the system's input and output",
                "answer": "system analysis"
            },
            {
                "question": "_____ is the stage when programmers develop a process for obtaining the output from the input",
                "answer": "system design"
            }
        ]
    },
    {
        "chapter": "4",
        "questions": [
            {
                "question": "A _____ type variable can store a True or False value.",
                "answer": "boolean"
            },
            {
                "question": "The _____ operators (<, <=, ==, !=, >, >=), which work with numbers and characters, yield a Boolean value.",
                "answer": "relational"
            },
            {
                "question": "The Boolean operators and, or, and _____ operate with Boolean values and variables.",
                "answer": "not"
            },
            {
                "question": "There are several types of _____: if statements, if-else statements, nested if-elif-else statements, and conditional expressions",
                "answer": "selection statements"
            },
            {
                "question": "The various _____ statements all make control decisions based on a Boolean expression.  Based on the True or False evaluation of the expression, these statements take one of two possible courses.",
                "answer": "if"
            },
            {
                "question": "The _____ in arithmetic expressions are evaluated in the order determined by the rules of parentheses, operator precedence, and operator associativity.",
                "answer": "operators"
            },
            {
                "question": "_____ can be used to force the order of evaluation to occur in any sequence.",
                "answer": "parentheses"
            },
            {
                "question": "Operators with higher precedence are evaluated earlier. For operators of the same precedence, their _____ determines the order of evaluation.",
                "answer": "associativity"
            },
            {
                "question": "This needs to be a question from chapter 4",
                "answer": "chapter 4 question answer"
            },
            {
                "question": "This needs to be another question from chapter 4",
                "answer": "chapter 4 question answer"
            }
        ]
    }]
    table = db.table('tests')
    table.insert(data)
