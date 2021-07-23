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
    #criando a conexão
    conexao = mysql.connector.connect(**configuracao);
    cursor = conexao.cursor();

except mysql.connector.Error as erro:
        if erro.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Usuario ou senha invalidos");
        elif erro.errno == errorcode.ER_BAD_DB_ERROR:
            print("Bando de dados nao existe");
        else:
            print("Erro");
else:
    
    while(True):
        #comando
        inserir_cliente = ("insert into cliente (nome, telefone, observacao, cidade, estado, tipo_pessoa)" 
        "values (%(nome_contato)s, %(telefone)s, %(observacao)s, %(cidade)s, %(estado)s, %(tipo_pessoa)s)");
        
        #Consultas
        
        '''
        ##Select  
        consulta = ("select nome, telefone, celular from contatos where nome like 'M%'");
        cursor.execute(consulta);

        for (nome, telefone, celular) in cursor:
            print(f"Nome: {nome}, telefone: {telefone}, celular: {celular}");
        ## FIM SELECT #############################
        '''

        #Dados do cliente:
        _nome = input("\nNome do cliente: ")
        _telefone = input("\Telefone do cliente: ")
        _observacao = input("\nOnde entregar: ")
        _cidade = input("\nCidade do cliente: ")
        _estado = input("\nEstado: ")
        _tipo_pessoa = input("\nFisica ou Juridica? ")
        

        #valores
        cliente = {
            'nome_contato' : _nome,
            'telefone' : _telefone,
            'observacao' : _observacao,
            'cidade' : _cidade,
            'estado' : _estado,
            'tipo_pessoa' : _tipo_pessoa
        };

        cursor.execute(inserir_cliente, cliente);
        conexao.commit();

    conexao.close();
