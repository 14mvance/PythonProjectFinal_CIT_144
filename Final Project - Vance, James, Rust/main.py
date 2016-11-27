
################################################################
## Final Project for CIT 144 Intro to Programming Using Python #
##              Textbook Quiz Application                      #
##   By:                                                       #
##      Casey James                                            #
##      Matthew Vance                                          #
##      Kyle Rust                                              #
################################################################


### Imports
from tkinter import *
from Questions import *
import random


### GUI Class
class GUI:
    def __init__(self):

        ### Setting up a Window in tkinter at 600x180 resolution
        window = Tk()
        window.title("Introduction to Programming Using Python")
        window.geometry('1380x720')

        ### GUI Class Variables
        self.str_Question = StringVar()
        self._Answer = IntVar()
        self.answerOne = StringVar()
        self.answerTwo = StringVar()
        self.answerThree = StringVar()
        self.answerFour = StringVar()
        self.myAnswer = StringVar()
        self.correctAnswer = StringVar()
        self.chapter = IntVar() 
        self.questionNumber = IntVar()
        self._Chapter = IntVar()

        self.RightAnswers = IntVar()
        self.TotalQuestions = IntVar()
 
        
        ### Frame 1 GUI Elements
        frame1 = Frame(window)
        frame1.pack()
        rbChapterOne = Radiobutton(frame1, text = "Chapter 1",  variable = self._Chapter, value = 1, command = self.chapterRadio)
        rbChapterTwo = Radiobutton(frame1, text = "Chapter 2",  variable = self._Chapter, value = 2, command = self.chapterRadio)
        rbChapterThree = Radiobutton(frame1, text = "Chapter 3",  variable = self._Chapter, value = 3, command = self.chapterRadio)
        rbChapterFour = Radiobutton(frame1, text = "Chapter 4",  variable = self._Chapter, value = 4, command = self.chapterRadio)
        rbChapterFive = Radiobutton(frame1, text = "Chapter 5",  variable = self._Chapter, value = 5, command = self.chapterRadio)
        rbChapterSix = Radiobutton(frame1, text = "Chapter 6",  variable = self._Chapter, value = 6, command = self.chapterRadio)
        rbChapterSeven = Radiobutton(frame1, text = "Chapter 7",  variable = self._Chapter, value = 7, command = self.chapterRadio)
        rbChapterEight = Radiobutton(frame1, text = "Chapter 8",  variable = self._Chapter, value = 8, command = self.chapterRadio)
        rbChapterNine = Radiobutton(frame1, text = "Chapter 9",  variable = self._Chapter, value = 9, command = self.chapterRadio)
        rbChapterTen = Radiobutton(frame1, text = "Chapter 10",  variable = self._Chapter, value = 10, command = self.chapterRadio)
        rbChapterEleven = Radiobutton(frame1, text = "Chapter 11",  variable = self._Chapter, value = 11, command = self.chapterRadio)
        rbChapterTwelve = Radiobutton(frame1, text = "Chapter 12",  variable = self._Chapter, value = 12, command = self.chapterRadio)
        rbChapterThirteen = Radiobutton(frame1, text = "Chapter 13",  variable = self._Chapter, value = 13, command = self.chapterRadio)
        rbChapterFourteen = Radiobutton(frame1, text = "Chapter 14",  variable = self._Chapter, value = 14, command = self.chapterRadio)
        rbChapterFifteen = Radiobutton(frame1, text = "Chapter 15",  variable = self._Chapter, value = 15, command = self.chapterRadio)

        btBeginQuiz = Button(frame1, text = "Begin Quiz", command = self.BeginQuiz)
        rbChapterOne.grid(row = 0, column = 0, sticky = W)
        rbChapterTwo.grid(row = 0, column = 1, sticky = W)
        rbChapterThree.grid(row = 0, column = 2, sticky = W)
        rbChapterFour.grid(row = 0, column = 3, sticky = W)
        rbChapterFive.grid(row = 0, column = 4, sticky = W)
        rbChapterSix.grid(row = 0, column = 5, sticky = W)
        rbChapterSeven.grid(row = 0, column = 6, sticky = W)
        rbChapterEight.grid(row = 0, column = 7, sticky = W)
        rbChapterNine.grid(row = 0, column = 8, sticky = W)
        rbChapterTen.grid(row = 0, column = 9, sticky = W)
        rbChapterEleven.grid(row = 0, column = 10, sticky = W)
        rbChapterTwelve.grid(row = 0, column = 11, sticky = W)
        rbChapterThirteen.grid(row = 0, column = 12, sticky = W)
        rbChapterFourteen.grid(row = 0, column = 13, sticky = W)
        rbChapterFifteen.grid(row = 0, column = 14, sticky = W)
        btBeginQuiz.grid(row = 0, column = 17, sticky = E)
        
        ### Frame 2 GUI Elements
        frame2 = Frame(window)
        frame2.pack()

        self.lblQuestion = Label(frame2, text = "This is where the questions will go.")
        self.lblQuestion.grid(column = 0, columnspan = 5, sticky = W)

        ### Frame 3 GUI Elements
        frame3 = Frame(window)
        frame3.pack()
        btSubmitAnswer = Button(frame3, text = "Submit Answer", command = self.SubmitButton)
             
        rbAnswerOne = Radiobutton(frame3, textvariable = self.answerOne, variable = self._Answer, value = 1, command = self.processRadioButton)
        rbAnswerTwo = Radiobutton(frame3, textvariable = self.answerTwo, variable = self._Answer, value = 2, command = self.processRadioButton)
        rbAnswerThree = Radiobutton(frame3, textvariable = self.answerThree, variable = self._Answer, value = 3, command = self.processRadioButton)
        rbAnswerFour = Radiobutton(frame3, textvariable = self.answerFour, variable = self._Answer, value = 4, command = self.processRadioButton)

        rbAnswerOne.grid(row = 0, column = 0, sticky = W)
        rbAnswerTwo.grid(row = 1, column = 0, sticky = W)
        rbAnswerThree.grid(row = 2, column = 0, sticky = W)
        rbAnswerFour.grid(row = 3, column = 0, sticky = W)
        btSubmitAnswer.grid(row = 4, column = 0, sticky = W)

        
    
        
        window.mainloop()

    def Results(self):
        correct = self.RightAnswers.get()
        total = self.TotalQuestions.get()
        percent = (correct / total) * 100

        if (percent <= 59):
            grade = 'F'
        if (percent >= 60):
            grade = 'D'
        if (percent >= 70):
            grade = 'C'
        if (percent >= 80):
            grade = 'B'
        if (percent >= 90):
            grade = 'A'
            
        self.str_Question.set("This is where the questions will go")
        self.answerOne.set("A:")
        self.answerTwo.set("B:")
        self.answerThree.set("C:")
        self.answerFour.set("D:")
        messagebox.showinfo("Results", "You scored: " + str(correct) + " out of " + str(total) + \
                            "\nPercent: " + str(percent) + \
                            "\nGrade: " + grade)
        self.RightAnswers.set(0)
        self.TotalQuestions.set(0)

        


    def BeginQuiz(self):
        self.questionNumber.set(1) 
        self.Create_Question(self.chapter.get(), self.questionNumber.get())
        self.lblQuestion["text"] = self.str_Question.get()

    ### These Radio buttons determine what chapter the user is currently working on
    def chapterRadio(self):
        self.chapter.set(self._Chapter.get())
       


    ### This button submits the current answer for grading and then asks for antoher question
    def SubmitButton(self):
        if (self.myAnswer.get() == self.correctAnswer.get()):
            self.RightAnswers.set(self.RightAnswers.get() + 1)
        
        self.TotalQuestions.set(self.TotalQuestions.get() + 1)
            

        self.questionNumber.set(self.questionNumber.get()+1)
        self.Create_Question(self.chapter.get(), self.questionNumber.get())
        self.lblQuestion["text"] = self.str_Question.get()

        self._Answer.set(0)

        
    ### These Radio Buttons are the choices for the answers                
    def processRadioButton(self):
        if (self._Answer.get() == 1):
            self.myAnswer.set(self.answerOne.get())
        if (self._Answer.get() == 2):
            self.myAnswer.set(self.answerTwo.get())
        if (self._Answer.get() == 3):
            self.myAnswer.set(self.answerThree.get())
        if (self._Answer.get() == 4):
            self.myAnswer.set(self.answerFour.get())
        
   
    ### Uses the Questions.py file to create questions    
    def Create_Question(self, chapter, number):
        if (number <= 5): # If 5 questions haven't been asked, then it asks another
            
            ### Just chooses which chapter to quiz over, based on the user's radio button selection
            if (chapter == 1):
                chapterQuestions = chapter1_Questions
                chapterAnswers = chapter1_Answers
                
            if (chapter == 2):
                chapterQuestions = chapter2_Questions
                chapterAnswers = chapter2_Answers
                
            if (chapter == 3):
                chapterQuestions = chapter3_Questions
                chapterAnswers = chapter3_Answers
                
            if (chapter == 4):
                chapterQuestions = chapter4_Questions
                chapterAnswers = chapter4_Answers
                
            if (chapter == 5):
                chapterQuestions = chapter5_Questions
                chapterAnswers = chapter5_Answers
                
            if (chapter == 6):
                chapterQuestions = chapter6_Questions
                chapterAnswers = chapter6_Answers
                
            if (chapter == 7):
                chapterQuestions = chapter7_Questions
                chapterAnswers = chapter7_Answers
                
            if (chapter == 8):
                chapterQuestions = chapter8_Questions
                chapterAnswers = chapter8_Answers
                
            if (chapter == 9):
                chapterQuestions = chapter9_Questions
                chapterAnswers = chapter9_Answers
                
            if (chapter == 10):
                chapterQuestions = chapter10_Questions
                chapterAnswers = chapter10_Answers
                
            if (chapter == 11):
                chapterQuestions = chapter11_Questions
                chapterAnswers = chapter11_Answers
                
            if (chapter == 12):
                chapterQuestions = chapter12_Questions
                chapterAnswers = chapter12_Answers
                
            if (chapter == 13):
                chapterQuestions = chapter13_Questions
                chapterAnswers = chapter13_Answers
                
            if (chapter == 14):
                chapterQuestions = chapter14_Questions
                chapterAnswers = chapter14_Answers
                
            if (chapter == 15):
                chapterQuestions = chapter15_Questions
                chapterAnswers = chapter15_Answers
 
            MAX = len(chapterQuestions) # Asks a question within the range of the chapter (0 to However many questions there are in that particular chapter)
            question = random.randint(0, MAX -1) # Creates the current question
            correct = chapterAnswers[question] # Gets the correct answer associated with current question
            quiz_Answers = [] # List used to store current answer choices
            quiz_Answers.append(correct) # Makes sure that the correct answer is added to the list of choices
            self.correctAnswer.set(correct) # Stores the correct answer in a GUI class variable, so that the test can be graded properly

       
            self.str_Question.set(str(number) + ": " + chapterQuestions[question] + "?") # Creates the string that is seen on the Question Label

            ### Creates 3 additional choices besides the correct answer for our multiple choice questions
            for i in range (0,3): 
                nextAnswer = random.randint(0, MAX-1) # Finds a random answer from the chapter
                quiz_Answers.append(chapterAnswers[nextAnswer]) # Adds the random answer to the list of choices
        

            random.shuffle(quiz_Answers) # Shuffles the answer choices, so that the correct answer isn't always in the same spot

            ### Sets all of the answers in GUI class Variables, so that the Radio Buttons can use them
            self.answerOne.set(quiz_Answers[0])
            self.answerTwo.set(quiz_Answers[1])
            self.answerThree.set(quiz_Answers[2])
            self.answerFour.set(quiz_Answers[3])

        ### If 5 questions have been asked then results are given
        else:           
            self.Results()
           
       
        


GUI()

        
