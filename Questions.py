class Questions:

    def __init__(self, question, answer):
        self.question = question
        self.answer= answer



    def __str__(self):
        return "the question is" + self.question +" " + self.answer

    def question(self):
        return " the question is " + self.question()

    def answer(self):
        return " the answer is "+ self.answer()