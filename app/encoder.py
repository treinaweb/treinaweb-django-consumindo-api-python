import json

class MeuEncoder(json.JSONEncoder):
    def default(self, o):
        return {k.lstrip('Tarefa__'): v for k, v in vars(o).items()}