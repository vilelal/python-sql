#importando as bibliotecas (Abreviei o pandas para pd)
import pandas as pd
import pyodbc

#importando o arquivo csv. O try e except servirá caso haja algum erro com a leitura.
try:
  df=pd.read_csv('Agenda_contatos.csv')
  print("Arquivo lido com sucesso.")
except:
  print("Falha ao ler o arquivo. Observe se o nome do arquivo foi escrito corretamente.")


#Criando uma cadeia de conexão
SERVER = 'DESKTOP-RUTJMII'
DATABASE = 'Agenda_contatos'
USUARIO = 'sa'
SENHA = 'pe20082001'

try:
  # Estrutura de String Responsável por pegar os dados necessários para a conexão com o banco
  string_conexao = f'DRIVER={{SQL Server Native Client 11.0}};SERVER={SERVER};DATABASE={DATABASE};UID={USUARIO};PWD={SENHA};TrustServerCertificate=yes'
  print("Sucesso na conexão com banco de dados.")

except:
  print("Falha ao conectar no banco de dados. Confira se, nos dados colocados para a conexão, não há nenhum erro")

#Codigo que irá conectar o python ao banco de dados
conexao= pyodbc.connect(string_conexao)

#Elemento que irá executar comandos no Sql, possibilitando o pyodbc utilizar comandos do sql
cursor = conexao.cursor()


#iterando o Data Frame e dizendo para pegar todas as linhas (index) e as informações dentro da linha(row)
try:
  for index, row in df.iterrows():
    #Comando em sql para a inserção de informações.
    sql = "INSERT INTO contatos (nome, email, telefone, cep) VALUES (?, ?, ?, ?)"
    
    #Comando para executar
    cursor.execute(sql, tuple(row))
    cursor.commit()
  #Fechando a conexão
  conexao.close()
  print("Inserção realizada com êxito.")
except:
  print("Falha na inserção dos dados no SQL. Confira se a sintexe ou o código está escrito corretamente. ")