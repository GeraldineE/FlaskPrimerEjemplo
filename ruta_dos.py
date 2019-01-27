from flask import Flask
from flask import request

app = Flask(__name__)#nuevo objeto
@app.route('/')#wrap indica en que el usuario puede entrar('/')
def index(): #Funcion que regresa un string
    return 'cambios hola'

#http://localhost:8000/params?params1=Geraldine&params2=test_dos
#http://localhost:8000/params
#params/libros/1
@app.route('/params/')
@app.route('/params/<name>/')
@app.route('/params/<name>/<int:num>')
def params(name = 'este es un valor por default', num='nada'):
    param=request.args.get('params1','no contiene este parametro')
    param_dos=request.args.get('params2','no contiene este parametro')
    return 'El parametro es : {} {}'.format(name,num)

if __name__=='__main__':
    app.run(debug= True, port=8000) #Se encarga de ejecutar/levantar el servidor por default en el puerto 5000
                                    #debug si es falso no le permite a mi servidor estar a la escucha ante cualquier cambio que se haga dentro de mi proyecto
