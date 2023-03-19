from My_own_tests.enums.security_enums import SecTypes
from pydantic import BaseModel, validator, ValidationError
import xmltodict

with open("C:/Users/User/PycharmProjects/pytest/My_own_tests/test_data/response.xml") as fd:
    obj = xmltodict.parse(fd.read())
    print(obj)


class Security(BaseModel):
    ID: str
    Ticket: str
    SecTypeID: int
    Sec_type: SecTypes
    Name: str
    SYMBOL: str

    @validator('ID', pre=True, always=True)
    def check_id_isalnums(cls, ID):
        if ID.isalnum() and ID.isupper():
            return ID
        else:
            raise ValueError('ID is not correct!')

    @validator('SYMBOL', pre=True, always=True)
    def check_symbol_isalnums(cls, SYMBOL):
        if SYMBOL.isalnum() and SYMBOL.isupper():
            return SYMBOL
        else:
            raise ValueError('SYMBOL is not correct!')

class Securities(BaseModel):
    security: list[Security]

try:
    security = Securities.parse_obj(obj['securities'])
    print(security)
except ValidationError as e:
    print(e)
