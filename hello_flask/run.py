from flask import Flask

app = Flask(__name__)

@app.route('/<nome>', methods = ['GET', 'POST'])
def ola(nome):
    return 'Olá {}'.format(nome)

if __name__ == '__main__':
    app.run()