# Quiz Game

# import
from question_model import Question
from quiz_brain import QuizBrain
from data import question_data

# test code
# print(question_data[0])
# print(question_data[0]["text"])

# create list
question_bank = []

# append string data from dictionary into a list of objects
# converting string to object helps to prevent typos, changes, modifications, etc. when using strings
for item in question_data:
    # extract data from inputted dictionary using dictionary keys
    question_text = item["text"]
    question_answer = item["answer"]

    # input extracted data into a  list of objects by using a class
    new_question = Question(question_text, question_answer)

    # append class object to list
    question_bank.append(new_question)

# create class object "quiz" from class "QuizBrain"
quiz = QuizBrain(question_bank)

while quiz.still_has_questions():  # if quiz still has questions
    quiz.next_question()
print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(quiz.question_list)}")

# total questions can also be: len(question_bank)  or  quiz.question_number

# test code
# print(question_bank)  # outputs class objects
# print(question_bank[0])  # outputs first class object
# print(question_bank[0].text)
# print(question_bank[0]["text"])  # TypeError: 'Question' object is not subscriptable
# to make objects subscriptable, use __getitem__  # SPECIAL NOTE ABOUT SUBSCRIPTABLE
# print(question_bank[0].answer)  # output "True" or "False"
# print(question_bank[0].answer.lower())  # output "true" or "false"
# print((question_bank[0].answer.lower())[0])  # output is "t" or "f"


# TODO THIS WORKS AS FINAL SOLUTION, BUT THE INSTRUCTOR WANTS TO DO SOMETHING DIFFERENT
# variables
# total_questions = len(question_bank)
# total_correct = 0
#
# print("Type 'T' for True or 'F' for false")
# for item in range(total_questions):
#
#     choice = input(f"Q{item+1}: {question_bank[item].text}: ").lower()
#
#     if (choice == question_bank[item].answer.lower()) or (choice == question_bank[item].answer.lower()[0]):
#         print("Correct.")
#         total_correct += 1
#     elif (choice != question_bank[item].answer.lower()) or (choice != question_bank[item].answer.lower()[0]):
#         print(f"That's wrong. The correct answer is: {question_bank[item].answer}")
#
#     print(f"Your current score is: {total_correct}/{item+1}")
#
# print(f"Total score: {total_correct} out of {total_questions}")
