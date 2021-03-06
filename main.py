## if you run into trouble, clear data in the db.json file
from tinydb import TinyDB, where
from tinydb.queries import Query

from Student import Student
from Test import Test

def showScores():
    student.showAllScores()

def takeTest():
    chapter = input("what chapter would you like to test on")
    test = Test(chapter)
    score = test.run()
    student.saveScore(chapter, score)

def saveTestToDB():
    db = TinyDB('db.json')
    table = db.table('tests')
    tests = table.all()
    if len(tests) <= 0:
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
                    "question": "You can get input using the input function and convert a string into a numerical value using the _____ function.",
                    "answer": "eval"
                },
                {
                    "question": "_____ are the name used for elements in a program.",
                    "answer": "identifiers"
                },
                {
                    "question": "_____ are used to store data in a program.",
                    "answer": "variables"
                },
                {
                    "question": "The _____ sign is used as the assignment operator.",
                    "answer": "equals"
                },
                {
                    "question": "The _____ operators in a Python expression are applied the same way as in an arithmetic expression.",
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
                    "question": "You can convert a _____ to an int using the int(value) function.",
                    "answer": "float"
                },
                {
                    "question": "_____ _____ seeks to analyze the data flow and to identify the system's input and output.",
                    "answer": "system analysis"
                },
                {
                    "question": "_____ _____ is the stage when programmers develop a process for obtaining the output from the input.",
                    "answer": "system design"
                }
            ]
        },
        {
            "chapter": "3",
            "questions": [
                {
                    "question":"Python provides the mathematical functions in the _____ module.",
                    "answer":"math"
                },
                {
                    "question":"A _____ is a sequence of characters.",
                    "answer":"string"
                },
                {
                    "question": "_____ are used to store data in a program.",
                    "answer": "variables"
                },
                {
                    "question":"Python does not have a _____ _____ for characters.",
                    "answer":"data type"
                },
                {
                    "question":"An _____ _____ is a special syntax that begins with the character \ followed by a letter of a combination of digits to represent special characters.",
                    "answer":"escape sequence"
                },
                {
                    "question":"All data including numbers and strings are _____ in Python.",
                    "answer":"objects"
                },
                {
                    "question":"You can invoke _____ to perform operations on the objects.",
                    "answer":"methods"
                },
                {
                    "question":"You can use the _____ function to format a number or a string and return the result as a string.",
                    "answer":"format"
                },
                {
                    "question":"The _____ for the objects are called methods in Python.",
                    "answer":"functions"
                },
                {
                    "question":"The _____ function can be used to convert a number into a string.",
                    "answer":"str"
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
                    "question":"_____ can be used to force the order of evaluation to occur in any sequence.",
                    "answer":"parentheses"
                },
                {
                    "question":"Operators with a higher precedence are evaluated _____.",
                    "answer":"earlier"
                }
            ]
        },
        {
            "chapter": "5",
            "questions": [
                {
                    "question":"There are tow types of repetition statements: the while loop and the _____ loop.",
                    "answer":"for"
                },
                {
                    "question":"The part of the loop that contains the statements to be repeated is called the loop _____.",
                    "answer":"body"
                },
                {
                    "question":"A one-time execution of a loop body is referred to as an _____ of the loop.",
                    "answer":"iteration"
                },
                {
                    "question":"An _____ loop is a loop statement that executes infinitely.",
                    "answer":"infinite"
                },
                {
                    "question":"In designing loops, you need to consider both the loop-control structure and the loop _____.",
                    "answer":"body"
                },
                {
                    "question":"The _____ loop checks the loop-continuation-condition first.  If the condition is true, the loop body is executed.",
                    "answer":"while"
                },
                {
                    "question":"A _____ value is a special value that signifies the end of the input.",
                    "answer":"sentinel"
                },
                {
                    "question":"The for loop is a _____-controlled loop and is used to execute a loop body a predictable number of times.",
                    "answer":"count"
                },
                {
                    "question":"Two keywords, _____ and continue, can be used in a loop.",
                    "answer":"break"
                },
                {
                    "question":"The break keyword immediately ends the _____ loop, which contains the break.",
                    "answer":"innermost"
                }
            ]
        },
        {
             "chapter": "6",
            "questions": [
                {
                    "question":"Making programs modular and reusable is one of the central goals in software engineering.  _____ can help to achieve this goal.",
                    "answer":"functions"
                },
                {
                   "question":"A function _____ begins with the def keyword followed by function's name and parameters, and ends with a colon.",
                    "answer":"header"
                },
                {
                    "question":"Parameters are _____; that is, a function does not have to contain any parameters.",
                    "answer":"optional"
                },
                {
                    "question":"A function is called a _____ or None function if it does not return a value.",
                    "answer":"void"
                },
                {
                    "question":"A _____ statement can also be used in a void function for terminating the function and returning to the function's caller.",
                    "answer":"return"
                },
                {
                    "question":"The _____ that are passed to a function should have the same number, type, and order as the parameters in the function header.",
                    "answer":"arguements"
                },
                {
                    "question":"A function's arguements can be passed as positional arguements or _____ arguements.",
                    "answer":"keyword"
                },
                {
                    "question":"_____ variables are created outside all functions and are accessible to all functions in their scope.",
                    "answer":"global"
                },
                {
                    "question":"Function _____ is achieved by separating the use of a function from its implementation.",
                    "answer":"abstraction"
                },
                {
                    "question":"Function abstraction _____ programs in a neat, hierarchical manner.",
                    "answer":"modularizes"
                }
            ]
        },
        {
             "chapter": "7",
            "questions": [
                {
                    "question":"A _____ is a template, a blueprint, a contract, and a data type for objects.",
                    "answer":"class"
                },
                {
                   "question":"A class defines the properties of objects and provides an _____ for initializing objects and methods for manipulationg them.",
                    "answer":"initializer"
                },
                {
                    "question":"The intitializer is always named _____.",
                    "answer":"__init__"
                },
                {
                    "question":"The first parameter in each method including the initializer in the class refers to the object that calls the method. By convention, this parameter is named _____.",
                    "answer":"self"
                },
                {
                    "question":"An object is an _____ of a class.",
                    "answer":"instance"
                },
                {
                    "question":"A _____ is used to create an object",
                    "answer":"constructor"
                },
                {
                    "question":"A _____ is used to access members of an object through its reference variable.",
                    "answer":"dot operator"
                },
                {
                    "question":"An _____ variable or method belongs to an instance of a class.",
                    "answer":"instance"
                },
                {
                    "question":"_____ fields in classes should be hidden to prevent data tampering and to make classes easy to maintain.",
                    "answer":"data"
                },
                {
                    "question":"You can provide a _____ method or a set method to enable clients to see or modify the data.",
                    "answer":"get"
                }
            ]
        },
        {
             "chapter": "8",
            "questions": [
                {
                    "question":"A string is _____.  Its contents cannot be changed.",
                    "answer":"immutable"
                },
                {
                   "question":"You can use the _____ function to return the length of a string.",
                    "answer":"len"
                },
                {
                    "question":"You can use the _____ operator to reference an individual character in a string.",
                    "answer":"index"
                },
                {
                    "question":"You can use the _____ operator to duplicate strings.",
                    "answer":"repetition"
                },
                {
                    "question":"You can use the _____ operator to get a substring.",
                    "answer":"slicing"
                },
                {
                    "question":"The _____ operators can be used to compare two strings.",
                    "answer":"comparision"
                },
                {
                    "question":"You can use a _____ loop to iterate all characters in a string.",
                    "answer":"for"
                },
                {
                    "question":"You can define special methods for overloading the _____.",
                    "answer":"operators"
                },
                {
                    "question":"Strings are objects of the _____ class.",
                    "answer":"str"
                },
                {
                    "question":"The _____ function returns a string frp, the keyboard.",
                    "answer":"input"
                }
            ]
        },
        {
             "chapter": "9",
            "questions": [
                {
                    "question":"To place a widget in a container, you have to specify its _____ manager.",
                    "answer":"geometry"
                },
                {
                   "question":"The _____ manager places widgets side by side or on top of eachother.",
                    "answer":"pack"
                },
                {
                    "question":"The _____ manager places widgets in grids.",
                    "answer":"grid"
                },
                {
                    "question":"The _____ manager places the widgets in absolute locations.",
                    "answer":"place"
                },
                {
                    "question":"Many widgets have the command option for binding an event with a _____ function.  When an event occurs, this function is invoked.",
                    "answer":"callback"
                },
                {
                    "question":"The _____ widget can be used to draw lines, rectagles, ovals, arcs, and polygons, and to display images and text strings.",
                    "answer":"canvas"
                },
                {
                    "question":"You can use the _____ class to create menu bars, menu items, and pop-up menus.",
                    "answer":"menu"
                },
                {
                    "question":"You can bind mouse and key events to a widget with a _____ function.",
                    "answer":"callback"
                },
                {
                    "question":"You can use _____ to develop animations.",
                    "answer":"canvases"
                },
                {
                    "question":"You can use standard dialog boxes to display _____ and receive input",
                    "answer":"messages"
                }
            ]
        },
        {
             "chapter": "10",
            "questions": [
                {
                    "question":"You can use the _____ function in the random module to shuffle the elements in a list.",
                    "answer":"shuffle"
                },
                {
                   "question":"You can use the _____ operators to compare the elements of two lists.",
                    "answer":"comparison"
                },
                {
                    "question":"You can use a _____ loop to travers all elements in a list.",
                    "answer":"for"
                },
                {
                    "question":"A list object is _____.  You can use the methods append, extend, insert, pop, and remove to add and remove elements to and from a list.",
                    "answer":"mutable"
                },
                {
                    "question":"You can use the _____ method to get the index of an element in a list.",
                    "answer":"index"
                },
                {
                    "question":"You can use the _____ method to sort elements in a list.",
                    "answer":"sort"
                },
                {
                    "question":"You can use the _____ method to reverse elements in a list.",
                    "answer":"reverse"
                },
                {
                    "question":"You can use the _____ method to split a string into a list.",
                    "answer":"split"
                },
                {
                    "question":"When a function is invoked with a list arguement, the _____ of the list is passed to the function.",
                    "answer":"reference"
                },
                {
                    "question":"The _____-sort algorithm sorts a list of values by repeatedly inserting a new element into a sorted sublist until the whole list is sorted.",
                    "answer":"insertion"
                }
            ]
        },
        {
             "chapter": "11",
            "questions": [
                {
                    "question":"A two dimensional list can be used to store two-dimensional data such as a table and a _____.",
                    "answer":"matrix"
                },
                {
                   "question":"A two-dimenional list is a list.  Each of its elements is a _____.",
                    "answer":"list"
                },
                {
                    "question":"An element in a two-dimensional list can be accessed using the following syntax: _____[rowIndex][columnIndex].",
                    "answer":"listName"
                },
                {
                    "question":"You can use lists of list to form _____ lists.",
                    "answer":"multidimensional"
                },
                {
                    "question":"A two-dimensional list is a list that contains other lists as its _____.",
                    "answer":"elements"
                },
                {
                    "question":"A _____ is a list in which each element is another list",
                    "answer":"multidimensional"
                },
                {
                    "question":"A list that is contained within another list is considered a _____ list.",
                    "answer":"nested"
                },
                {
                    "question":"You can apply the _____ method to sort a two-dimensional list.",
                    "answer":"sort"
                },
                {
                    "question":"A value in a two-dimensional list can be accessed through a _____ and clolumn index.",
                    "answer":"row"
                },
                {
                    "question":"When passing a two-dimensional list to a function, the list's _____ is passed to the function.",
                    "answer":"reference"
                }
            ]
        },
        {
             "chapter": "12",
            "questions": [
                {
                    "question":"A new class can be derived from an existing class.  This is known as class _____.",
                    "answer":"inheritance"
                },
                {
                   "question":"A new class that is derived from an existing class is called a _____, child class, or extended class.",
                    "answer":"subclass"
                },
                {
                    "question":"The existing class that a new class is derived from is called a _____, parent class, or base class",
                    "answer":""
                },
                {
                    "question":"To override a method, the method must be defined in the subclass using the same _____ as its superclass.",
                    "answer":"header"
                },
                {
                    "question":"The object class is the _____ class for all Python classes.",
                    "answer":"root"
                },
                {
                    "question":"_____ means that an object of a subclass can be passed to a parameter of a superclass type.",
                    "answer":"Polymorphism"
                },
                {
                    "question":"The _____ function can be used to determine whether an object is an instance of a class.",
                    "answer":"isinstance"
                },
                {
                    "question":"The common _____ among classes are association, aggregation, composition, and inheritance.",
                    "answer":"relationships"
                },
                {
                    "question":"_____ enables you to define a general class and later extend it to a more specialized class.",
                    "answer":"inheritance"
                },
                {
                    "question":"A method may be implemented in serveral classes along the _____ chain.",
                    "answer":"inheritance"
                }
            ]
        },
        {
             "chapter": "13",
            "questions": [
                {
                    "question":"You can use _____ objects to read/write data from/to files.",
                    "answer":"file"
                },
                {
                   "question":"You can open a file to create a file object with the mode _____ for reading.",
                    "answer":"r"
                },
                {
                    "question":"You can open a file to create a file object with the mode _____ for writing.",
                    "answer":"w"
                },
                {
                    "question":"You can open a file to create a file object with the mode _____ for appending.",
                    "answer":"a"
                },
                {
                    "question":"You can use the os.path._____(f) function to check if a file exists.",
                    "answer":"isfile"
                },
                {
                    "question":"You can use the read(), readline(), and _____() methods to read data from a file.",
                    "answer":"readlines"
                },
                {
                    "question":"You can use the _____(s) method to write a string to a file.",
                    "answer":"write"
                },
                {
                    "question":"You should _____ the file after the file is processed to ensure that he data is saved properly.",
                    "answer":"close"
                },
                {
                    "question":"You can use _____ handling to catch and handle runtime errors.",
                    "answer":"exception"
                },
                {
                    "question":"You can use the Python _____ module to store objects in a file.",
                    "answer":"pickle"
                }
            ]
        },
        {
             "chapter": "14",
            "questions": [
                {
                    "question":"A tuple is a _____ list.",
                    "answer":"fixed"
                },
                {
                   "question":"You cannot add, delete, or replace elements in a _____.",
                    "answer":"tuple"
                },
                {
                    "question":"Since a tuple is a _____, the common operations for sequences can be used for tuples.",
                    "answer":"sequence"
                },
                {
                    "question":"A tuple is _____, if all its elements are immutable.",
                    "answer":"immutable"
                },
                {
                    "question":"_____ are like lists in that you use them for storing a collection of elements.",
                    "answer":"sets"
                },
                {
                    "question":"You can add an element to a set using the ______ method.",
                    "answer":"add"
                },
                {
                    "question":"You can remove an element from the set using the _____ method.",
                    "answer":"remove"
                },
                {
                    "question":"You can use a ____ loop to traverse the elements in a set.",
                    "answer":"for"
                },
                {
                    "question":"A _____ can be used to store key/value pairs.",
                    "answer":"dictionary"
                },
                {
                    "question":"You can use the _____ function to return he number of items in a dictionary.",
                    "answer":"len"
                }
            ]
        },
        {
             "chapter": "15",
            "questions": [
                {
                    "question":"A _____ function is one that directly or indirectly invokes itself.",
                    "answer":"recursive"
                },
                {
                   "question":"For a recursive function to terminate, there must be one or more _____ cases.",
                    "answer":"base"
                },
                {
                    "question":"Recursion is an alternative form of program _____.",
                    "answer":"control"
                },
                {
                    "question":"Sometimes the original function needs to be modified o receive additional parameters in order to be invoked recursively.  A recursive _____ function can be defined for this purpose.",
                    "answer":"helper"
                },
                {
                    "question":"A recursive function is said to be tail recursive if there are no pending operations to be performed on return from a recursive _____.",
                    "answer":"call"
                },
                {
                    "question":"_____ recursion is efficient.",
                    "answer":"tail"
                },
                {
                    "question":"Recursion can be used to specify simple, clear solutions for inherently recursive problems that would otherwise be _____ to solve.",
                    "answer":"difficult"
                },
                {
                    "question":"Recursion bears substantial _____.",
                    "answer":"overhead"
                },
                {
                    "question":"Recursion is ideal for displaying fractals, because fractals are _____ recursive.",
                    "answer":"inherently"
                },
                {
                    "question":"A recursive functio is one that _____ itself.",
                    "answer":"invokes"
                }
            ]
        }]

        for chapter in data:
            table.insert(chapter)

saveTestToDB()  
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















