import os
from dotenv import load_dotenv, find_dotenv
from pymongo import MongoClient
load_dotenv(find_dotenv())

password = os.environ.get("MONGODB_PWD")

# Connection with MongoDB
connection_string =f"mongodb+srv://LukaszWelna:{password}@codingchallenge.1erxlw7.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(connection_string)
db_pool = client.db_Pool

# Convert questions document to dictionary
def question_helper(question) -> dict:
    return {
        "id": str(question["_id"]),
        "content": question["content"],
        "a": question["a"],
        "b": question["b"],
        "c": question["c"],
        "d": question["d"],
    }

# Get questions from MongoDB
def receive_questions():
    collection = db_pool.coll_Questions
    questions = []
    for question in collection.find():
        questions.append(question_helper(question))
    return questions

# Get answears from MongoDB
def receive_answears():
    collection = db_pool.coll_Answears
    answears = []
    for answear in collection.find():
        answears.append(answear_helper(answear))
    return answears

# Convert answears document to dictionary
def answear_helper(answear) -> dict:
    return {
        "id": str(answear["_id"]),
        "answear": answear["answear"],
    }

# Convert answears document to dictionary
def good_answear_helper(answear) -> dict:
    return {
        "id": str(answear["_id"]),
        "good_answear": answear["good_answear"],
    }

def insert_answear(user_answear: dict) -> dict:
    collection = db_pool.coll_Answears
    inserted_id = collection.insert_one(user_answear).inserted_id
    inserted_answear = collection.find_one({"_id": inserted_id})
    return answear_helper(inserted_answear)

def calculate_answear_average(answears: list) -> float:
    sum = 0
    collection = db_pool.coll_GoodAnswears
    good_answears = []
    for answear in collection.find():
        good_answears.append(good_answear_helper(answear))

    for index in range(len(answears)):
        for value in answears[index]['answear']:
            if value == good_answears[0]["good_answear"]:
                sum += 1
    average = sum / len(answears) * 100
    return average

#ans = [{'id': '637a77c8bed886f872ee8b87', 'answear': 'a'}, {'id': '637a77c8bed886f872ee8b87', 'answear': 'b'}, {'id': '637a77c8bed886f872ee8b87', 'answear': 'b'}]
#print(calculate_answear_average(ans))
# Get answears from MongoDB
# def receive_answears():
#     collection = db_pool.coll_Answears
#     answears = []
#     for answear in collection.find():
#         answears.append(answear_helper(answear))
#     return answears


# def insert_test_document():
#     collection = db_pool.coll_GoodAnswears
#     first_question = {
#         "good_answear": "b",
#     }

#     inserted_id = collection.insert_one(first_question).inserted_id
#     print(inserted_id)

# insert_test_document()