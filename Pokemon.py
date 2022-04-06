class Pokemon:
    def __init__(self, id, name, base_exp, generation, type):
        self.id = id
        self.name = name
        self.base_exp = base_exp
        self.generation = generation
        self.type = type

    def print_info(self):
        tipos = ', '.join([t['type']['name'] for t in self.type])

        resposta = "ID: " + str(self.id) + "\nEspécie: " + self.name + "\nTipo: " + tipos + "\nEXP Base: " + str(
            self.base_exp) + "\nGeração: " + self.generation
        print(resposta)
