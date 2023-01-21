Este sistema é composto por uma API RESTful construída com Django e Django REST framework. A API fornece uma série de endpoints para gerenciar os recursos de sobreviventes, incluindo criação, leitura, atualização e exclusão. Além disso, há endpoints adicionais para realizar operações específicas, como marcar um sobrevivente como infectado, relatar recursos e realizar trocas de recursos entre sobreviventes.

É composto por um banco de dados de sobreviventes de uma pandemia, com informações como nome, idade, sexo, localização, recursos possuídos e se está infectado ou não.

Os endpoints disponíveis são:

* /api/survivors/: Retorna a lista de todos os sobreviventes cadastrados no sistema. Também é possível cadastrar novos sobreviventes enviando um POST request para este endpoint com os dados do sobrevivente.
* /api/survivors/<int:pk>/: Retorna as informações de um sobrevivente específico, dado o seu id. É possível também atualizar as informações deste sobrevivente enviando um PUT request para este endpoint com os novos dados.
* /api/survivors/<int:pk>/mark_as_infected/: Marca um sobrevivente específico como infectado. Este endpoint só pode ser acessado através de um PUT request.
* /api/survivors/<int:pk>/make_trade/: Realiza uma troca de recursos entre dois sobreviventes específicos, dado o id dos dois sobreviventes e os recursos a serem trocados. Este endpoint só pode ser acessado através de um PUT request.
* /api/survivors/get_resources_report/: Retorna um relatório com a quantididade de recursos existentes entre todos os sobreviventes. Este endpoint só pode ser acessado através de um GET request.

Para utilizar estes endpoints é necessário enviar as requisições HTTP para as URLs específicas, junto com os parâmetros e corpos de requisição necessários, de acordo com a descrição de cada endpoint.

Além disso, é importante notar que ao cadastrar um novo sobrevivente ou realizar uma troca, os pontos dos sobreviventes são automaticamente calculados e atualizados de acordo com a quantidade de recursos possuídos.