import sys #me permite encerrar o programa 'sys.exit()', e passar o caminho do arquivo de leitura 'sys.argv'

class testeLexico():
    fonte = sys.argv[1]

    def lerFonte(self, argv):
        self.fonte = open(argv[1], 'rb')

        if len(argv[1]) == 0:
            print('Parâmetro em branco!')
            sys.exit()

    estadosFinais = [
        {'numEstado': 1, 'tokenIdent': 'Num'},
        {'numEstado': 2, 'tokenIdent': 'id'},
        {'numEstado': 3, 'tokenIdent': 'PT_V'}
    ]

    estadosNaoFinais = [
        {'numEstado': 0, 'msg': 'Sentença iniciando com espaço.'}
    ]

    tabelaSimbolos = [
        {'lexema': 'inicio', 'token': 'inicio', 'tipo': ''},
        {'lexema': 'varinicio', 'token': 'varinicio', 'tipo': ''},
        {'lexema': 'varfim', 'token': 'varfim','tipo': ''},
        {'lexema': 'fim', 'token': 'fim', 'tipo': ''},
        {'lexema': 'inteiro', 'token': 'inteiro', 'tipo': ''},
        {'lexema': 'literal', 'token': 'literal', 'tipo': ''}
    ]


    def busca(self, dentroDe, chave, valor):
        for dado in dentroDe:
            if dado[chave] == valor:
                return dado
        return False

    # ----------- Implementando a tabela de transição ----------------
    #para identificar as 24 'colunas' da tabelaTransicao (que vao de 0 à 23) // ou seja:
    #se leu digito retorna true caso coluna 0 // se leu . retorna true caso coluna 1 [...]    
    def enumFuncoes2(self, coluna, char):
        if (coluna == 0):
                return char in '0123456789'

        elif (coluna == 1):
                return char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
                
        elif (coluna == 2):
                return "_" == char

        elif (coluna == 3):
                return " " == char

        elif (coluna == 4):
                return ";" == char

        elif (coluna == 5):
                return "\n" == char

    tabelaTransicao = [
        [1,2,None,0,3,0],
        [1,None,None,None,None,None],
        [2,2,2,None,None,None],
        [None,None,None,None,None,None]
    ]

    #começo no estado 0 com palavra vazia..
    estado = 0
    palavra = ''

    def estadoInicial(self, estado): 
        self.estado = estado
        if estado == 0:
            self.palavra = ''

                     #o self vem como 1o param. em todas funcoes de uma classe: padrão no python
    def showTabSimbolos(self): #o self vem como 1o param. em todas funcoes de uma classe: padrão no python
        print("-"*60)
        print("{}\t\t{}\t\t{}".format(("Lexema").center(10), "Token".center(1), "Tipo" ))   
        print("-"*60)
        
        for data in self.tabelaSimbolos:
            print("{}\t\t{}\t\t{}".format(data['lexema'].center(10),data['token'].center(1),data['tipo']))
            
            print("-"*60)

    def insereLexemaTabSimbolos(self, lexema, token, tipo=''):
        if token == 'id' and {'lexema': lexema, 'token': token, 'tipo': tipo} not in self.tabelaSimbolos: #se token for id e não tiver na tabela ainda:
            self.tabelaSimbolos.append ({'lexema': lexema, 'token': token, 'tipo': ''}) #insiro na tab o token (passado como parametro)

        print("|{}|{}|{}|".format(token.center(15),lexema.center(30),tipo.center(10))) #inserindo ou não, eu printo (o NÃO é caso ja esteja na tabela)


    palavrasReservadas = ['inicio','varinicio','varfim','fim','literal','inteiro']

    def verificaEstadoFinal(self, estado): 
        estadoFinal = self.busca(self.estadosFinais,'numEstado',estado)
        if estadoFinal != False: 
            if self.palavra in self.palavrasReservadas: #INICIO JA ESTA NA TAB SIMBOLOS (PORQUE É RESERVADA).
                self.insereLexemaTabSimbolos(self.palavra, self.palavra) #mas chamo a funcao inserelexema, mesmo que ela não va inserir na tabela
                                                                         #pq fará um print com esse lexema, token e tipo que foram passados como parametro
            else: #se != palavrasReservadas, mando pra insereLexema ou printar, ou inserir (caso id)
                self.insereLexemaTabSimbolos(self.palavra, estadoFinal['tokenIdent'])

            self.palavra = '' #resetando palavra
            self.estado = 0   #volto pra estado inicial caso possuiRetornoTrue só retorne False
                              #(ou seja, não existe nenhuma coluna valida de ida, para o simbolo lido)
            
            return True       #retorno True para resetar o analisaArquivo
        return False          #se estadoAtual não for final - retorno o erro


    def lerProximoChar(self):
        self.charAtual = self.fonte.read(1).decode('utf-8') #coloca atual caractere lido (na 1a vez, é o primeiro char 'i') em formato utf-8 na variavel char
