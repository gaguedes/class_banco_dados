# Classe para conexão com um banco de dados SQL Server
Classe em Python que realiza a conexão e execução de queries em bancos de dados SQL Server

## Como usar
Após clonar o projeto, realize a importação da classe no seu código principal:
```
import conexaoBancoDados
```
Para inciar a conexão, utilize o método "conexao" com os parâmetros necessários:
```
ipServidor = 'localhost'
bancoDados = 'mainDb'
usuario = 'SA'
senha = f'Abc1234'

conexao = conexaoBancoDados.conexao(ipServidor, bancoDados, usuario, senha)
```
Para realizar a primneira consulta, basta utilizar o método "exec" que existe na classe "conexao", passando a query:
```
query = 'SELECT TOP 1 * FROM [dbo].[Table]'
resultado = conexao.exec(query)
```
A função "exec" irá retornar os resultados em forma de lista, em caso de queries que realizem ações como Insert ou Update, o retorno será uma mensagem se sucesso ou erro.
