producoesEnumeradas = { #enumrando a gramática
   #1: é o accept (P'), não entra
    #adaptei pra que o prodEnum[2] demonstre se tem regra semântica
    2: [6, "P", False],
    3: [4, "V", False],
    4: [4, "LV", False],
    5: [4, "LV", True],
    6: [6, "D", True],
    7: [2, "TIPO", True],
    8: [2, "TIPO", True],
    9: [2, "TIPO", True],
    10: [4, "A", False],
    11: [6, "ES", True],
    12: [6, "ES", True],
    13: [2, "ARG", True],
    14: [2, "ARG", True],
    15: [2, "ARG", True],
    16: [4, "A", False],
    17: [8, "CMD", True],
    18: [6, "LD", True],
    19: [2, "LD", True],
    20: [2, "OPRD", True],
    21: [2, "OPRD", True],
    22: [4, "A", False],
    23: [4, "COND", True],
    24: [10, "CABEÇALHO", True],
    25: [6, "EXP_R", True],
    26: [4, "CORPO", False],
    27: [4, "CORPO", False],
    28: [4, "CORPO", False],
    29: [2, "CORPO", False],
    30: [2, "A", False]
}


tabelaTransicao = [ #linhas - estados || colunas - Símbolos não terminais
    [1, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, 3, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, 5, None, None, None, 6, None, 7, None, None, 8, 13, None, None],
    [None, None, None, 15, 16, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None,19,None,None,None,6,None,7,None,None,8,13,None,None],
    [None, None,20,None,None,None,6,None,7,None,None,8,13,None,None],
    [None, None,21,None,None,None,6,None,7,None,None,8,13,None,None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None,None,None,None,None,None,23,None,None,None,None,None,None,None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None,None,None,None,None,29,None,30,None,None,31,13,28,None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None,None,34,16,None,None,None,None,None,None,None,None,None,None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, 36, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, 42, 43, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, 29, None, 30, None, None, 31, 13, 46, None],
    [None, None, None, None, None, None, 29, None, 30, None, None, 31, 13, 47, None],
    [None, None, None, None, None, None, 29, None, 30, None, None, 31, 13, 48, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 50, None, None, None, 49],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 56, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, 58, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None],
    [None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
]

simbolosNaoTerminais = { #enumerados de acordo com as colunas na tabelaTransicao- fazendo a conexao coluna - não-terminal representado
    'P': 0,
    'V': 1,
    'A': 2,
    'LV': 3,
    'D': 4,
    'TIPO': 5,
    'ES': 6,
    'ARG': 7,
    'CMD': 8,
    'LD': 9,
    'OPRD':10 ,
    'COND': 11,
    'CABEÇALHO': 12,
    'CORPO': 13,
    'EXP_R': 14
}

