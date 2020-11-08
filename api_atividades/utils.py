from models import Pessoas, Atividades, Usuarios

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

def insere_usuario(login, senha):
    usuario = Usuarios(login = login, senha = senha)
    usuario.save()


if __name__ == '__main__':
    insere_usuario('guilherme', '123')
    insere_usuario('roncato', '123')