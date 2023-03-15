import json

json_string = '{"name": "John Doe", "age": 30, "is_student": false}'

try:
    python_obj = json.loads(json_string)
    print(python_obj)
except ValueError as e:
    print("Error", e)


python_obj = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

json_str = json.dumps(python_obj, indent=4, sort_keys=True)
print(json_str)
