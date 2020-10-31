from flask import Flask, jsonify, request
import json

app =  Flask(__name__)

desenvolvedores = [{'id': 0,
                    'nome': 'Guilherme',
                    'habilidades': ['Python', 'Flask']},
                   {'id': 1,
                    'nome': 'João',
                    'habilidades': ['Python', 'Django']}]

# consulta um desenvolvedot, altera um desenvolver e deleta um desenvolvedor
@app.route('/dev/<int:id>/', methods = ['GET', 'PUT', 'DELETE'])
def desenvolvedor(id):
    if request.method == 'GET':
        try:
            response = desenvolvedores[id]
        except IndexError:
            mensagem = f'Desenvolvedor id {id} não existe'
            response = {'status': 'erro', 'mensagem': mensagem}
        except Exception:
            mensagem = f'Erro desconhecido - Procure o ADM da API'
            response = {'status': 'erro', 'mensagem': mensagem}
        return jsonify(response)
    elif request.method == 'PUT':
        dados = json.loads(request.data)
        desenvolvedores[id] = dados
        return jsonify(dados)
    elif request.method == 'DELETE':
        desenvolvedores.pop(id)
        return jsonify({'status': 'sucesso', 'mensagem': 'registro excluido'})

# lista todos os desenvolvedores e permite incluir um novo desenvolvedor
@app.route('/dev/', methods = ['GET', 'POST'])
def lista_desenvolvedores():
    if request.method == 'POST':
        dados = json.loads(request.data)
        posicao = len(desenvolvedores)
        dados['id'] = posicao
        desenvolvedores.append(dados)
        return jsonify(desenvolvedores[posicao])
    elif request.method == 'GET':
        return jsonify(desenvolvedores)

if __name__ == '__main__':
    app.run()