tabelaAcao = [ #linhas - estados || colunas - Símbolos terminais
    ['S2', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0', 'e0'],
    ['e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'e1', 'ACC'],
    ['e2', 'S4', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2', 'e2'],
    ['e3', 'e3', 'e3', 'e3', 'S12', 'e3', 'e3', 'e3', 'S10', 'S11', 'e3', 'e3', 'e3', 'e3', 'S14', 'e3', 'e3', 'e3', 'e3', 'e3', 'S9','e3'],
    ['e4', 'e4', 'S17', 'e4', 'S18', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4', 'e4'],
    ['e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'e5', 'R2'],
    ['e6', 'e6', 'e6', 'e6', 'S12', 'e6', 'e6', 'e6', 'S10', 'S11', 'e6', 'e6', 'e6', 'e6', 'S14', 'e6', 'e6', 'e6', 'e6', 'e6', 'S9', 'e6'],
    ['e7', 'e7', 'e7', 'e7', 'S12', 'e7', 'e7', 'e7', 'S10', 'S11', 'e7', 'e7', 'e7', 'e7', 'S14', 'e7', 'e7', 'e7', 'e7', 'e7', 'S9', 'e7'],
    ['e8', 'e8', 'e8', 'e8', 'S12', 'e8', 'e8', 'e8', 'S10', 'S11', 'e8', 'e8', 'e8', 'e8', 'S14', 'e8', 'e8', 'e8', 'e8', 'e8', 'S9', 'e8'],
    ['e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'e9', 'R30'],
    ['e10', 'e10', 'e10', 'e10', 'S22', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10', 'e10'],
    ['e11', 'e11', 'e11', 'e11', 'S26', 'e11', 'e11', 'e11', 'e11', 'e11', 'S24', 'S25', 'e11', 'e11', 'e11', 'e11', 'e11', 'e11', 'e11', 'e11', 'e11', 'e11'],
    ['e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'S27', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12', 'e12'],
    ['e13', 'e13', 'e13', 'e13', 'S12', 'e13', 'e13', 'e13', 'S10', 'S11', 'e13', 'e13', 'e13', 'e13', 'S14', 'e13', 'e13', 'e13', 'e13', 'S32', 'e13', 'e13'],
    ['e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14', 'S33', 'e14', 'e14', 'e14', 'e14', 'e14', 'e14'],
    ['e15', 'e15', 'e15', 'e15', 'R3', 'e15', 'e15', 'e15', 'R3', 'R3', 'e15', 'e15', 'e15', 'e15', 'R3', 'e15', 'e15', 'e15', 'e15', 'e15', 'R3', 'e15'],
    ['e16', 'e16', 'S17', 'e16', 'S18', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16', 'e16'],
    ['e17', 'e17', 'e17', 'S35', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17', 'e17'],
    ['e18', 'e18', 'e18', 'e18', 'e18', 'S37', 'S38', 'S39', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18', 'e18'],
    ['e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'e19', 'R10'],
    ['e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'e20', 'R16'],
    ['e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'e21', 'R22'],
    ['e22', 'e22', 'e22', 'S40', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22', 'e22'],
    ['e23', 'e23', 'e23', 'S41', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23', 'e23'],
    ['e24', 'e24', 'e24', 'R13', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24', 'e24'],
    ['e25', 'e25', 'e25', 'R14', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25', 'e25'],
    ['e26', 'e26', 'e26', 'R15', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26', 'e26'],
    ['e27', 'e27', 'e27', 'e27', 'S44', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27', 'S45', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27', 'e27'],
    ['e28', 'e28', 'e28', 'e28', 'R23', 'e28', 'e28', 'e28', 'R23', 'R23', 'e28', 'e28', 'e28', 'e28', 'R23', 'e28', 'e28', 'e28', 'e28', 'R23', 'R23', 'e28'],
    ['e29', 'e29', 'e29', 'e29', 'S12', 'e29', 'e29', 'e29', 'S10', 'S11', 'e29', 'e29', 'e29', 'e29', 'S14', 'e29', 'e29', 'e29', 'e29', 'S32', 'e29', 'e29'],
    ['e30', 'e30', 'e30', 'e30', 'S12', 'e30', 'e30', 'e30', 'S10', 'S11', 'e30', 'e30', 'e30', 'e30', 'S14', 'e30', 'e30', 'e30', 'e30', 'S32', 'e30', 'e30'],
    ['e31', 'e31', 'e31', 'e31', 'S12', 'e31', 'e31', 'e31', 'S10', 'S11', 'e31', 'e31', 'e31', 'e31', 'S14', 'e31', 'e31', 'e31', 'e31', 'S32', 'e31', 'e31'],
    ['e32', 'e32', 'e32', 'e32', 'R29', 'e32', 'e32', 'e32', 'R29', 'R29', 'e32', 'e32', 'e32', 'e32', 'R29', 'e32', 'e32', 'e32', 'e32', 'R29', 'R29', 'e32'],
    ['e33', 'e33', 'e33', 'e33', 'S44', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33', 'S45', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33', 'e33'],
    ['e34', 'e34', 'e34', 'e34', 'R4', 'e34', 'e34', 'e34', 'R4', 'R4', 'e34', 'e34', 'e34', 'e34', 'R4', 'e34', 'e34', 'e34', 'e34', 'e34', 'R4', 'e34'],
    ['e35', 'e35', 'e35', 'e35', 'R5', 'e35', 'e35', 'e35', 'R5', 'R5', 'e35', 'e35', 'e35', 'e35', 'R5', 'e35', 'e35', 'e35', 'e35', 'e35', 'R5', 'e35'],
    ['e36', 'e36', 'e36', 'S51', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36', 'e36'],
    ['e37', 'e37', 'e37', 'R7', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37', 'e37'],
    ['e38', 'e38', 'e38', 'R8', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38', 'e38'],
    ['e39', 'e39', 'e39', 'R9', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39', 'e39'],
    ['e40', 'e40', 'e40', 'e40', 'R11', 'e40', 'e40', 'e40', 'R11', 'R11', 'e40', 'e40', 'e40', 'e40', 'R11', 'e40', 'e40', 'e40', 'e40', 'R11', 'R11', 'e40'],
    ['e41', 'e41', 'e41', 'e41', 'R12', 'e41', 'e41', 'e41', 'R12', 'R12', 'e41', 'e41', 'e41', 'e41', 'R12', 'e41', 'e41', 'e41', 'e41', 'R12', 'R12', 'e41'],
    ['e42', 'e42', 'e42', 'S52', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42', 'e42'],
    ['e43', 'e43', 'e43', 'R19', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'S53' , 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43', 'e43'],
    ['e44', 'e44', 'e44', 'R20', 'e44', 'e44', 'e44', 'e44', 'e44', 'e44', 'e44', 'e44', 'e44', 'R20', 'e44', 'e44', 'R20', 'e44', 'R20', 'e44', 'e44', 'e44'],
    ['e45', 'e45', 'e45', 'R21', 'e45', 'e45', 'e45', 'e45', 'e45', 'e45', 'e45', 'e45', 'e45', 'R21', 'e45', 'e45', 'R21', 'e45', 'R21', 'e45', 'e45', 'e45'],
    ['e46', 'e46', 'e46', 'e46', 'R26', 'e46', 'e46', 'e46', 'R26', 'R26', 'e46', 'e46', 'e46', 'e46', 'R26', 'e46', 'e46', 'e46', 'e46', 'R26', 'R26', 'e46'],
    ['e47', 'e47', 'e47', 'e47', 'R27', 'e47', 'e47', 'e47', 'R27', 'R27', 'e47', 'e47', 'e47', 'e47', 'R27', 'e47', 'e47', 'e47', 'e47', 'R27', 'R27', 'e47'],
    ['e48', 'e48', 'e48', 'e48', 'R28', 'e48', 'e48', 'e48', 'R28', 'R28', 'e48', 'e48', 'e48', 'e48', 'R28', 'e48', 'e48', 'e48', 'e48', 'R28', 'R28', 'e48'],
    ['e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'e49', 'S54', 'e49', 'e49', 'e49', 'e49', 'e49'],
    ['e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'e50', 'S55', 'e50', 'e50', 'e50'],
    ['e51', 'e51', 'R6', 'e51', 'R6', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51', 'e51'],
    ['e52', 'e52', 'e52', 'e52', 'R17', 'e52', 'e52', 'e52', 'R17', 'R17' , 'e52', 'e52', 'e52', 'e52', 'R17', 'e52', 'e52', 'e52', 'e52', 'R17', 'R17', 'e52'],
    ['e53', 'e53', 'e53', 'e53', 'S44', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53', 'S45', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53', 'e53'],
    ['e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'e54', 'S57', 'e54', 'e54', 'e54', 'e54'],
    ['e55', 'e55', 'e55', 'e55', 'S44' , 'e55', 'e55', 'e55', 'e55', 'e55', 'e55', 'S45' , 'e55', 'e55', 'e55', 'e55', 'e55', 'e55', 'e55', 'e55', 'e55', 'e55'],
    ['e56', 'e56', 'e56', 'R18', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56', 'e56'],
    ['e57', 'e57', 'e57', 'e57', 'R24', 'e57', 'e57', 'e57', 'R24', 'R24', 'e57', 'e57', 'e57', 'e57', 'R24', 'e57', 'e57', 'e57', 'e57', 'R24', 'e57', 'e57'],
    ['e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'e58', 'R25', 'e58', 'e58', 'e58', 'e58', 'e58']
    
]

simbolosTerminais = { #enumerados de acordo com as colunas na tabelaAcao - fazendo a conexão coluna - terminal representado
    'inicio': 0,
    'varinicio': 1,
    'varfim': 2,
    'PT_V': 3,
    'id': 4,
    'inteiro': 5,
    'real': 6,
    'lit': 7,
    'leia': 8,
    'escreva': 9,
    'Literal': 10,
    'Num': 11,
    'RCB': 12,
    'OPM': 13,
    'se': 14,
    'AB_P': 15,
    'FC_P': 16,
    'entao': 17,
    'OPR': 18,
    'fimse': 19,
    'fim': 20,
    'EOF': 21
}

errors = {
    'e0': 'Terminal "inicio" não consta!',
    'e1': 'Provável que tabela não tenha o ACCEPT!',
    'e2': 'Terminal "varinicio" não consta!',
    'e3': 'Terminais "fim", "leia", "escreva", "id" ou "se" não encontrados!',
    'e4': 'Terminais "varfim" ou "id" não encontrados!',
    'e5': 'Nenhum terminal gerado por A encontrado!',
    'e6': 'Terminais "fim", "leia", "escreva", "id" ou "se" não encontrados!',
    'e7': 'Terminais "fim", "leia", "escreva", "id" ou "se" não encontrados!',
    'e8': 'Terminais "fim", "leia", "escreva", "id" ou "se" não encontrados!',
    'e9': 'Existe algo além do terminal "fim" que não faz parte da linguagem!',
    'e10': 'Terminal "id" não consta!',
    'e11': 'Terminais "literal", "num" ou "id" não encontrados!',
    'e12': 'Atribuição incorreta || termo "Escreva" faltante || estrutura do "Escreva" está incorreta!',
    'e13': 'Terminais "fim", "leia", "escreva", "id" ou "se" não encontrados!',
    'e14': 'Abre parênteses não encontrado!',
    'e15': 'LV não gerou "id", "leia", "escreva", "se" ou "fim"!',
    'e16': 'Terminais "varfim" ou "id" não encontrados!',
    'e17': 'Terminal ";" não consta!',
    'e18': 'Tipo identificador está vazio ou diferente de "lit", "inteiro" ou "real"!',
    'e19': 'Nenhum terminal gerado por A encontrado!',
    'e20': 'Nenhum terminal gerado por A encontrado!',
    'e21': 'Nenhum terminal gerado por A encontrado!',
    'e22': 'Terminal ";" não consta!',
    'e23': 'Terminal ";" não consta!',
    'e24': 'Terminal ";" não encontrado após o literal!',
    'e25': 'Existe algo além do terminal "num"!',
    'e26': 'Terminal ";" não encontrado após print!',
    'e27': 'Terminais "num" ou "id" não encontrados!',
    'e28': 'Nenhuma expressão gerada por CORPO encontrado antes de "fimse" (atribuição, leitura, comparação)!',
    'e29': 'Fechamento do "então" não encontrado: "fimse"!',
    'e30': 'Terminais "leia", "escreva", "id", "se" ou "fimse" não encontrados!',
    'e31': 'Terminais "leia", "escreva", "id", "se" ou "fimse" não encontrados!',
    'e32': 'Existe algo além do terminal "fimse" que não faz parte da linguagem!',
    'e33': 'Terminais "num" ou "id" não encontrados!',
    'e34': 'Terminal identificador de tipo não consta!',
    'e35': 'Terminal ";" não consta após "leia", "escreva", "id", "se" ou "fim"!',
    'e36': 'Terminal ";" não consta após declaração do tipo do id!',
    'e37': 'Terminal ";" não encontrado após declaração do tipo "inteiro"!',
    'e38': 'Terminal ";" não encontrado após declaração do tipo "real"!',
    'e39': 'Terminal ";" não encontrado após declaração do tipo "lit"!',
    'e40': 'Condicional "se" não encontrado!',
    'e41': 'Fechamento do "inicio" não encontrado: "fim"',
    'e42': 'Terminal ";" não consta!',
    'e43': 'Operador matemático não encontrado ou existe algo após a declaração do operando!',
    'e44': 'Espaçamento não suportado! Espera-se um operador aritmético!',
    'e45': 'Terminal ";" não encontrado após a atribuição ou faltando fechamento de parenteses!',
    'e46': 'Corpo não finalizado com "fimse"!',
    'e47': 'Corpo não finalizado com "fimse"!',
    'e48': 'Corpo não finalizado com "fimse"!',
    'e49': 'Fecha parênteses não encontrado!',
    'e50': 'Operador aritmético não consta!',
    'e51': 'Terminal ";" ou fechamento de "varinicio" (varfim) não constam!',
    'e52': 'Terminal ";" não consta após atribuição!',
    'e53': 'Operando diferente de "id" ou "num"!',
    'e54': 'Fechamento do "se" não encontrado: "então"!',
    'e55': 'Operando diferente de "id" ou "num"!',
    'e56': 'Operando diferente de "id" ou "num"!',
    'e57': 'Condicional "se" não encontrado!',
    'e58': 'Operando diferente de "id" ou "num"!',
}
