# 400 -> Bad Request
# 422 -> Unprocessable Entity

class HttpUnprocessableEntityError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__(message)
        self.message = message
        self.name = 'UnprocessableEntity'
        self.status_code = 422


try:
    print('Estou no bloco try')
    raise HttpUnprocessableEntityError('Estou lançando uma exception')
except HttpUnprocessableEntityError as exception:
    print('Estou no tratamento de erro')
    print(exception.name)
    print(exception.status_code)
    print(exception.message)
