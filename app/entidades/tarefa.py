class Tarefa():
    def __init__(self, titulo, descricao):
        self.__titulo = titulo
        self.__descricao = descricao


    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def descricao(self):
        return self.__descricao

    @descricao.setter
    def descricao(self, descricao):
        self.__descricao = descricao