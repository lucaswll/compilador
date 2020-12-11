import sys
import AnalisadorLexico as AL
import data
import data2


def busca(lista, chave, valor):
    for item in lista:
        if item[chave] == valor:
            return item
    return False

                    #classe instanciada, atributo que quero pegar dela
def chamaRegraSemantica(instancia, nomeRegra):
    return getattr(instancia, nomeRegra)
    #retorno qual a função que tem como nome, essa regra. Por exemplo, se fiz reduce R25, usarei a regra semantica regra25
    #esse retorno traz o que a funcao regra25 faz..

def itsInt(s):
    try:
        x = int(s)
        return True
    except ValueError:
        return False
    

class Pilha():
    pilha= []

    def topoDaPilha(self):
        return self.pilha[len(self.pilha)-1] 
    
    def retiraErroTopoPilha(self, n):
        for i in range(0, n):
            self.pilha.pop(i-n)    

    def empilha(self, valor):
        self.pilha.append(valor)

    '''def desempilha(self):
        self.pilha.pop()'''

    def pilhaVazia(self):
        return len(self.pilha) == 0

    def mostraReducao(self, n): #printar sempre que aparecer um reduce (R?)
        ladoDireito = ''

        for i in range(0, n):
            if type(self.pilha[i-n]) is str:                 
                ladoDireito += self.pilha[i-n] + ' '
                
            if not self.pilhaVazia(): 
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

        #iniciando semantico
        analisadorSemantico = AnalisadorSemantico(analisadorLexico)

        #startando a pilha
        pilha = Pilha()
        pilha.empilha(0)

        #seja a o primeiro simbolo do programa (w$) = inicio
        tokenEnviado = analisadorLexico.tokenizarUmLexema()
        
        while(True):
            s = pilha.topoDaPilha()
            wichAcao = data2.tabelaAcao[s][data2.simbolosTerminais[tokenEnviado['token']]]
            

            if(wichAcao[0] == 'S'):
                pilha.empilha(tokenEnviado['lexema'])            
                pilha.empilha(int(wichAcao[1:])) 
                tokenEnviado = analisadorLexico.tokenizarUmLexema()

            elif(wichAcao[0] == 'R'):
                numeroDaProducao = data2.producoesEnumeradas[int(wichAcao[1:])]
                producaoToPrint = '{} => '.format(numeroDaProducao[1]) + pilha.mostraReducao(numeroDaProducao[0]) #salvo o reduce
                
                print(producaoToPrint) #print do reduce
                
                topo = pilha.topoDaPilha()
                
                pilha.empilha(numeroDaProducao[1])
                pilha.empilha(data2.tabelaTransicao[topo][data2.simbolosNaoTerminais[numeroDaProducao[1]]])
                ########SEMANTICO######
                if numeroDaProducao[2]: #se houver regra semantica associada
                    numeroDaRegra = wichAcao[1:] #pego qual regra to reduzindo, e se passou pelo if, é o mesmo nº da regra semantica (se R2, o wichAcao[1:] pega o 2)
                    print("Regra semântica associada -> Regra {}\n".format(numeroDaRegra))
                    executaRegra = chamaRegraSemantica(analisadorSemantico, 'regra'+numeroDaRegra)(producaoToPrint)
                    #passo pra funcao minha instancia do analisadorSemantico e o numero da regra semantica respectiva à redução realizada
                    #como as regras semanticas precisam das produções, passo também a produção que ta sendo reduzida (é o segundo param de todas as regrasX)
                
            elif(wichAcao == 'ACC'):
                print("P' => P")
                print('\n'+'Gramática aceita!')
                ########SEMANTICO######
                analisadorSemantico.closeAndGetC() #fecha a chave final do código e insere os temporarios utilizados..
                                                   #salto as 7 primeiras linhas pra por os temps, pois contem a parte fixa do programa (include, main..)
                print("\nNenhuma regra semântica associada, apenas finaliza escrita no arquivo .c!\n")
                print("Arquivo gerado: 'programa.c'\n") #nome do arquivo .c gerado               
                break

            else:
                print('-'*20)
                print("Erro sintático vindo de {} -> {}".format((wichAcao), data2.errors[wichAcao]))
                print("Linha: {}".format(analisadorLexico.wichLinha()))
                print("Coluna: {}".format(analisadorLexico.wichColuna()))
                print('-'*20)
            
                break


