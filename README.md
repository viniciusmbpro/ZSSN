Deploy: https://zssn-vmb.herokuapp.com/

Demonstração: https://youtu.be/jctl0kYenOE

``Este sistema é composto por uma API e uma interface web que fornecem acesso aos dados de sobreviventes de um apocalipse zumbi. A API fornece os seguintes endpoints:``

* https://zssn-vmb.herokuapp.com/api/survivors/: Este endpoint fornece uma lista de todos os sobreviventes cadastrados. Ele também permite a criação de novos sobreviventes através de uma requisição POST.
* https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/: Este endpoint fornece informações sobre um sobrevivente específico, identificado pelo ID (pk). Ele também permite a atualização das informações desse sobrevivente através de uma requisição PUT.
* https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/mark_as_infected/: Este endpoint marca um sobrevivente como infectado. Ele deve ser acessado através de uma requisição PUT.
* https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/report_infected/: Este endpoint permite ao usuário relatar um sobrevivente infectado. Ele deve ser acessado através de uma requisição PUT.
* https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/make_trade/: Este endpoint permite a realização de trocas entre sobreviventes. Ele deve ser acessado através de uma requisição PUT.
* https://zssn-vmb.herokuapp.com/api/get_resources_report/: Este endpoint fornece um relatório dos recursos disponíveis.

``Exemplos:``

Para obter a lista de sobreviventes, faça uma requisição GET para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/
* Para criar um novo sobrevivente, faça uma requisição POST para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ com os dados do sobrevivente (nome, idade, sexo, latitude, longitude) no corpo da requisição.
* Para obter as informações de um sobrevivente específico, faça uma requisição GET para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/ onde ``<pk>`` é o ID do sobrevivente.
* Para atualizar as informações de um sobrevivente, faça uma requisição PUT para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/ com os novos dados no corpo da requisição.
* Para marcar um sobrevivente como infectado, faça uma requisição PUT para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/mark_as_infected/
* Para relatar um sobrevivente infectado, faça uma requisição PUT para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/report_infected/
* Para realizar uma troca entre sobreviventes, faça uma requisição PUT para o endpoint https://zssn-vmb.herokuapp.com/api/survivors/ ``<pk>``/make_trade/ com os dados da troca (itens e pontos dos sobreviventes envolvidos) no corpo da requisição.
* Para obter um relatório dos recursos disponíveis, faça uma requisição GET para o endpoint https://zssn-vmb.herokuapp.com/api/get_resources_report/. Este relatório mostrará a quantidade de cada item disponível entre todos os sobreviventes.

Além dos endpoints mencionados acima, a interface web também fornece acesso às funcionalidades da API através de formulários e botões, demonstrando com utilizar a API. Esses formulários permitem ao usuário inserir informações e realizar ações, como criar um novo sobrevivente, marcar um sobrevivente como infectado, relatar um sobrevivente infectado e realizar trocas entre sobreviventes. Os botões também permitem que o usuário acesse as informações de um sobrevivente específico, ver a lista de sobreviventes e obter o relatório de recursos.

Em resumo, este sistema fornece uma maneira fácil e intuitiva de gerenciar e acessar informações sobre sobreviventes de um apocalipse zumbi, incluindo a criação, atualização, marcação como infectado, relato de infectados, realização de trocas e obtenção de relatórios.
