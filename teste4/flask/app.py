from flask import Flask, jsonify
from flask_cors import CORS
import pymysql

hostname = 'localhost'
username = 'root'
password = ''
database = 'relatorio_bd'
def doQuery( conn ) :
    cur = conn.cursor()

    cur.execute( "SELECT * FROM cadastro_de_operadoras;" )
    resultados = cur.fetchall()
    return resultados

def doQuery_specific( conn, key, value ) :
    cur = conn.cursor()

    cur.execute( f"SELECT * FROM cadastro_de_operadoras where {key} like '%{value}%';" )
    resultados = cur.fetchall()
    return resultados



DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)

CORS(app, resources={r'/*': {'origins': '*'}})


myConnection = pymysql.connect( host=hostname, user=username, passwd=password, db=database )


# Retorna todas as operadoras
@app.route('/pegar_todas_operadoras', methods = ['GET'])
def pegar_operadoras():
    result = doQuery( myConnection )
    return jsonify(result)

# Retorna operadora com registro ANS especificado
@app.route('/pesquisar_operadoras/<campo>/<valor_parecido>/', methods = ['GET'])
def procurar_operadoras(campo, valor_parecido):
    
    if(campo == "campo" and valor_parecido == "valor_parecido"):
        return jsonify(doQuery(myConnection))

   
    results = doQuery_specific(myConnection, campo, valor_parecido)
    return jsonify(results)    
    



    
if __name__ == "__main__":
    app.run(debug=True)