from pydantic import BaseModel, Field

def response_model(data, message):
    """
    Function which shows result in API
    """
    return{
        "data": [data],
        "code": 200,
        "message": message
    }

class Answer(BaseModel):
    """
    Model to validate if answer data is proper
    """
    answer: str = Field(...)
