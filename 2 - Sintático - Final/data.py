estadosFinais = [
    {'numEstado': 1, 'tokenIdent': 'Num'},
    {'numEstado': 3, 'tokenIdent': 'Num'},
    {'numEstado': 6, 'tokenIdent': 'Num'},
    {'numEstado': 8, 'tokenIdent': 'Literal'},
    {'numEstado': 9, 'tokenIdent': 'id'},
    {'numEstado': 11, 'tokenIdent': 'Comentario'},
    {'numEstado': 12, 'tokenIdent': 'EOF'},
    {'numEstado': 13, 'tokenIdent': 'OPR'},
    {'numEstado': 14, 'tokenIdent': 'OPR'},
    {'numEstado': 15, 'tokenIdent': 'OPR'},
    {'numEstado': 16, 'tokenIdent': 'OPR'},
    {'numEstado': 17, 'tokenIdent': 'OPR'},
    {'numEstado': 18, 'tokenIdent': 'RCB'},
    {'numEstado': 19, 'tokenIdent': 'OPM'},
    {'numEstado': 20, 'tokenIdent': 'AB_P'},
    {'numEstado': 21, 'tokenIdent': 'FC_P'},
    {'numEstado': 22, 'tokenIdent': 'PT_V'},
]

estadosNaoFinais = [ #msg apresentada caso fique 'preso' num estado nao final
    {'numEstado': 0, 'msg': 'Lexema só é valido caso todos caracteres façam parte do alfabeto da linguagem.'},
    {'numEstado': 2, 'msg': 'Número real necessita no minimo uma parte decimal e aceita apenas dígitos.'},
    {'numEstado': 4, 'msg': 'Número exponencial (e) deve possuir: pelo menos 1 dígito com ou sem sinal (+/-).'},
    {'numEstado': 5, 'msg': 'Número exponencial (e) deve possuir apenas dígitos após o sinal (+/-).'},
    {'numEstado': 7, 'msg': 'Literal sem fechamento das aspas ou com caractere fora do alfabeto da linguagem.'},
    {'numEstado': 10, 'msg': 'Comentário sem fechamento das chaves.'},
    {'numEstado': 23, 'msg': 'Caractere usado está fora do alfabeto da linguagem.'}
]

tabelaSimbolos = [ #pré-preenchida com as palavras reservadas do MGol - tipo vazio - usarei no sintatico
    {'lexema': 'inicio', 'token': 'inicio', 'tipo': ''},
    {'lexema': 'varinicio', 'token': 'varinicio', 'tipo': ''},
    {'lexema': 'varfim', 'token': 'varfim','tipo': ''},
    {'lexema': 'escreva', 'token': 'escreva', 'tipo': ''},
    {'lexema': 'leia', 'token': 'leia', 'tipo': ''},
    {'lexema': 'se', 'token': 'se', 'tipo': ''},
    {'lexema': 'entao', 'token': 'entao', 'tipo': ''},
    {'lexema': 'fimse', 'token': 'fimse', 'tipo': ''},
    {'lexema': 'fim', 'token': 'fim', 'tipo': ''},
    {'lexema': 'inteiro', 'token': 'inteiro', 'tipo': ''},
    {'lexema': 'lit', 'token': 'lit', 'tipo': ''},
    {'lexema': 'real', 'token': 'real', 'tipo': ''}
]

tabelaTransicao = [ #linha - estados e coluna - entradas
    [1, None, None, 19, 19, 7, None, 9, None, 10, None, 12, 13, 17, 15, 19, 19, 20, 21, 22, 23, 0, 0, 0, None],
    [1, 2, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [3, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [3, None, 4, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [6, None, None, 5, 5, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [6, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 8, 7, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [9, None, None, None, None, None, None, 9, 9, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 11, None, None, None, None, None, None, None, None, None, None, None, None, None, 10],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, 18, None, None, None, None, None, None, None, None, 14, 14, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, 16, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, 23, None, None, None, None]
]
