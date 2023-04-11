from Study.src.baseclasses.response import Response
from Study.src.schemas.user import User


def test_getting_users_list(get_users, status_code, make_number):
    Response(get_users).assert_status_code(status_code).validate(User)
    
