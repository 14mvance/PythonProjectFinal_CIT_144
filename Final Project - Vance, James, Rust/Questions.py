###########################################################################################################################################
#   Questions and Answers stored as Lists                                                                                                 #
#   chapter1_Questions[0] corresponds with chapter1_Answers[0] and so on                                                                  #
###########################################################################################################################################

### Temporary variables used to store the questions
###  and answers that the user is currently
###   working with
chapterQuestions = [] 
chapterAnswers = []

############################################################################################################################################
chapter1_Questions = ["Python source or script file", "Translates assembly-language into machine language", \
                      "A low-level language that uses descriptive key words", "A binary digit, either 0 or 1", \
                      "A subsystem of a computer that connects all of its components", "The minimum storage unit in a computer", \
                      "A modem that uses a TV line and is generally faster than DSL", "Using or invoking a function", \
                      "The computer's brain", "A tool used to help programmers communicate and understand a program", \
                      "Translates entire source code into machine code, and then executes the machine code", \
                      "The text entry and display device of a computer", "The amount of space between pixels, measured in millimeters", \
                      "Connection that uses a phone line, but can transfer data 20 times faster than dial-up modems", \
                      "Set of rules that govern how a computer translates characters, numbers, and symbols", \
                      "A tool that performs actions (must be invoked)", "The visible, physical elements of a computer", \
                      "English-like languages that are easy to learn and use", "Integrated Development Environment for Python", \
                      "Whitespace to the left of Python statements", "Typing a statement at the prompt and executing it", \
                      "Reads one statement from source code, translates it to machine code and executes it right away", \
                      "Using or calling a function", "Comment preceded by a # symbol" , \
                      "Error that occurs when a program does not perform the way it is intended to", \
                      "Close in nature to machine language and is machine dependent", \
                      "A computer's native language, a set of built-in primitive instructions", \
                      "Consists of an ordered sequence of bytes for storing programs as data", \
                      "Communication devices used to network computers",  \
                      "A circuit case that connects all of the parts of a computer", "Device that connects to a LAN", \
                      "The most important program on a computer (manages and controls a computer's activities", \
                      "Tiny dots that form the image on a screen", \
                      "Software that contains instructions to tell your computer what actions to take", \
                      "Errors that occur while a program is running and cause abnormal termination", \
                      "The number of pixels in horizontal and vertical dimensions of a display device",\
                      "Running a Python program from a script file", \
                      "The invisible instructions that control the hardware and make it perform specific tasks", \
                      "A program written in a high-level language", "Instructions in a high-level programming language", \
                      "Place where programs and data are permanently stored", "Result from errors in code construction", \
                      "Rules governing the structure of a program"]

chapter1_Answers =  [".py file", "assembler", "assembly language", \
                     "bit", "bus", "byte", "cable modem", "calling a function", \
                     "central processing unit (CPU)", "comment", "compiler", \
                     "console", "dot pitch", "DSL (digital subscriber line", \
                     "encoding scheme", "function", "hardware", "high-level language", \
                     "IDLE", "indentation", \
                     "interactive mode", "interpreter", "invoking a function", "line comment", \
                     "logic error", "low-level language", "machine language", "memory", \
                     "modem", "motherboard", "network interface card (NIC)", \
                     "operating system (OS)", "pixel", "program", "runtime errors", \
                     "screen resolution", "script mode", "software", \
                     "source code or source program", "statement", \
                     "storage device", "syntax errors", "syntax rules"]                                                                  
###########################################################################################################################################
chapter2_Questions = ["Describes how a problem is solved by listing the actions that need to be taken and the order of their execution", \
                      "A single Equal sign (=)", "Adding two operators together to make a compound assignment", \
                      "Naming style where first word is lowercase and the first letter of each subsequent letter is capitalized", \
                      "Combining multiple operators in a single assignment", "Integers, Floats, Strings, Lists...", \
                      "A computation involving values, variables, and operators", "Real numbers", \
                      "A sequence of characters that consists of letters, digits, and underscores", \
                      "Approach to programming where steps are developed and tested one at a time", \
                      "Input, Process, Output", "Reserved words that have special meaning in Python", \
                      "Symbol that can be placed at the end of a line to tell the interpreter that the statement continues on the next line",\
                      "A constant value that appears directly in a program", "The values operated by an operator", \
                      "Numeric data types that include the standard arithmetic operators", "Natural language mixed with some programming code", \
                      "Words that have special meaning in Python, such as import", "The part of a program where a variable can be referenced", \
                      "Evaluating all the expressions on the right and assigning them to the corresponding variable on the left at the same time", \
                      "Seeks to analyze the data flow and to identify the system's input and output.", \
                      "The design process for obtaining the output from the input", "Converting operands of different types", \
                      "A name that references a value stored in the computer's memory"]