#        print(self.charAtual) #inicialmente estou no estado 0 e leio charAtual = i . Pra qual estado vou agora?
#        print(len(self.tabelaTransicao[self.estado])) #retorna qtde de colunas da tabTransicao (4)

        if self.charAtual == '':
            return True      #pra retornar pro primeiro while do analisaArquivo e encerrar..
        
        self.countChars += 1 #conforme caminho no arquivo (antes do \n) avanço uma coluna

        possiveisEstados = []
        for i in range(6):   #andando nas 4 colunas da tab de transicao                                  #                    i     i     i     i
            if not self.tabelaTransicao[self.estado][i] == None: #percorrerei tab: (0,0) (0,1) (0,2) (0,3) -> pois estado aqui inicia valendo 0; i vai de 0 a 3
                                                                 #estadoDeIda são:   1     2    None   0
                                                                 #ou seja, possui 3 estados a serem validados no filtro
                possiveisEstados.append({ 'coluna': i, 'estadoDeIda': self.tabelaTransicao[self.estado][i] })
                #como nao quero os None, possiveisEstados vai receber: = [
                #{'coluna': 0, 'estadoDeIda': 1},
                #{'coluna': 1, 'estadoDeIda': 2},
                #{'coluna': 3, 'estadoDeIda': 0},]
                #mas como o primeiro char = i, quero apenas coluna 1, estadoDeIda 2                

        filtroPossivelEstado2 = []  #daí vou percorrer a lista acima para pegar a coluna e o respectivo estadoDeIda
        for value in possiveisEstados:   #ou seja, coluna = [0,1,3] // estadoDeIda = [1, 2, 0]                                
            #filtroPossivelEstado.append({ 'retorno': self.enumFuncoes[value['coluna']](self.charAtual), 'estado': value['estadoDeIda'], 'charAtual': self.charAtual })
            #na 1a iteração seria:    'retorno': enumFuncoes 0 (i) = digito(i) = false             'estado': 1
            #                         'retorno': enumFuncoes 1 (i) = letra(i)  = true              'estado': 2  (QUERO ESSA)
            #                         'retorno': enumFuncoes 3 (i) = espaco(i) = false             'estado': 0
            filtroPossivelEstado2.append({ 'retorno': self.enumFuncoes2(value['coluna'], self.charAtual), 'estadoDeIda': value['estadoDeIda'], 'lendo': self.charAtual })
            #retorno recebe True se ao chamar as enumFuncoes passando colunas de possiveisEstados charAtual, alguma delas retornar True
            #se uma delas retorna True, eu salvo essa respectiva coluna e o respectivo estadoDeIda em filtroPossivelEstado
            
        #como possiveisEstados são 3, aqui tb terei 3.. pq faço o for mediante ele
        #filtroPossivelEstado2 vai receber: =[
        #{false, 1, i},     {true, 2, i},    {false, 0, i} ]
#       print(filtroPossivelEstado2[0], filtroPossivelEstado2[1], filtroPossivelEstado2[2]) #OK, bateu, pq retornou true no estado 2, que e pra onde devo ir

        #é possível que não retorne nenhum true (por ex. para os estadoAtual = 16~23, todas colunas retornam None       
        possuiRetornoTrue = self.busca(filtroPossivelEstado2, 'retorno', True) # o retorno disso me devolve o item "{'retorno': ,'estadoDeIda': ,'lendo': }" da lista
                                                                          #mudaEstadoAtual que retornou True
