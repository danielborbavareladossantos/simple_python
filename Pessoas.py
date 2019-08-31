class Pessoas:
    __nome: str
    __sobrenome: str
    __idade: int

    def __init__(self, nome, sobrenome, idade):
        self.nome = nome
        self.sobrenome = sobrenome
        self.idade = idade

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        try:
            self.__nome = str(nome)
        except Exception:
            raise Exception('Erro na inserção do atributo nome!')

    @property
    def sobrenome(self):
        return self.__sobrenome

    @sobrenome.setter
    def sobrenome(self, sobrenome):
        try:
            self.__sobrenome = str(sobrenome)
        except Exception:
            raise Exception('Erro na inserção do atributo sobrenome!')

    @property
    def idade(self):
        return self.__idade

    @idade.setter
    def idade(self, idade):
        try:
            self.__idade = int(idade)
        except Exception:
            raise Exception('Erro na inserção do atributo idade!')

    def retornoNomeCompleto(self):
        return self.__nome+" "+self.__sobrenome