# create class called "Question"
class Question:
    # create module to call on for object that is linked to the class "Question"
    def __init__(self, q_text, q_answer):
        # create attributes "text" and "answer"
        self.text = q_text
        self.answer = q_answer


# test code
# practice_q = Question("hello", "True")
# print(practice_q.text)