#        print(possuiRetornoTrue) #pro estado 0, retorna apenas o possivel estado filtrado: {'retorno': True, 'estadoDeIda': 2, 'lendo': 'i'}

        if possuiRetornoTrue != False: #quer dizer que sei proximo estado (estadoDeIda)
            self.palavra += self.charAtual #palavra inicialmente vazia (pq estava em estado 0) é concatenada com charAtual

            self.estado = possuiRetornoTrue['estadoDeIda'] #meu estado recebe o estadoDeIda
            if self.estado == 0: #se ele for o 0 (to no incial, então minha palavra volta a ser vazia!)
                self.palavra = ''

            if self.charAtual == '\n': #se o charAtual for o salto de linha, zero meu contador de coluna e somo uma no das linhas
                self.countLinhas +=1
                self.countChars = 0

        else: #vindo pra ca, possuiRetornoTrue = False; ou seja,terminei de ler uma palavra. Sei disso pq sempre que chegar num \n, possuiRetornoTrue <- False
            #volto 1 caractere para que não de estado de erro, pois e.g. estando no estado 9 lendo ;, seria none, e ele pularia o ;. Eu volto pra contar o ;
                #a partir do estado 0
            #seek(offset, from_what): from_what = 1 indica a posição atual no arquivo. offset = -1: define que a nova posição no arquivo é a anterior da posição atual
            self.fonte.seek(-1,1)
            chamaVerificaEstado = self.verificaEstadoFinal(self.estado) # AQUI CHAMO A verificaEstadoFinal e zero o estado!!!!
            
            if chamaVerificaEstado == False: #se estado atual não for final
                self.insereLexemaTabSimbolos("ERRO","Erro encontrado")
                print("Erro na linha {} coluna {} - {}\nMensagem: {}".format(
                    self.countLinhas,
                    self.countChars-1,
                    self.palavra,
                    self.busca(self.estadosNaoFinais,'numEstado',self.estado)['msg']))
                sys.exit()
            return True #quando termina de ler INICIO, ele le \n, verificaEstadoFinal=False mas o estado ainda é 9, então ele nao entra no if, pra mostrar erro
                        #vem p ca e retorna True pra condicao_de_parada ((((((CONEXAO DESSA))))))))


    def mostrar_cabecalho_de_tokens_lidos(self):
        print("#"*60)
        print("|{}|".format("Lexemas Toquenizados".center(58)))
        print("#"*60)
        print("{}\t{}\t{}".format(("Lexema").center(20), "Token".center(15), "Tipo".center(15) ))  
        print("-"*60)

    def analisaArquivo(self):
        while self.charAtual != "": #enquanto não chego no final do arquivo (como se fosse meu EOF)
            condicao_de_parada = False
            while condicao_de_parada == False:
                condicao_de_parada = self.lerProximoChar()#((((COM ESSA))) como condicao_de_parada agora é True, não vou chamar o lerProximoChar()
                #print(condicao_de_parada)  #voltou para o primeiro While.. meu char é ''? Sim: retorno para o chamador (main)// Não: faço condica_de_parada = False de novo
#voltando pro primeiro while,            

    def inicializaAnalise(self):
        self.countLinhas = 1
        self.countChars = 0
        self.charAtual = "qualquerCoisa"  #pq vou zerar a palavra msm

        self.mostrar_cabecalho_de_tokens_lidos()
        self.analiseInicializada = True
    
def main():
    analisador = testeLexico()       #construindo meu analisador

    analisador.lerFonte(sys.argv)    #lendo arquivo fonte (passando caminho deste arquivo para encontrar o fonte)

    print('\n')
    analisador.showTabSimbolos()  #mostrar a tabela de simbolos só com as palavras reservadas
    print('\n'*2+'.'*60+'\n'*2)
    analisador.inicializaAnalise()
    analisador.analisaArquivo() #faço a análise do arquivo
    print("-"*60)
    print('\n'*2+'.'*60+'\n'*2)
    analisador.showTabSimbolos()  #mostrar a tabela de simbolos depois de inseridos os IDs

if __name__ == "__main__":
    main()
    
        
