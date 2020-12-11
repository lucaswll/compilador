import sys 
import data

    
class analisadorLexico():

    def lerFonte(self, argv):
        if len(argv[1]) < 5:
            print('O nome do arquivo que deve ser passado como parâmetro tem pelo menos 5 letras (ex.: t.txt)!')
            sys.exit()
        
        elif len(argv[1]) != 0:
            try:
                self.fonte = open(argv[1], 'rb') #[1] pq é o parâmetro que retorna o nome do arquivo digitado como parâmetro (shift+F5) [0] retorna o caminho deste arquivo     
            except FileNotFoundError:
                print('Verifique o nome do arquivo e tente novamente!')
                sys.exit()
            

    def busca(self, dentroDe, chave, valor):
        for dado in dentroDe:
            if dado[chave] == valor:
                return dado
        return False

    def tokensTabSimb(lista):
        for dado in data.tabelaSimbolos:
            if dado['token'] != '':
                lista.append(dado['token'])
        return False
    
    def enumFuncoes(self, coluna, char):
        if (coluna == 0):
            return char in '0123456789'

        elif (coluna == 1):
            return "." == char

        elif (coluna == 2):
            return char in 'eE'

        elif (coluna == 3):
            return "+" == char

        elif (coluna == 4):
            return "-" == char

        elif (coluna == 5):
            return "\"" == char

        elif (coluna == 6):
            return char in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-*/(){}<>=_.;:\ " #nao posso usar caso leia {; caso ler } ele trava no estado 10

        elif (coluna == 7):
            return char in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

        elif (coluna == 8):
            return "_" == char

        elif (coluna == 9):
            return "{" == char

        elif (coluna == 10):
            return "}" == char

        elif (coluna == 11): #eof
            return "eof" == char

        elif (coluna == 12):
            return "<" == char

        elif (coluna == 13):
            return "=" == char

        elif (coluna == 14):
            return ">" == char

        elif (coluna == 15):
            return "*" == char

        elif (coluna == 16):
            return "/" == char

        elif (coluna == 17):
            return "(" == char

        elif (coluna == 18):
            return ")" == char

        elif (coluna == 19):
            return ";" == char 

        elif (coluna == 20): #qqer char fora do alfabeto (inverso da coluna 6) -> p levar pro erro
            return char in '!@#$%&\'~|'

        elif (coluna == 21):
            return " " == char

        elif (coluna == 22):
            return "\n" == char

        elif (coluna == 23):
            return "\t" == char

        elif (coluna == 24):
            return char in "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz+-*/(){<>=_.;:\ " #solução para caso haja "{algo}" -> ser comentario
                                                                                                            #e para não travar no estado 10


    estado = 0 
    palavra = ''
    flagAnaliseIniciada = False
       
    def showTabSimbolos(self):
        print('#'*60)
        print("|{}|".format("Tabela de Símbolos".center(58)))
        print("#"*60)
        print("{}\t\t{}\t\t{}".format(("Lexema").center(10), "Token".center(10), "Tipo".center(10)))   
        print("="*60)
        
        for dado in data.tabelaSimbolos:
            print("{}\t\t{}\t\t{}".format(dado['lexema'].center(10), dado['token'].center(10), dado['tipo'].center(10)))            
            print("-"*60)

    def printPalavra(self, lexema, token, tipo):
        print("{}\t{}\t{}".format(lexema.center(20), token.center(15), tipo.center(25) ))
 
    def insereLexemaTabSimbolos(self, lexema, token, tipo=''):
        if token == 'id':
            if {'lexema': lexema, 'token': token, 'tipo': tipo} in data.tabelaSimbolos:
                data.tabelaSimbolos.remove({'lexema': lexema,'token': token, 'tipo': tipo})
                data.tabelaSimbolos.append({'lexema': lexema,'token': token, 'tipo': tipo})
            else:
                data.tabelaSimbolos.append({'lexema': lexema,'token': token, 'tipo': tipo})
        '''
        if token == 'id' and {'lexema': lexema, 'token': token, 'tipo': tipo} not in data.tabelaSimbolos: 
            data.tabelaSimbolos.append ({'lexema': lexema, 'token': token, 'tipo': ''})
            self.printPalavra(lexema, token, tipo)

        elif token == 'id' and {'lexema': lexema, 'token': token, 'tipo': tipo} in data.tabelaSimbolos:
            print(f'\nO lexema {lexema} já consta na tabela de símbolos:')
            self.printPalavra(lexema, token, tipo)
            print('\n')

        else:
            self.printPalavra(lexema, token, tipo)'''


    palavrasReservadas = []
    tokensTabSimb(palavrasReservadas) #traz tokens que são palavras reservadas

    def verificaEstadoFinal(self, estado):
        estadoFinal = self.busca(data.estadosFinais,'numEstado',estado)
        if estadoFinal != False: 
            if self.palavra in self.palavrasReservadas:
                self.insereLexemaTabSimbolos(self.palavra, self.palavra) #chamando insereLexema eu printo a palavra lida, mesmo que nao tenha sido inserida na tabSimb
                retorno = {'token': self.palavra, 'lexema': self.palavra, 'tipo': ''}
            else:
                self.insereLexemaTabSimbolos(self.palavra, estadoFinal['tokenIdent']) #se != palavrasReservadas, mando pra insereLexema ou printar, ou inserir (caso id)
                retorno = {'token': estadoFinal['tokenIdent'], 'lexema': self.palavra, 'tipo': ''}

            self.estado = 0  
            self.palavra = ''
            return retorno       #retorno True para continuar a analise do arquivo
        return False          #se estadoAtual não for final - retorno o erro


    def lerProximoChar(self):
        self.charAtual = self.fonte.read(1).decode('utf-8')
        #print(self.charAtual)
        
        if self.charAtual == '':
            self.insereLexemaTabSimbolos('EOF', 'EOF')
            return {'token': 'EOF', 'lexema': 'EOF', 'tipo': ''}

        self.countColunas += 1

        possiveisEstados = []
        for i in range(25):
            if not data.tabelaTransicao[self.estado][i] == None:
                possiveisEstados.append({ 'coluna': i, 'estadoDeIda': data.tabelaTransicao[self.estado][i] })
                #por ex, inicia no self.estado = 0 e leio a letra i: possiveisEstados vai ter ({coluna: 0, estadoIda: 1}, {coluna: 4, estadoIda: 19}..)

                #mas como i é uma letra (L), quero APENAS a coluna: 7, estadoIda: 9; (só olhar na tabela de transicao)

        filtroPossivelEstado = []
        for value in possiveisEstados: 
            filtroPossivelEstado.append({'retorno': self.enumFuncoes(value['coluna'], self.charAtual), 'estadoDeIda': value['estadoDeIda'], 'lendo': self.charAtual })
                      
        possuiRetornoTrue = self.busca(filtroPossivelEstado, 'retorno', True) #busco em filtroPossivelEstado e deixo apenas aquele item tem resposta=true

        if possuiRetornoTrue != False: 
            self.palavra += self.charAtual
            
            self.estado = possuiRetornoTrue['estadoDeIda']
            if self.estado == 0: 
                self.palavra = ''

            if self.charAtual in {'\n'}:
                self.countLinhas += 1
                self.countColunas = 0
            
        else:
            self.fonte.seek(-1,1)
            chamaVerificaEstado = self.verificaEstadoFinal(self.estado) # AQUI CHAMO A verificaEstadoFinal e zero o estado!!!!
            #aqui retorno o ERRO LÉXICO
            if chamaVerificaEstado == False: #se estado atual não for final
                print("ERRO: linha:{} & coluna:{} - em {}".format(self.countLinhas, self.countColunas-1, self.palavra))                   
                print(self.busca(data.estadosNaoFinais,'numEstado',self.estado)['msg'])
                
                self.estado = 0
                self.palavra = ''
            return chamaVerificaEstado  

    def tituloMostrarTokens(self):
        print("\n"+"#"*60)
        print("|{}|".format("Lexemas Tokenizados".center(58)))
        print("#"*60)
        print("|{}\t{}\t{}|".format(("Lexema").center(20), "Token".center(15), "Tipo".center(15) ))  
        print("-"*60)

    def tokenizarUmLexema(self):
        stopFlag = False
        while not stopFlag:
            stopFlag = self.lerProximoChar() #vai ser true sempre ao terminar de ler um lexema (quem faz isso é o else do lerProximoChar)
        return stopFlag #retorno o lexema
            
    def tokenizarTudo(self):
        self.tituloMostrarTokens()
        while self.charAtual != '': #enquanto não chego no final do arquivo (meu EOF)
            self.tokenizarUmLexema()

    def iniciaAnalise(self):        
        self.countLinhas = 1
        self.countColunas = 0
        self.charAtual = "whatever"

        self.flagAnaliseIniciada = True

    def wichLinha(self):        #wich's para retorno de linha+coluna do erro léxico
        return self.countLinhas

    def wichColuna(self):
        return self.countColunas - 2
        
                
def main():
    analisador = analisadorLexico()    

    analisador.lerFonte(sys.argv)    

    opcao= ''
    while opcao != '0':
        print('\n')
        print(''.rjust(59,'-'))
        print('|{}|'.format('1 - Tokenizar um lexema;'.center(57)))
        print('|{}|'.format('2 - Tokenizar arquivo completo;'.center(57)))
        print('|{}|'.format('3 - Mostrar tabela de símbolos;'.center(57)))
        print('|{}|'.format('0 - Sair.'.center(57)))
        print(''.rjust(59,'-'))
        
        opcao = str(input('\n\tOpcao desejada:'))
        
        if opcao == '1':
            if not analisador.flagAnaliseIniciada:
                analisador.iniciaAnalise()
                
            analisador.tituloMostrarTokens()
            analisador.tokenizarUmLexema()

        elif opcao == '2':
            if not analisador.flagAnaliseIniciada:
                analisador.iniciaAnalise()

            analisador.tokenizarTudo()

        elif opcao == '3':
            print("-"*60 + "\n"*2)    
            analisador.showTabSimbolos()

        elif opcao == '0':
            sys.exit()

        else:
            print('Opcão incorreta!!')

    

if __name__ == "__main__":
    main()   
