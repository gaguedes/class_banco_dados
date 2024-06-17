import pyodbc

class dadosConexao:
    def __init__(self, ipServidor, bancoDados, usuario, senha):
        self.ipServidor = ipServidor
        self.bancoDados = bancoDados
        self.usuario = usuario
        self.senha = senha


class conexao(dadosConexao):
    def __init__(self, ipServidor, bancoDados, usuario, senha):
        dadosConexao.__init__(self, ipServidor, bancoDados, usuario, senha)

    def exec(self, query):
        self.query = query

        cnxn = pyodbc.connect(
            'DRIVER={ODBC Driver 17 for SQL Server};SERVER=' + self.ipServidor + 
            ';DATABASE=' + self.bancoDados + 
            ';UID=' + self.usuario + 
            ';PWD=' + self.senha + 
            ';TrustServerCertificate=YES')
        cursor = cnxn.cursor()
        
        try:
            if 'SELECT' in self.query and 'INSERT' not in self.query:
                cursor.execute(self.query)
                resultado = cursor.fetchall()
                return resultado
            else:
                cursor.execute(self.query)
                cursor.commit()
                return 'ACAO REALIZADA COM SUCESSO'
        except Exception as e:
            return 'ERRO AO REALIZAR AÇÃO'
