import sys
import AnalisadorLexico as AL
import data2

class Pilha():
    pilha= []

    def topoDaPilha(self):
        return self.pilha[len(self.pilha)-1] 
    
    def retiraErroTopoPilha(self, n):
        for i in range(0, n):
            self.pilha.pop(i-n)
            
        #return self.pilha[len(self.pilha)-2] 
    

    def empilha(self, valor):
        self.pilha.append(valor)

    '''def desempilha(self):
        self.pilha.pop()'''

    def pilhaVazia(self):
        return len(self.pilha) == 0

    def mostraReducao(self, n): #printar sempre que aparecer um reduce (R?)
        ladoDireito = ''

        for i in range(0, n):
            if type(self.pilha[i-n]) is str: #i-n pois vai pegar o final da pilha até chegar no primeiro valor passado no reduce pra imprimir o lado direito
                #print((i-n), self.pilha[i-n])
                ladoDireito += self.pilha[i-n] + ' '
                #o mostrar vai retornar o lado esquerdo da producao e depois eu desempilho
            if not self.pilhaVazia(): #se a pilha não estiver vazia (estiver no ACCEPT da tabela de acao), desempilho esse valor da pilha
                self.pilha.pop(i-n)
        
        return ladoDireito

    def printPilha(self):
        print(self.pilha)


class analisadorSintatico():
    
    def iniciaAnalise(self):

        #iniciando o léxico
        analisadorLexico = AL.analisadorLexico()
        analisadorLexico.lerFonte(sys.argv)
        analisadorLexico.iniciaAnalise()

        #startando a pilha
        pilha = Pilha()
        pilha.empilha(0) #iniciando a pilha c valor 0 (por isso o -1 no topoDaPilha)

        #seja a o primeiro simbolo do programa (w$) = inicio
        tokenEnviado = analisadorLexico.tokenizarUmLexema()
        #print(tokenEnviado)
        
        while(True):
            #seja s o estado no topo da pilha (inicialmente 0
            s = pilha.topoDaPilha()
            wichAcao = data2.tabelaAcao[s][data2.simbolosTerminais[tokenEnviado['token']]] #qual a ação que ta na tabelaDeAcao? (lista de chave/valor)
            #pega a linha como (s) e a coluna como o lexema (tokenEnviado)
            #ou seja, incialmente, s=0 e lexema=inicio -> wichAcao = S2 (shift 2)

            if(wichAcao[0] == 'S'):
                pilha.empilha(tokenEnviado['lexema']) #empilhando o lexema do tokenEnviado (pq? pois eu busco uma string para printar la no reduce depois)
                # pra consertar isso no programa dado, eu desempilho o dobro do tamanho da producao do lado direito - la nas producoesEnumeradas (valores tao x2)
                pilha.empilha(int(wichAcao[1:])) #empilha t na pilha (por ex. empilha o 2 de S2)
                tokenEnviado = analisadorLexico.tokenizarUmLexema() #seja a o próximo simbolo da entrada
                #aqui ele ja me retorna o erro léxico, caso haja

                #pilha.printPilha()

            elif(wichAcao[0] == 'R'):
                numeroDaProducao = data2.producoesEnumeradas[int(wichAcao[1:])] #wichAcao[1:] pega o numero da producao que vou reduzir. Ex: 4, se R4
                #busca nas producoesEnumeradas o valor 4 trazendo o duo [tamanhoDoLadoDireito, ladoEsquerdo]
                print('{} => '.format(numeroDaProducao[1]), end = '') #print do lado esquerdo
                
                print(pilha.mostraReducao(numeroDaProducao[0])) #chamo mostraReducao passando como parametro o tamanhoDoLadoDireito da producao
                
                topo = pilha.topoDaPilha()
                #print(topo)
                pilha.empilha(numeroDaProducao[1]) #empilha lado esquerdo da producao pra quando varrer, utilizar ele pra compor o ladoDireito  (pra acompanhar o dobro de elementos colocados no if do shift)
                pilha.empilha(data2.tabelaTransicao[topo][data2.simbolosNaoTerminais[numeroDaProducao[1]]]) #empilha GOTO (o estado de ida a partir)
                #do estado atual (topo da pilha) e do lado esquerdo da producao

                #pilha.printPilha()

            elif(wichAcao == 'ACC'):

                print("P' => P")
                print('\n'+'Gramática aceita!')
                break

            else:
                print('-'*20)
                print("Erro sintático vindo de {} -> {}".format((wichAcao), data2.errors[wichAcao]))
                print("Linha: {}".format(analisadorLexico.wichLinha()))
                print("Coluna: {}".format(analisadorLexico.wichColuna()))
                print('-'*20)

                
                #pilha.printPilha()
                
                #aux = data2.producoesEnumeradas[topo][0]# desempilhar 4 valores da pilha e continuar o programa                
                #print(int(aux/2))
                
                #pilha.retiraErroTopoPilha(int(aux/2))
                
                break #
                

def main():
    anSintatico = analisadorSintatico()
    anSintatico.iniciaAnalise()

if __name__ == "__main__":
    main()
