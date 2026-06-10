# Introdução
Utilizando os conceitos de Programação Orientada a Objetos e Estrutura de Dados, nós, o grupo Winx, composto por André, Carlos, Gabriel e Jyan, desenvolvemos um programa em Python que simula um browser, onde se pode pesquisar páginas e suas respectivas páginas internas.

# Imagens
<img width="511" height="195" alt="Captura de tela de 2026-06-10 16-05-18" src="https://github.com/user-attachments/assets/bca56c8a-8e47-4843-8e90-0652dbbefa32" />
<img width="493" height="195" alt="Captura de tela de 2026-06-10 16-04-59" src="https://github.com/user-attachments/assets/d13130e0-35d2-4e21-b956-97a3ad279279" />
<img width="478" height="169" alt="Captura de tela de 2026-06-10 16-04-36" src="https://github.com/user-attachments/assets/5fee217a-fdc9-4c16-a8c7-55cee12e7a80" />
<img width="490" height="205" alt="Captura de tela de 2026-06-10 16-04-14" src="https://github.com/user-attachments/assets/57af25d6-2d3e-497f-8080-7ad681d04127" />
<img width="487" height="216" alt="Captura de tela de 2026-06-10 16-03-45" src="https://github.com/user-attachments/assets/f80f5976-6ebf-445b-9a66-a44b7fd74f21" />
<img width="487" height="216" alt="boas-vindas" src="https://github.com/user-attachments/assets/d65bc5b8-52cb-4615-8bf4-b6765a74856a" />

# Como funciona
O programa utiliza duas estruturas de dados principais: **arvore binária** para armazenar as URLs do arquivo-texto e possibilitar o uso de URLs internas e **lista encadeada** para armazenar num histórico as URLs já pesquisadas. 

Ao iniciar o browser, o arquivo-texto é carregado no programa, separado em listas e para cada URL raiz ou principal é instanciada uma árvore, que por sua vez é armazenada numa lista simples chamada banco_de_dados. No caso de URLs internas, o programa procura qual a sua URL 'mãe' e adiciona a URL interna como filha desta.

A cada pesquisa, a URL home é armazenada no histórico e a URL encontrada agora ocupa o home. Caso a URL encontrada tenha URLs internas, estas são printadas na tela logo após encontrar a URL. Caso a URL não seja encontrada, uma mensagem aparece na tela: 'Página não encontrada :('. O browser também aceita comandos:

**#back ->** Retorna à página anterior
**#add ->** Permite ao usuário adicionar uma URL, seja ela principal ou interna
**#showhist ->** Mostra todo o histórico de páginas visitadas, da mais recente à mais antiga
**#help ->** Printa uma ajuda como esta, listando a função de cada comando
**#sair ->** Encerra o browser

# Como utilizar
1. Baixe o arquivo 'projeto_browser.py' e o arquivo 'urls.txt' deste repositório.
2. Certifique-se de que ambos os arquivos se encontrem no mesmo diretório. Caso contrário, o programa não encontrará o arquivo-texto.
3. Utilize sua IDE favorita e utilize o programa.
