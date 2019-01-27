from flask import Flask
from flask import request

app = Flask(__name__)#nuevo objeto
@app.route('/')#wrap indica en que el usuario puede entrar('/')
def index(): #Funcion que regresa un string
    return 'cambios hola'

#http://localhost:8000/params?params1=Geraldine&params2=test_dos
#http://localhost:8000/params
@app.route('/params')
def params():
    param=request.args.get('params1','no contiene este parametro')
    param_dos=request.args.get('params2','no contiene este parametro')
    return 'El parametro es : {} , {}'.format(param,param_dos)

if __name__=='__main__':
    app.run(debug= True, port=8000) #Se encarga de ejecutar/levantar el servidor por default en el puerto 5000s
                                    #debug si es falso no le permite a mi servidor estar a la escucha ante cualquier cambio que se haga dentro de mi proyecto
