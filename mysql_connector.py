import mysql.connector
# from mysql.connector import 
from  mysql.connector import errorcode

configuracao = {
'user':'root', 
'password':'', 
'host':'127.0.0.1', 
'database': 'cremosinho'
};

try:
    conexao = mysql.connector.connect(**configuracao);

except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha invalidos");
        elif erro.errno == errorcode.ER_BAD_DB_ERROR:
            print("Bando de dados nao existe");
        else:
            print("Erro");
else:
    conexao.close();