from fastapi import FastAPI
from server.database import receive_questions, insert_answear, receive_answears, calculate_answear_average
from server.models import response_model, Answear
from fastapi.encoders import jsonable_encoder

class Wrong_Value_Exception(Exception):
    def __init__(self, answear_value) -> None:
        super().__init__(f"{answear_value} is wrong value. Please choose option a, b, c or d")

def check_user_answear(answear: str) -> bool:
    if answear in {'a', 'b', 'c','d'}:
        return True
    raise Wrong_Value_Exception(answear)

app = FastAPI()

@app.get("/")
def index():
    return {"message": "Hello World"}

# Get questions from MongoDB
@app.get("/Question/", response_description="Question received")
def get_questions():
    """
    Retrieve the question from database
    """
    questions = receive_questions()
    if questions:
        return response_model(questions, "Question data received successfully")
    return response_model(questions, "Empty")

# Post answears to MongoDB
@app.post("/Answear")
def post_answears(user_answear: Answear):
    user_answear = jsonable_encoder(user_answear)
    try:
        if check_user_answear(answear=user_answear['answear']):
            new_user_answear = insert_answear(user_answear)
            return response_model(new_user_answear, "Thank You")
    except Wrong_Value_Exception as e:
        print(e)
        
# Get answears from MongoDB and calculate average of good answears
@app.get("/Average/", response_description="Answears received")
def get_answears():
    """
    Retrieve the answears from database 
    """
    answears = receive_answears()
    print(answears)
    average = calculate_answear_average(answears)
    if answears:
        return response_model(answears, f"Average: {average}")
    return response_model(answears, "Empty")
