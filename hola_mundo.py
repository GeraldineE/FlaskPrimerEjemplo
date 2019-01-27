from flask import Flask

app = Flask(__name__)#nuevo objeto
@app.route('/')#wrap indica en que el usuario puede entrar('/')
def index(): #Funcion que regresa un string
    return 'Hola mundo'

app.run() #Se encarga de ejecutar el servidor por default en el puerto 5000s
