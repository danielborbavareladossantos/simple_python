from Pessoas import Pessoas

try:
    nome: str = str(input('Qual seu nome? '))
    sobrenome: str = str(input('Qual seu sobrenome? '))
    idade: int = int(input('Qual sua idade? '))
    p = Pessoas(nome,sobrenome,idade)
    print("Seu nome é " + p.retornoNomeCompleto() + " e sua idade é "+str(p.idade))
except Exception as e:
    print("Erro: ", e)