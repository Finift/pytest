from enum import Enum


class Genders(Enum):
    female = "female"
    male = "male"
# таким образом мы перечислили все возможные гендеры


class Statuses(Enum):
    inactive = "inactive"
    active = "active"
    banned = "banned"
    deleted = "deleted"


class UserErrors(Enum):
    WRONG_EMAIL = "Email doesn't contain @"
