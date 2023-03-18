from pydantic import BaseModel, validator, ValidationError
from My_own_tests.enums.security_enums import SecTypes


response = """{
"ID": "US0045DZ13",
"Sec_type": "Asset Backet",
"SecTypeID": "30",
"Ticket": "AAWW",
"country": "Ireland",
"Name": "15",
"SYMBOL": "AAET"
 }"""


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


try:
    security = Security.parse_raw(response)
except ValidationError as e:
    print(e.json(), response)
else:
    print(response)
