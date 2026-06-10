'''Banco das árvores de URL's'''
banco_de_dados = []

class NoBinario:
    '''Classe Nó Binário -> utilizada para cadastrar os sites no banco de dados 
    e possibilitar a adição de URLs internas'''

    def __init__(self, carga = None, esquerda = None, direita = None):
        '''Método construtor da classe'''
        self.carga = carga
        self.esquerda = esquerda
        self.direita = direita

    def adicionar_filho(self, filho):
        '''Percorre os ponteiros esquerda e direita e adiciona uma URL interna ao nó URL.
        Caso estejam ocupados, printa uma mensagem de erro'''
        if self.esquerda is None:
            self.esquerda = NoBinario(filho)
        elif self.direita is None:
            self.direita = NoBinario(filho)
        else:
            print('Não é possível adicionar mais filhos')

    def buscar_chave(self, chave: str):
        '''Procura uma URL em si mesma e nas URLs filhas.
        Retorna uma string se encontrar, e se não encontrar, retorna None.'''
        if self.carga == chave:
            return self.carga
        
        resultado = None

        if self.esquerda is not None:
            resultado = self.esquerda.buscar_chave(chave)
        if resultado is None and self.direita is not None:
            resultado = self.direita.buscar_chave(chave)

        return resultado
        
    def buscar_no(self, chave: str):
        '''Procura uma URL em si mesma e nas URLs filhas.
        Retorna o objeto se encontrar, e se não encontrar, retorna None.'''
        if self.carga == chave:
            return self

        resultado = None

        if self.esquerda is not None:
            resultado = self.esquerda.buscar_no(chave)
        
        if resultado is None and self.direita is not None:
            resultado = self.direita.buscar_no(chave)

        return resultado

class ArvoreBinaria:
    '''Classe Árvore Binária -> serve para instanciar uma árvore binária para cada URL principal ou raiz'''
    def __init__(self, url_raiz):
        '''Método construtor da classe'''
        self.raiz = NoBinario(url_raiz)

class NoLista:
    '''Classe Nó Lista -> serve para criar a lista encadeada do histórico'''
    def __init__(self, carga, ant: 'NoLista' = None, prox: 'NoLista' = None):
        '''Método construtor da classe'''
        self.carga = carga
        self.ant = ant
        self.prox = prox

class ListaEncadeada:
    '''Classe Lista Encadeada -> lista encadeada que serve para armazenar as URLs pesquisadas'''
    def __init__(self, cabeca: 'NoLista' = None, cauda: 'NoLista' = None):
        '''Método construtor da classe'''
        self.cabeca = cabeca
        self.cauda = cauda

    def __repr__(self):
        '''Possibilita printar a lista'''
        if self.cabeca is None:
            return '[ ]'
        
        historico = ''
        atual = self.cabeca

        while atual is not None:
            historico += f'[{atual.carga}]'
            atual = atual.prox

        return historico

    def imprimir_lista(self, home):
        '''Imprime uma lista de todas as páginas visitadas, desde a mais recente até a primeira'''
        print('\nHistórico de páginas visitadas: ')
        print('-', home)
        atual = self.cauda
        while atual is not None:
            print('-', str(atual.carga))
            atual = atual.ant

    def inserir_elemento(self, elemento):
        '''Insere uma URL no histórico'''
        novo: 'NoLista' = NoLista(elemento)
        if self.cabeca is None:
            self.cabeca = self.cauda = novo
        else:
            novo.ant = self.cauda
            novo.ant.prox = novo
            self.cauda = novo
    
    def remover_do_inicio(self):
        '''Remove um elemento do início'''
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cabeca = self.cabeca.prox
            self.cabeca.ant = None

    def remover_do_final(self):
        '''Remove um elemento do final. Utilizado no #back'''
        if self.cabeca == self.cauda:
            self.cabeca = self.cauda = None
        else:
            self.cauda = self.cauda.ant
            self.cauda.prox = None

    def retornar_anterior(self):
        '''Retorna o último elemento da lista. Utilizado no #back'''
        return self.cauda

    def is_empty(self):
        '''Verifica se a lista está vazia'''
        return self.cabeca is None
    