chapter2_Answers = ["algorithm", "assignment operator", "augmented assignment", "camelCase", "compund assignment", \
                    "data type", "expression", "floating-point numbers", "identifiers", "incremental development and testing", \
                    "IPO", "keyword", "line continuation symbol", "literal", "operands", "operators", \
                    "pseudocode", "reserved word", "scope of a variable", "simultaneous assignment", "system analysis", \
                    "system design", "type conversion", "variable"]

chapter3_Questions = ["Python provides the mathematical functions in the _____ module.", \
                      "A _____ is a sequence of characters.", \
                      "_____ are used to store data in a program.", \
                      "Python does not have a _____ _____ for characters.", \
                      "An _____ _____ is a special syntax that begins with the character followed by a letter of a combination of digits to represent special characters.", \
                      "All data including numbers and strings are _____ in Python.", \
                      "You can invoke _____ to perform operations on the objects.", \
                      "You can use the _____ function to format a number or a string and return the result as a string.", \
                      "The _____ for the objects are called methods in Python.", \
                      "The _____ function can be used to convert a number into a string."]

chapter3_Answers = ["math", "string", "variables", "data type", "escape sequence", "objects", "methods", "format", "functions", "str"]

chapter4_Questions = ["A _____ type variable can store a True or False value.", \
                      "The _____ operators (<, <=, ==, !=, >, >=), which work with numbers and characters, yield a Boolean value.", \
                      "The Boolean operators and, or, and _____ operate with Boolean values and variables.", \
                      "There are several types of _____: if statements, if-else statements, nested if-elif-else statements, and conditional expressions", \
                      "The various _____ statements all make control decisions based on a Boolean expression.", \
                      "The _____ in arithmetic expressions are evaluated in the order determined by the rules of parentheses, operator precedence, and operator associativity.", \
                      "_____ can be used to force the order of evaluation to occur in any sequence.", \
                      "Operators with higher precedence are evaluated earlier. For operators of the same precedence,", \
                      "Their _____ determines the order of evaluation.", \
                      "Operators with a higher precedence are evaluated _____."]

chapter4_Answers = ["boolean", "relational", "not", "selection statements", "if", "operators", "parentheses", "associativity", "parentheses", "earlier"]

chapter5_Questions = ["There are tow types of repetition statements: the while loop and the _____ loop.", \
                      "The part of the loop that contains the statements to be repeated is called the loop _____.", \
                      "A one-time execution of a loop body is referred to as an _____ of the loop.", \
                      "An _____ loop is a loop statement that executes infinitely.", \
                      "In designing loops, you need to consider both the loop-control structure and the loop _____.", \
                      "The _____ loop checks the loop-continuation-condition first.  If the condition is true, the loop body is executed.", \
                      "A _____ value is a special value that signifies the end of the input.", \
                      "The for loop is a _____-controlled loop and is used to execute a loop body a predictable number of times.", \
                      "Two keywords, _____ and continue, can be used in a loop.", \
                      "The break keyword immediately ends the _____ loop, which contains the break."]

chapter5_Answers = ["for", "body", "iteration", "infinite", "body", \
                    "while", "sentinel", "count", "break", "innermost"]

chapter6_Questions = ["Making programs modular and reusable is one of the central goals in software engineering.  _____ can help to achieve this goal.", \
                      "A function _____ begins with the def keyword followed by function's name and parameters, and ends with a colon.", \
                      "Parameters are _____; that is, a function does not have to contain any parameters.", \
                      "A function is called a _____ or None function if it does not return a value.", \
                      "A _____ statement can also be used in a void function for terminating the function and returning to the function's caller.", \
                      "The _____ that are passed to a function should have the same number, type, and order as the parameters in the function header.", \
                      "A function's arguements can be passed as positional arguements or _____ arguements.", \
                      "_____ variables are created outside all functions and are accessible to all functions in their scope.", \
                      "Function _____ is achieved by separating the use of a function from its implementation.", \
                      "Function abstraction _____ programs in a neat, hierarchical manner."]

