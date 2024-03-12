# JogoTeca

## Descrição do Projeto

O JogoTeca é um aplicativo desenvolvido em Flask Python que permite aos usuários armazenar e gerenciar uma biblioteca pessoal de jogos. O sistema oferece funcionalidades básicas de CRUD (Create, Read, Update, Delete), onde os usuários podem cadastrar novos jogos, visualizar sua coleção, editar informações existentes e excluir jogos.

O projeto exige um sistema de login, onde os usuários podem criar uma conta que será armazenada em um banco de dados MySQL com senhas encriptadas para garantir a segurança dos dados.

Na tela principal, os usuários têm acesso à sua coleção de jogos, que é exibida por meio de imagens dos jogos, juntamente com o nome, categoria e o tipo de console associado a cada jogo. Ao lado de cada jogo, há botões para editar e excluir, permitindo que os usuários atualizem ou removam jogos conforme desejado.

Além disso, há um botão "Novo" que direciona os usuários para a tela de cadastro de um novo jogo. Da mesma forma, a lógica do botão "Editar" é aplicada, levando os usuários para a tela de edição de um jogo específico.

O aplicativo também possui um botão "Logout", que permite aos usuários sair de suas contas atuais.

## Exemplos

A seguir, são fornecidos exemplos visuais das telas principais do JogoTeca:

- [Tela de Login](exemplos/tela_login.png)
- [Tela Principal (Coleção de Jogos)](exemplos/tela_principal.png)
- [Tela de Cadastro de Novo Jogo](exemplos/tela_cadastro.png)
- [Tela de Edição de Jogo Existente](exemplos/tela_edicao.png)

## Tecnologias Utilizadas

- Backend: Flask (Python)
- Banco de Dados: MySQL

## Como Executar o Projeto

1. Clone este repositório em sua máquina local.
2. Certifique-se de ter o Python e o Flask instalados.
3. Configure as credenciais do banco de dados no arquivo de configuração correspondente.
4. Execute o jogoteca.py.
5. Abra o navegador e acesse o endereço indicado pelo Flask.

## Contribuindo

Contribuições são bem-vindas! Sinta-se à vontade para enviar pull requests ou relatar problemas encontrados.

## Licença

Este projeto está licenciado sob a MIT License.
