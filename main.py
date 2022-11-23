from fastapi import FastAPI, HTTPException
from fastapi.encoders import jsonable_encoder
from server.database import (
    receive_questions,
    insert_answer,
    receive_answers,
    calculate_answer_average
)
from server.models import response_model, Answer
from exceptions import WrongValueException
from utilities import check_user_answer

app = FastAPI()

@app.get("/question/", response_description="Question received")
def get_questions():
    """
    Retrieve the questions from database
    """
    questions = receive_questions()
    if questions:
        return response_model(questions, "Question data received successfully")
    return response_model(questions, "Empty")

@app.post("/answer")
def post_answers(user_answer: Answer):
    """
    Post answers in database
    """
    user_answer = jsonable_encoder(user_answer)
    try:
        if check_user_answer(answer=user_answer['answer']):
            new_user_answer = insert_answer(user_answer)
            return response_model(new_user_answer, "Thank You")
    except WrongValueException as e:
        raise HTTPException(status_code=400, detail=repr(e))

@app.get("/average/", response_description="Answers received")
def get_answers():
    """
    Retrieve the answers from database and calculate average of good answers
    """
    answers = receive_answers()
    average = calculate_answer_average(answers)
    if answers:
        return response_model(answers, f"Average of good answers: {average}%")
    return response_model(answers, "Empty list of answers")
