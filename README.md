# Introdução
Utilizando os conceitos de Programação Orientada a Objetos e Estrutura de Dados, nós, o grupo Winx, composto por André, Carlos, Gabriel e Jyan, desenvolvemos um programa em Python que simula um browser, onde se pode pesquisar páginas e suas respectivas páginas internas.

# Imagens
- Mensagem de boas-vindas
<img width="613" height="289" alt="boas-vindas" src="https://github.com/user-attachments/assets/883c5acd-d101-42b5-b4e4-c7367570e3b3" />

- Página encontrada
<img width="613" height="289" alt="pagina-encontrada" src="https://github.com/user-attachments/assets/bcad6401-c29f-4a0f-94e6-d8d440c7dc8c" />

- Links disponíveis
<img width="613" height="289" alt="links-disponiveis" src="https://github.com/user-attachments/assets/bc1514ac-afeb-4f5c-a2e1-27c74b602c35" />

- Página não encontrada
<img width="613" height="289" alt="pagina-nao-encontrada" src="https://github.com/user-attachments/assets/61e17f31-1ff8-45a3-a587-0f2e279372ba" />

# Como funciona
O programa utiliza duas estruturas de dados principais: **arvore binária** para armazenar as URLs do arquivo-texto e possibilitar o uso de URLs internas e **lista encadeada** para armazenar num histórico as URLs já pesquisadas. 

Ao iniciar o browser, o arquivo-texto é carregado no programa, separado em listas e para cada URL raiz ou principal é instanciada uma árvore, que por sua vez é armazenada numa lista simples chamada banco_de_dados. No caso de URLs internas, o programa procura qual a sua URL 'mãe' e adiciona a URL interna como filha desta.

A cada pesquisa, a URL home é armazenada no histórico e a URL encontrada agora ocupa o home. Caso a URL encontrada tenha URLs internas, estas são printadas na tela logo após encontrar a URL. Caso a URL não seja encontrada, uma mensagem aparece na tela: 'Página não encontrada :('. O browser também aceita comandos:

**#back ->** Retorna à página anterior
<img width="613" height="289" alt="#back" src="https://github.com/user-attachments/assets/27b869b2-efbd-4139-a1f0-7367231938f2" />

**#add ->** Permite ao usuário adicionar uma URL, seja ela principal ou interna
<img width="613" height="289" alt="#add" src="https://github.com/user-attachments/assets/192f4097-28be-497d-838a-92d3ba2bb777" />

**#showhist ->** Mostra todo o histórico de páginas visitadas, da mais recente à mais antiga
<img width="613" height="289" alt="#showhist" src="https://github.com/user-attachments/assets/bef1089a-e3f4-4e9e-9bed-2a088f19523c" />

**#help ->** Printa uma ajuda como esta, listando a função de cada comando
<img width="613" height="289" alt="#help" src="https://github.com/user-attachments/assets/ed0d857b-12ec-4d55-b66b-5886e778a0ee" />

**#sair ->** Encerra o browser
<img width="613" height="289" alt="#sair" src="https://github.com/user-attachments/assets/7e8a54bd-7bf0-42cf-ac88-f82b069d6487" />


# Como utilizar
1. Baixe o arquivo 'projeto_browser.py' e o arquivo 'urls.txt' deste repositório.
2. Certifique-se de que ambos os arquivos se encontrem no mesmo diretório. Caso contrário, o programa não encontrará o arquivo-texto.
3. Utilize sua IDE favorita e utilize o programa.
