import csv
from My_own_tests.enums.security_enums import SecTypes
from pydantic import ValidationError, BaseModel, validator, Field


class References(BaseModel):
    Code: str
    Sec_type: SecTypes = Field(alias='Type Name')

    @validator('Code', pre=True, always=True)
    def check_code_isalnums(cls, Code):
        if Code == "" or Code == None:
            raise ValueError('Code is missing!')
        elif Code.isalnum() and Code.isupper() and (3 <= len(Code) <= 4):
            return Code
        else:
            raise ValueError('Code is not correct!')


with open('C:/Users/User/PycharmProjects/pytest/My_own_tests/test_data/sec_types_reference.csv',
          newline='') as ref_types:
    ref_reader = csv.DictReader(ref_types, delimiter=',')
    for row in ref_reader:
        try:
            ref = References.parse_obj(row)
            print(row)
        except ValidationError as e:
            print(row, e)
