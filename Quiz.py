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
        #         # label = tk.Label(master=frame, text=f"Row {i}\nColumn {j}", padx=5 , pady=5

        label1=tk.Label(text="QUIZ",font=30)
        label1.grid(row=0,column =2)

        label1.grid(row=0,column=3)

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

        l=[label2,label3,label4,label5,label6,label8,label9,label10]

        for i in l:# loop through the labels
            for j in questions:
                print(j)






        window.mainloop()



    def main(self):

        questions={}
        self.read_file(questions) # pulls questions from files and stores them in a dictionary.
        self.display(questions)







if __name__ == "__main__":
    c= Quiz()
    c.main()