import csv
from My_own_tests.enums.security_enums import SecTypes
from pydantic import ValidationError, BaseModel, validator


class Sect(BaseModel):
    ID: str
    Sec_type: SecTypes
    SecTypeID: int
    Ticket: str

    @validator('ID', pre=True, always=True)
    def check_ids_isalnums(cls, ID):
        if ID.isalnum() and ID.isupper():
            return ID
        else:
            raise ValueError('ID is not correct!')

    @validator('Ticket', pre=True, always=True)
    def check_ticket_isalnums(cls, Ticket):
        if Ticket.replace(' ', '').isalnum():
            return Ticket
        else:
            raise ValueError('Ticket is not correct!')


with open('C:/Users/User/PycharmProjects/pytest/My_own_tests/test_data/sec_types.csv', newline='') as sec_types:
    sect_reader = csv.DictReader(sec_types, delimiter=';')
    for row in sect_reader:
        try:
            sect = Sect.parse_obj(row)
            print(row)
        except ValidationError as e:
            print(row, e)
