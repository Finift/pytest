from pydantic import BaseModel, validator
from src.enums.user_enums import Genders, Statuses, UserErrors


class User(BaseModel):
    # опишем нашу модель json
    id: int
    name: str
    email: str
    gender: Genders #тут будут рассматриваться только значения из Genders в нашем enum
    status: Statuses

    @validator('email')
    def check_that_at_in_email(cls, email):
        if '@' in email:
            return email
        else:
            raise ValueError(UserErrors.WRONG_EMAIL.value)