class AnalisadorSemantico():
    #atributos temporarios para escrita das regras
    tipoTemp = '' #pra conter o tipo dos nao terminais
    exprTemp = '' #pra conter o lexema dos nao terminais
    oprdTemp = [] 
    argTemp = ''    
    ldTemp = ''
    

    tCount = 0
    tVar = []

    def __init__(self, analisadorLexico):#executado instantaneamente ao instanciar o semantico
        self.analisadorLexico= analisadorLexico
        self.programaC = open('programa.c', 'w')
        self.programaC.write('#include <stdio.h>\n\n')
        self.programaC.write('typedef char literal[256];\n\n')
        self.programaC.write('void main(void)\n')
        self.programaC.write('{\n')
        self.programaC.write('  /*----Variaveis temporarias----*/\n')
        #eu poderia inserir aqui as variaveis T temporarias, mas elas vao aparecer conforme são usadas pelo semantico (regras 18 e 25)

    def closeAndGetC(self):
        self.programaC.write('}') #fecha a última chave do main
        self.programaC.close() #fecha o arquivo

        vsTemp = ''
        for item in self.tVar: #sao os T utilizados nas regras que usam Tx (18 e 25)
            vsTemp = vsTemp + '  {} {};\n'.format(item['tipo'], item['lexema'])
        vsTemp = vsTemp + '  /*-------------------------*/\n'

        programaC = open('programa.c', 'r') #read no arquivo antes de inserir as varTemp
        programaCLido = programaC.readlines()   

        #valor 7 pra pular as 7 primeiras linhas do programa (colocar os T temporarios no lugar certo)
        programaCLido.insert(7, vsTemp)

        #reescreve o programa com a declaração dos T temp
        programaC = open('programa.c', 'w')
        programaCLido = "".join(programaCLido)
        programaC.write(programaCLido)
        programaC.close()
    

    def regra5(self, reducao = ''):
        self.programaC.write("\n\n\n") #3 linhas brancas

    def regra6(self, producao = ''):
        id_lexema = producao.split()[2] #D(0) ->(1) id(2) TIPO(3)
        token = busca(data.tabelaSimbolos, 'lexema', id_lexema)
        self.analisadorLexico.insereLexemaTabSimbolos(token['lexema'], token['token'], self.tipoTemp) #inserindo lexema, token e id para os NAO TERMINAIS
        self.programaC.write("  {} {};\n".format(self.tipoTemp, id_lexema)) #o tipoTemp vai ser int, real ou literal, depende se chamou a regra 7,8 ou 9 por ultimo


    def regra7(self, producao = ''): #TIPO(0) ->(1) inteiro(2)
        self.tipoTemp = producao.split()[2]

    def regra8(self, producao = ''): #TIPO(0) ->(1) real(2)
        self.tipoTemp = 'double'

    def regra9(self, producao = ''): #TIPO(0) ->(1) literal(2)
        self.tipoTemp = producao.split()[2]

    def regra11(self, producao = ''): #ES(0) ->(1) leia(2) id(3) ;(4)
        id_lexema = producao.split()[3]
        token = busca(data.tabelaSimbolos, 'lexema', id_lexema)

        if token['tipo'] != '': #se o tipo do id ta declarado (ou seja, passou ok pela regra 6)
            if token['tipo'] == 'literal':
                self.programaC.write("  scanf(\"%s\", {});\n".format(token['lexema']))
            if token['tipo'] == 'int':
                self.programaC.write("  scanf(\"%d\", &{});\n".format(token['lexema']))
            if token['tipo'] == 'real':
                self.programaC.write("  scanf(\"%lf\", &{});\n".format(token['lexema']))
        else:
            self.mostraErro("Variável não declarada")

    def regra12(self, producao = ''): #ES(0) ->(1) escreva(2) ARG(3) ;(4)
        # self.programaC.write("printf({});\n".format(self.argTemp))
        token = busca(data.tabelaSimbolos, 'lexema', self.argTemp) #argTemp baseia-se nas regras 13,14 ou 15. Depende do tipo do ARG recebido (argTemp = literal, num ou id)
        if token:
            if token['tipo'] == 'double':
                self.programaC.write("  printf(\"%lf\",{});\n".format(self.argTemp))
            elif token['tipo'] == 'int':
                self.programaC.write("  printf(\"%d\",{});\n".format(self.argTemp))
            else:
                self.programaC.write("  printf(\"%s\",{});\n".format(self.argTemp))
        else:
            self.programaC.write("  printf({});\n".format(self.argTemp))
            

    def regra13(self, producao = ''): #ARG(0) ->(1) literal(2)
        self.argTemp = producao.split(' => ')[1]

    def regra14(self, producao = ''): #ARG(0) ->(1) num(2)
        self.argTemp = producao.split()[2]

    def regra15(self, producao = ''): #ARG(0) ->(1) id(2)
        id_lexema = producao.split()[2]
        token = busca(data.tabelaSimbolos, 'lexema', id_lexema) #o id foi declarado? (se foi, ta na tabela..)

        if token['tipo'] != '':
            self.argTemp = token['lexema']
        else:
            self.mostraErro("Variável não declarada")

    def regra17(self, producao = ''):
        id_lexema = producao.split()[2] #CMD(0) ->(1) id(2) rcb(3) LD(4) ;(5)
        token = busca(data.tabelaSimbolos, 'lexema', id_lexema)

        if token['tipo'] != '':
            if token['tipo'] == self.ldTemp['tipo']:
                self.programaC.write("  {} = {};\n".format(token['lexema'], self.ldTemp['lexema'])) #pega a temporaria gerada na regra18 e atribui ao id (B = T2 por ex)
            else:
                self.mostraErr('Tipos diferentes para atribuição')

        else:
            self.mostraErro('Variável não declarada')        

    def regra18(self, producao = ''):
        opm = producao.split()[3] #método split vai salvar a 3 posicao da PRODUCAO em opm (sempre a 3a, pois a operacao matematica ta nessa posicao
                                    #LD(0) =>(1) OPRD(2) +(3) OPRD(4)
        oprd1 = self.oprdTemp.pop()
        oprd2 = self.oprdTemp.pop()
        print(oprd1, oprd2)

        if (oprd1['tipo'] == oprd2['tipo']) and oprd1['tipo'] != 'literal':
            v = "T{}".format(self.tCount)
            self.tCount += 1
            self.ldTemp = {'tipo': oprd1['tipo'], 'lexema': v}
            self.tVar.append(self.ldTemp)
            self.programaC.write("  {} = {} {} {};\n".format(v, oprd2['lexema'], opm, oprd1['lexema']))
        else:
            self.mostraErro("Operandos com tipos incompatíveis")

    def regra19(self, producao = ''):
        self.ldTemp = self.oprdTemp.pop() #pop remove e devolve o que ta na ultima posicao do vetor oprdTemp

    def regra20(self, producao = ''):
        id_lexema = producao.split()[2] #OPRD(0) ->(1) id(2)
        token = busca(data.tabelaSimbolos, 'lexema', id_lexema) #verifica se id ta declarado (taela de simb. contem todos os ids)

        if token['tipo'] != '':
            self.oprdTemp.append({'tipo': token['tipo'], 'lexema': token['lexema']})
        else:
            self.mostraErro("Variável não declarada")

    def regra21(self, producao = ''): #OPRD(0) ->(1) num(2) verifica se o num é inteiro, se for, tipo=inteiro, se nao, tipo=double
        self.oprdTemp.append({'tipo': 'int' if itsInt(producao.split()[2]) else 'double', 'lexema': producao.split()[2]})

    def regra23(self, producao = ''):
        self.programaC.write("  }\n") #insiro fecha chaves no programa.c

    def regra24(self, producao = ''):
        self.programaC.write("  if({})".format(self.exprTemp)+"{\n") #insiro if(expressão){ no programa.c
        #a exprTemp será o que vem da regra 25, a qual usa o id e o num das regras 20 e 21

    def regra25(self, producao = ''):
        opr = producao.split()[3] #EXP_R(0) ->(1) OPRD(2) opr(3) OPRD(4)
        oprd1 = self.oprdTemp.pop() #oprdTemp inserido através da regra 20 (id)
        oprd2 = self.oprdTemp.pop() #oprdTemp inserido através da regra 21 (num)

        if (oprd1['tipo'] == oprd2['tipo']) and oprd1['tipo'] != 'literal':
            v = "T{}".format(self.tCount) #crio variavel temporaria Tx (onde x é o contador das temporarias)
            self.tCount+=1 #++ pra proxima Tx
            self.tVar.append({'tipo': 'bool', 'lexema': v}) #Tx é do tipo Booleana
            self.exprTemp = v #exprTemp recebe a Tx
            self.programaC.write("  {} = {} {} {};\n".format(v, oprd2['lexema'], opr, oprd1['lexema']))
        else:
            self.mostraErro("Operandos com tipos incompatíveis")

    def mostraErro(self,mensagem):
        print("ERRO SEMÂNTICO: {}".format(mensagem))
        print("LINHA - {}".format(self.analisadorLexico.wichLinha()))
        print("COLUNA - {}".format(self.analisadorLexico.wichColuna()))


def main():
    anSintatico = analisadorSintatico()
    anSintatico.iniciaAnalise()

if __name__ == "__main__":
    main()