chapter6_Answers = ["functions", "header", "optional", "void", "return", \
                    "arguements", "keyword", "global", "abstraction", "modularizes"]
                    
chapter7_Questions = ["A _____ is a template, a blueprint, a contract, and a data type for objects.", \
                      "A class defines the properties of objects and provides an _____ for initializing objects and methods for manipulationg them.", \
                      "The intitializer is always named _____.", \
                      "The first parameter in each method including the initializer in the class refers to the object that calls the method. By convention, this parameter is named _____.", \
                      "An object is an _____ of a class.", \
                      "A _____ is used to create an object", \
                      "A _____ is used to access members of an object through its reference variable.", \
                      "An _____ variable or method belongs to an instance of a class.", \
                      "_____ fields in classes should be hidden to prevent data tampering and to make classes easy to maintain.", \
                      "You can provide a _____ method or a set method to enable clients to see or modify the data."]

chapter7_Answers = ["class", "initializer", "__init__", "self", "instance", \
                    "constructor", "dot operator", "instance", "data", "get"]

chapter8_Questions = ["A string is _____.  Its contents cannot be changed.", \
                      "You can use the _____ function to return the length of a string.", \
                      "You can use the _____ operator to reference an individual character in a string.", \
                      "You can use the _____ operator to duplicate strings.", \
                      "You can use the _____ operator to get a substring.", \
                      "The _____ operators can be used to compare two strings.", \
                      "You can use a _____ loop to iterate all characters in a string.", \
                      "You can define special methods for overloading the _____.", \
                      "Strings are objects of the _____ class.", \
                      "The _____ function returns a string frp, the keyboard."]

chapter8_Answers = ["immutable", "len", "index", "repetition", "slicing", \
                    "comparision", "for", "operators", "str", "input"]

chapter9_Questions = ["To place a widget in a container, you have to specify its _____ manager.", \
                     "The _____ manager places widgets side by side or on top of eachother.", \
                     "The _____ manager places widgets in grids.", \
                     "The _____ manager places the widgets in absolute locations.", \
                     "Many widgets have the command option for binding an event with a _____ function.  When an event occurs, this function is invoked.", \
                     "The _____ widget can be used to draw lines, rectagles, ovals, arcs, and polygons, and to display images and text strings.", \
                     "You can use the _____ class to create menu bars, menu items, and pop-up menus.", \
                     "You can bind mouse and key events to a widget with a _____ function.", \
                     "You can use _____ to develop animations.", \
                     "You can use standard dialog boxes to display _____ and receive input"]

chapter9_Answers = ["geometry", "pack", "grid", "place", "callback", \
                    "canvas", "menu", "callback", "canvases", "messages"]

chapter10_Questions = ["You can use the _____ function in the random module to shuffle the elements in a list.", \
                       "You can use the _____ operators to compare the elements of two lists.", \
                       "You can use a _____ loop to travers all elements in a list.", \
                       "A list object is _____.  You can use the methods append, extend, insert, pop, and remove to add and remove elements to and from a list.", \
                       "You can use the _____ method to get the index of an element in a list.", \
                       "You can use the _____ method to sort elements in a list.", \
                       "You can use the _____ method to sort elements in a list.", \
                       "You can use the _____ method to split a string into a list.", \
                       "When a function is invoked with a list arguement, the _____ of the list is passed to the function.", \
                       "The _____-sort algorithm sorts a list of values by repeatedly inserting a new element into a sorted sublist until the whole list is sorted."]
                          
chapter10_Answers = ["shuffle", "comparison", "for", "mutable", "index", \
                     "sort", "reverse", "split","reference", "insertion"]