class Interface():
    '''Classe Interface -> onde o browser funciona na prática'''
    def __init__(self):
        '''Método construtor da classe'''
        self.historico: 'ListaEncadeada' = ListaEncadeada()
        self.home: 'NoLista' = NoLista('')
        self.barra_de_busca = ''

    def _encontrar_no(self, objeto, chave):
        '''Chama a função buscar_no() de um nó binário'''
        return objeto.buscar_no(chave)

    def _carregar_urls(self):
        '''Carrega as urls do arquivo-texto e as armazena, instanciando as URLs e colocando as no banco de dados'''
        try:
            with open('urls.txt', 'r') as arq:
                urls = arq.read().splitlines()
                
                for url in urls:
                    if url.count('/') == 0:
                        site = ArvoreBinaria(url)
                        banco_de_dados.append(site)
                    else:
                        self._carregar_url_filha(url)
        except:
            raise FileNotFoundError('Arquivo de texto não encontrado :(')

    def _carregar_url_filha(self, url_filha):
        '''Identifica URLs internas e adiciona-as as suas respesctivas URLs'''
        partes = url_filha.rsplit('/', 1)
        url_mae = partes[0]

        for objeto in banco_de_dados:
            link = self._encontrar_no(objeto.raiz, url_mae)
            if link is not None:
                link.adicionar_filho(url_filha)

    def _exibir(self):
        '''Exibe o cabeçalho do browser'''
        print(f'\nHistórico de visitas: {self.historico}')
        print(f'Home: [{self.home.carga}]')
        print('Digite a url desejada ou #help para obter ajuda:')
        self.barra_de_busca = input('url: ')

    def _buscar(self, url: str):
        '''Verifica se a URL pesquisada existe'''
        for objeto in banco_de_dados:
            filho = objeto.raiz.buscar_chave(url)
            if filho is not None:
                return True
        if self._urls_internas(url):
            return True
                
    def _urls_internas(self, url):
        '''Permite que o usuário digite URLs internas começando da barra,
        sem precisar digitar o endereço inteiro'''
        if url.startswith('/'):
            for objeto in banco_de_dados:
                link_mae = self._encontrar_no(objeto.raiz, self.home.carga)
                if link_mae is not None:
                    if link_mae.esquerda is not None:
                        string = self.home.carga + url
                        if link_mae.esquerda.carga == string:
                            return True
                    if link_mae.direita is not None:
                        string = self.home.carga + url
                        if link_mae.direita.carga == string:
                            return True

    def _pagina_encontrada(self):
        '''Tendo encontrado a URL pesquisada, verifica se ela é interna, se é a primeira pesquisada
        e a adiciona ao self.home'''
        if self._urls_internas(self.barra_de_busca) == True:
            string = self.home.carga + self.barra_de_busca
            self.historico.inserir_elemento(self.home.carga)
            self.home.carga = string
        elif self.home.carga == '':
            self.home.carga = self.barra_de_busca
        else:
            self.historico.inserir_elemento(self.home.carga)
            self.home.carga = self.barra_de_busca
        print('\nPágina encontrada!')

    def _mostrar_filhos(self):
        '''Permite que as URLs internas de uma URL pesquisada sejam printadas no browser'''
        for objeto in banco_de_dados:
            link_mae = self._encontrar_no(objeto.raiz, self.home.carga)
            if link_mae is not None:
                if link_mae.esquerda is not None and link_mae.direita is None:
                    string = link_mae.esquerda.carga
                    partes = string.rsplit('/')
                    nova_string = '/' + partes[-1]

                    print('\nLinks disponíveis: ')
                    print(f'{nova_string}')

                elif link_mae.esquerda is None and link_mae.direita is not None:
                    string = link_mae.direita.carga
                    partes = string.rsplit('/')
                    nova_string = '/' + partes[-1]

                    print('\nLinks disponíveis: ')
                    print(f'{nova_string}')

                elif link_mae.esquerda is not None and link_mae.direita is not None:
                    string1 = link_mae.esquerda.carga
                    partes1 = string1.rsplit('/')
                    nova_string1 = '/' + partes1[-1]

                    string2 = link_mae.direita.carga
                    partes2 = string2.rsplit('/')
                    nova_string2 = '/' + partes2[-1]

                    print('\nLinks disponíveis: ')
                    print(f'{nova_string1}')
                    print(f'{nova_string2}')

    def _back(self):
        '''#back -> permite que o usuário volte uma URL'''
        if self.historico.is_empty():
            print('\nO histórico está vazio, não é possível voltar mais :/')
        else:
            print('\nVoltando à página anterior...')
            self.home = self.historico.retornar_anterior()
            self.historico.remover_do_final()
            self._mostrar_filhos()

    def _add(self):
        '''#add -> permite que o usuário adicione URLs e URLs internas'''
        tipo = input('\nQual tipo de URL deseja cadastrar? (raiz/interna) ')
        if tipo == 'raiz':
            url = input('\nDigite a URL que deseja cadastrar: ')

            for objeto in banco_de_dados:
                if objeto.raiz.carga == url:
                    print('\nEsta URL já foi cadastrada :)')
                    return
        
            with open('urls.txt', 'a') as arq:
                arq.write('\n' + url)
        
            site = ArvoreBinaria(url)
            banco_de_dados.append(site)

            print('\nURL cadastrada com sucesso!')
            ask = input('Deseja adicionar um link interno a esta URL? (sim/nao) ')

            if ask == 'sim':
                link_interno = url + input('\nDigite o link interno que deseja cadastrar (ex: /tsi): ')

                with open('urls.txt', 'a') as arq:
                    arq.write('\n' + link_interno)
                site.raiz.adicionar_filho(link_interno)

                print('\nURL interna cadastrada com sucesso!')
                return

        elif tipo == 'interna':
            url_raiz = input('\nPara qual URL raiz deseja adicionar um link interno? ')
            url_filha = url_raiz + input('\nDigite o link interno que deseja cadastrar (ex: /tsi): ')

            for objeto in banco_de_dados:
                link_mae = self._encontrar_no(objeto.raiz, url_raiz)
                if link_mae is not None:
                    link_mae.adicionar_filho(url_filha)
        else:
            print('\nEste tipo não é válido :/')

    def _help(self):
        '''#help -> printa os comandos disponíveis do browser'''
        print('\nComandos disponíveis:')
        print('#back -> Retorna à última página visitada')
        print('#add -> Adiciona uma nova URL')
        print('#help -> Exibe esta ajuda')
        print('#showhist -> Imprime o histórico de páginas visitadas')
        print('#sair -> Encerra o browser')

    def _sair(self):
        '''#sair -> encerra o browser'''
        print('Encerrando browser...')

    def _showhist(self):
        '''#showhist -> utiliza a função imprimir_lista() do historico para
        printar todas as páginas visitadas'''
        self.historico.imprimir_lista(self.home.carga)

    def _pagina_nao_encontrada(self):
        '''Printa uma mensagem de erro caso a página não seja encontrada'''
        print('\nPágina não encontrada :(')

    def _executar(self):
        '''Chama os métodos necessários para instanciação do browser'''
        self._carregar_urls()
        print()
        print("╔══════════════════════════════════════════╗")
        print("║   Olá! Seja bem-vindo ao                 ║")
        print("║   browser! URLs carregadas...            ║")
        print("╚══════════════════════════════════════════╝")
        while True:
            self._exibir()
            if self._buscar(self.barra_de_busca) == True:
                self._pagina_encontrada()
                self._mostrar_filhos()
            elif self.barra_de_busca == '#back':
                self._back()
            elif self.barra_de_busca == '#add':
                self._add()
            elif self.barra_de_busca == '#help':
                self._help()
            elif self.barra_de_busca == '#sair':
                self._sair()
                break
            elif self.barra_de_busca == '#showhist':
                self._showhist()
            else:
                self._pagina_nao_encontrada()

def main():
    '''Cria o objeto pesquisa e chama o método executar()'''
    pesquisa = Interface()
    pesquisa._executar()

if __name__ == '__main__':
    main()
