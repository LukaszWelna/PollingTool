import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

# Connection with MongoDB
connection_string =(f"mongodb+srv://LukaszWelna:{password}@codingchallenge.1erxlw7."
                    f"mongodb.net/?retryWrites=true&w=majority")
                    
client = MongoClient(connection_string)
db_pool = client.db_Pool

def question_helper(question) -> dict:
    """
    Convert question data to dictionary type
    """
    return {
        "id": str(question["_id"]),
        "content": question["content"],
        "a": question["a"],
        "b": question["b"],
        "c": question["c"],
        "d": question["d"],
    }

def receive_questions():
    """
    Retrieve the questions from database
    """
    collection = db_pool.coll_Questions
    questions = []
    for question in collection.find():
        questions.append(question_helper(question))
    return questions

def receive_answers():
    """
    Retrieve the answers from database
    """
    collection = db_pool.coll_Answers
    answers = []
    for answer in collection.find():
        answers.append(answer_helper(answer))
    return answers

def answer_helper(answer) -> dict:
    """
    Convert answer data to dictionary type
    """
    return {
        "id": str(answer["_id"]),
        "answer": answer["answer"],
    }

def good_answer_helper(answer) -> dict:
    """
    Convert good answer data to dictionary type
    """
    return {
        "id": str(answer["_id"]),
        "good_answer": answer["good_answer"],
    }

def insert_answer(user_answer: dict) -> dict:
    """
    Insert the answers to database
    """
    collection = db_pool.coll_Answers
    inserted_id = collection.insert_one(user_answer).inserted_id
    inserted_answer = collection.find_one({"_id": inserted_id})
    return answer_helper(inserted_answer)

def calculate_answer_average(answers: list) -> float:
    """
    Calculate average of good answers
    """
    sum_of_good_answers = 0
    collection = db_pool.coll_GoodAnswers
    good_answers = []
    for answer in collection.find():
        good_answers.append(good_answer_helper(answer))

    if (answers and good_answers):
        for value in answers:
            if value['answer'] == good_answers[0]["good_answer"]:
                sum_of_good_answers += 1
        average = sum_of_good_answers / len(answers) * 100
        return average
    return 0
