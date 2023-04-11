import requests

class Blog:
    def __init__(self, name):
        self.name = name

    def posts(self):
        response = requests.get("https://jsonplaceholder.typicode.com/posts")

        return response.json()

    def __repr__(self):
        return '<Blog: {}>'.format(self.name)


# Этот код определяет класс Blog с методом posts.
# Запустив posts в Blog, вы инициируете вызов API.
# Ссылаясь на post в Blog, объект будет инициировать вызов API jsonplaceholder.