chapter11_Questions = ["A two dimensional list can be used to store two-dimensional data such as a table and a _____.", \
                       "A two-dimenional list is a list.  Each of its elements is a _____.", \
                       "An element in a two-dimensional list can be accessed using the following syntax: _____[rowIndex][columnIndex].", \
                       "You can use lists of list to form _____ lists.", \
                       "A two-dimensional list is a list that contains other lists as its _____.", \
                       "A _____ is a list in which each element is another list", \
                       "A list that is contained within another list is considered a _____ list.", \
                       "You can apply the _____ method to sort a two-dimensional list.", \
                       "A value in a two-dimensional list can be accessed through a _____ and clolumn index.", \
                       "When passing a two-dimensional list to a function, the list's _____ is passed to the function."]

chapter11_Answers = ["matrix", "list", "listName", "multidimensional", "elements", \
                    "multidimensional", "nested", "sort", "row" "reference"]

chapter12_Questions = ["A new class can be derived from an existing class.  This is known as class _____.", \
                       "A new class that is derived from an existing class is called a _____, child class, or extended class.", \
                       "The existing class that a new class is derived from is called a _____, parent class, or base class", \
                       "To override a method, the method must be defined in the subclass using the same _____ as its superclass.", \
                       "The object class is the _____ class for all Python classes.", \
                       "_____ means that an object of a subclass can be passed to a parameter of a superclass type.", \
                       "The _____ function can be used to determine whether an object is an instance of a class.", \
                       "The common _____ among classes are association, aggregation, composition, and inheritance.", \
                       "_____ enables you to define a general class and later extend it to a more specialized class.", \
                       "A method may be implemented in serveral classes along the _____ chain."]
                      
chapter12_Answers = ["inheritance", "subclass", "none of these", "header", "root", \
                     "Polymorphism", "isinstance", "relationships", "inheritance", "inheritance"]

chapter13_Questions = ["You can use _____ objects to read/write data from/to files.", \
                       "You can open a file to create a file object with the mode _____ for reading.", \
                       "You can open a file to create a file object with the mode _____ for writing.", \
                       "You can open a file to create a file object with the mode _____ for appending.", \
                       "You can use the os.path._____(f) function to check if a file exists.", \
                       "You can use the read(), readline(), and _____() methods to read data from a file.", \
                       "You can use the _____(s) method to write a string to a file.", \
                       "You should _____ the file after the file is processed to ensure that he data is saved properly.", \
                       "You can use _____ handling to catch and handle runtime errors.", \
                       "You can use the Python _____ module to store objects in a file."]

chapter13_Answers = ["file", "r", "w", "a", "isfile", \
                     "readlines", "write", "close", "exception","pickle"]


chapter14_Questions = ["A tuple is a _____ list.", \
                      "You cannot add, delete, or replace elements in a _____.", \
                      "Since a tuple is a _____, the common operations for sequences can be used for tuples.", \
                      "A tuple is _____, if all its elements are immutable.", \
                      "_____ are like lists in that you use them for storing a collection of elements.", \
                      "You can add an element to a set using the ______ method.", \
                      "You can remove an element from the set using the _____ method.", \
                      "You can use a ____ loop to traverse the elements in a set.", \
                      "A _____ can be used to store key/value pairs.", \
                      "You can use the _____ function to return he number of items in a dictionary."]

chapter14_Answers = ["fixed", "tuple", "sequence", "immutable", "sets", \
                     "add","remove", "for", "dictionary" "len"]

chapter15_Questions = ["A _____ function is one that directly or indirectly invokes itself.", \
                      "For a recursive function to terminate, there must be one or more _____ cases.", \
                      "Recursion is an alternative form of program _____.", \
                      "Sometimes the original function needs to be modified o receive additional parameters in order to be invoked recursively.  A recursive _____ function can be defined for this purpose.", \
                      "A recursive function is said to be tail recursive if there are no pending operations to be performed on return from a recursive _____.", \
                      "_____ recursion is efficient.", \
                      "Recursion can be used to specify simple, clear solutions for inherently recursive problems that would otherwise be _____ to solve.", \
                      "Recursion bears substantial _____.", \
                      "Recursion is ideal for displaying fractals, because fractals are _____ recursive.", \
                      "A recursive functio is one that _____ itself."]

chapter15_Answers = ["recursive", "base", "control", "helper", "call", \
                     "tail", "difficult", "overhead", "inherently", "invokes"]

















