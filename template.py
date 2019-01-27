from flask import Flask
from flask import render_template

app = Flask(__name__)#nuevo objeto
@app.route('/')#wrap indica en que el usuario puede entrar('/')
def index(): #Funcion que regresa un string
    return render_template('index.html')


if __name__=='__main__':
    app.run(debug= True, port=8000) #Se encarga de ejecutar/levantar el servidor por default en el puerto 5000s
                                #debug si es falso no le permite a mi servidor estar a la escucha ante cualquier cambio que se haga dentro de mi proyecto
