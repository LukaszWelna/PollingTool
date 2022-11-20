from pydantic import BaseModel, Field

def response_model(data, message):
    return{
        "data": [data],
        "code": 200,
        "message": message
    }

class Answear(BaseModel):
    answear: str = Field(...)
