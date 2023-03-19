import csv
from My_own_tests.enums.security_enums import SecTypes
from pydantic import ValidationError, BaseModel, validator, Field


class Sec(BaseModel):
    ID: str
    Sec_type: SecTypes = Field(alias='SEC_TYPE')
    Name: str = Field(alias='NAME')
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

with open('C:/Users/User/PycharmProjects/pytest/My_own_tests/test_data/sec_names.csv', newline='') as sec_names:
    sec_reader = csv.DictReader(sec_names)
    for row in sec_reader:
        # print(row['ID'], row['SEC_TYPE'], row['NAME'], row['SYMBOL'])
        try:
            sec = Sec.parse_obj(row)
            print(row)
        except ValidationError as e:
            print(row, e)
