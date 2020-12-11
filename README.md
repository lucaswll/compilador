# Compilador
Analisadores Léxico, Sintático e Semântico feitos em Python, propondo construção de um compilador.

Os analisadores visam compilar para linguagem C, regras de uma linguagem proposta denominada MGOL (haja vista que linguagens existentes possuem muitas regras de 
análise léxica, sintática e semântica).
Os Tokens que precisam ser reconhecidos pelo Analisador Léxico para a respectiva linguagem, estão descritos na tabela abaixo: 

<h1 align="center">
    <img style="width:70%" alt="proffy-lks" src="https://i.ibb.co/gv9DvzW/111.png" />
    <br>
</h1>

Palavras-chave da linguagem estão definidas por: 

<h1 align="center">
    <img style="width:70%" alt="proffy-lks" src="https://i.ibb.co/xSxBcks/Palavras-Chave.png" />
    <br>
</h1>

O programa fonte teste que é lido pelo Analisador Léxico, o qual tokenizará os lexemas, passando-os para o Sintátio por ser visto a seguir.

<h1 align="center">
    <img style="width:70%" alt="proffy-lks" src="https://i.ibb.co/d4k6YsS/Progama-fonte.png" />
    <br>
</h1>

Por fim, o resultado final da compilação do código fonte resultará no programa final definido como 'programa.c'.

<h1 align="center">
    <img style="width:70%" alt="proffy-lks" src="https://i.ibb.co/J2Fntqm/Final.png" />
    <br>
</h1>


## Passos
A geração do resultado final (programa.c) se dá pela execução do 'Analisador Semântico.py'. Para isso, se faz necessário sua execução no formato personalizado, 
o qual permite a inserção de um arquivo que será utilizado pelo próprio código, através do módulo 'sys'. O arquivo diz respeito ao programa fonte, que está 
definido como 'fonteLexico.txt'. 

Ao finalizar a execução do semântico, em sua própria pasta será criado o arquivo 'programa.c', contendo a versão em C do programa em MGOL.
