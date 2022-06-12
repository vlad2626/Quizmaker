import random
import tkinter as tk
from tkinter import *
from tkinter import ttk



import Questions
class Quiz:




    # read the file
    # grab 5 random questions and add to a data structure, possibly dictionary or hashmap
    # display the questions
    # have the user enter the inputs
    # calculate the correct answers
    # display percentage of  correct answers .

    def read_file(self, questions):
        #questions = {}
        question=''
        file = open("key", "r")
        count=0

        l =len(question)
        line = ""

        for i in file:
            question = i
            l = len(question)
            correct = question.find("?"[:l]) # finds the length of the line. no errors
            answer=question[correct+1:]  # prints everything after the question mark

            flip = random.randint(0,50)
            if count<10:
                if flip <25:
                    questions[question] = answer
                    count+=1


            if count==10: # one we get 10 questions exit loop.
                break
        file.close()
        return questions


    def display(self,questions):
        #print(questions)
        window = Tk()

        # frm = ttk.Frame(root, padding=20)
        #         # frm.grid()
        #         # ttk.Label(frm, text="Hello World!").grid(column=4, row=7)
        #         # ttk.Entry().grid(column=4, row=8)
        #         # ttk.Button(frm, text="Quit", command=root.destroy).grid(column=6, row=10)

        frame = tk.Frame(
            master=window,
            relief=tk.RIDGE,
            borderwidth=5
        )

        window.rowconfigure([0,1,2,3,4], minsize=50)
        window.columnconfigure([0, 1, 2, 3,4,5,6,7,8,9], minsize=50)

        #unused loop.
        # for i in range(3):
        #     window.columnconfigure(i, weight=1, minsize=75)
        #     window.rowconfigure(i, weight=1, minsize=50)
        #
        #     for j in range(3):
        #         frame = tk.Frame(
        #             master=window,
        #             relief= tk.RIDGE,
        #             borderwidth=5
        #         )
        #         frame.grid(row=i,column=j, padx=5, pady=5)
        #         # label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", padx=5 , pady=5#

        k=tk.Label(text="QUIZ",font=30)
        k.grid(row=0,column=3)

        label1=tk.Label(text="")
        label2= tk.Label(text="")
        label3 = tk.Label(text="")
        label4 = tk.Label(text="")
        label5 = tk.Label(text="")
        label6 = tk.Label(text="")
        label7 = tk.Label(text="")
        label8 = tk.Label(text="")
        label9 = tk.Label(text="")
        label10 = tk.Label(text="")
        label11 = tk.Label(text="")
        label12 = tk.Label(text="")# labels
        # entry boxes
        entry1=tk.Entry(tk.Entry(master=window, width=30))
        entry2 = tk.Entry(tk.Entry(master=window, width=30))
        entry3 = tk.Entry(tk.Entry(master=window, width=30))
        entry4 = tk.Entry(tk.Entry(master=window, width=30))
        entry5 = tk.Entry(tk.Entry(master=window, width=30))
        entry6 = tk.Entry(tk.Entry(master=window, width=30))
        entry7 = tk.Entry(tk.Entry(master=window, width=30))
        entry8 = tk.Entry(tk.Entry(master=window, width=30))
        entry9 = tk.Entry(tk.Entry(master=window, width=30))
        entry10 = tk.Entry(tk.Entry(master=window, width=30))
        entry11 = tk.Entry(tk.Entry(master=window, width=30))


        values = list(questions.values())
        keys= list(questions.keys())

        quizQuestions=[]
        quizAnswers=[]
        l=[label1,label2,label3,label4,label5,label6,label8,label9,label10,label11,]
        boxes=[entry1,entry2,entry3,entry4,entry5,entry6,entry7,entry8,entry9,entry10]





        count1=0
        count2=0
        q2=""
        trimmed=""


        # sets the label text to the dictionary
        for i in l:# loop through the labels

            q=keys[count1]
            trimmed=q.find("?"[:len(q)])# afer question mark finds the answer
            trimmed2 = q[:trimmed+1]  # question

            finalAnswer=q[trimmed+1:len(q)-1]  # answer


            finalQuestion=trimmed2 # question
            # populate list with correct answerrs
            quizQuestions.append(finalQuestion)
            quizAnswers.append(finalAnswer)
            i=tk.Label(text=finalQuestion)

            i.grid(column=1, row= count1+1)
            count1 += 1

        print(quizAnswers)
        print(quizQuestions)
        # text boxes
        for j in boxes:  # loop through the labels
            j= tk.Entry(master=window, width=30)
            j.grid(column=3, row=count2+1)
            count2+=1








        window.mainloop()



    def main(self):

        questions={}
        self.read_file(questions) # pulls questions from files and stores them in a dictionary.
        self.display(questions)







if __name__ == "__main__":
    c= Quiz()
    c.main()