import requests

from Study.configuration import SERVICE_URL

#from Study.src.schemas.post import POST_SCHEMA
from Study.src.baseclasses.response import Response
from Study.src.pydantic_schemas.post import Post


def test_getting_post():
    r = requests.get(url=SERVICE_URL)
    response = Response(r)

    #response.assert_status_code(200).validate(POST_SCHEMA)
    response.assert_status_code(200).validate(Post)


# [{'id': 1, 'title': 'Post 1'}, {'id': 2, 'title': 'Post 2'}, {'id': 3, 'title': 'Post 3'}]