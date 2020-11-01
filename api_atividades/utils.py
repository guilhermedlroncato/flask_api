from models import Pessoas, Atividades

def insere_pessoa():
    pessoa = Pessoas(nome = 'Joana', idade = 10)
    pessoa.save()
    print(pessoa)

def consulta_pessoa():
    pessoas = Pessoas.query.all()
    for p in pessoas:
        print(f'{p.nome} - { p.idade}')

def altera_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Guilherme').first()
    pessoa.idade = 35
    pessoa.save()

def exclui_pessoa():
    pessoa = Pessoas.query.filter_by(nome = 'Guilherme').first()
    pessoa.delete()


if __name__ == '__main__':
    #insere_pessoa()
    #altera_pessoa()
    exclui_pessoa()
    consulta_pessoa()