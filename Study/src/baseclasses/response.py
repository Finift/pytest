#from jsonschema import validate
from Study.src.enums.global_enums import GlobalErrorMessages


class Response:
    def __init__(self, response):
        self.response = response
        self.response_json = response.json().get('data')
        self.response_status = response.status_code

    def validate(self, schema):
        if isinstance(self.response_json, list):
            for item in self.response_json:
                #добавили для этого метода:
                schema.parse_obj(item)
                #validate(item, schema)
        else:
            # добавили для этого метода:
            schema.parse_obj(self.response_json, schema)
            #validate(self.response_json, schema)
        # добавили для этого метода:
        return self

    def assert_status_code(self, status_code):
        if isinstance(status_code, list):
            assert self.response_status in status_code, self  # под волшебный метод
        else:
            assert self.response_status == status_code, self  # под волшебный метод
        return self

    # улучшим читабельность волшебным методом, добавим удобства для дебага:
    def __str__(self):
        return \
            f"Status code: {self.response_status} - {GlobalErrorMessages.WRONG_STATUS_CODE.value} \n" \
            f"Requested url: {self.response.url} \n" \
            f"Response body: {self.response_json}"

