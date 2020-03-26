import ply.lex as lex
import sys

#Palavras reservadas
reserved = {
    'se': 'SE',
    'então': 'ENTAO',
    'senão': 'SENAO',
    'fim': 'FIM',
    'repita': 'REPITA',
    'flutuante': 'FLUTUANTE',
    'retorna': 'RETORNA',
    'até': 'ATE',
    'leia': 'LEIA',
    'escreva': 'ESCREVA',
    'inteiro': 'INTEIRO'
}

# Lista dos tokens
tokens = [
    'MAIS',
    'MENOS',
    'MULTIPLICACAO',
    'DIVISAO',
    'DOIS_PONTOS',
    'VIRGULA',
    'MENOR',
    'MAIOR',
    'IGUAL',
    'DIFERENTE',
    'MENOR_IGUAL',
    'MAIOR_IGUAL', 
    'E_LOGICO', 
    'OU_LOGICO', 
    'NEGACAO', 
    'ABRE_PARENTESE', 
    'FECHA_PARENTESE', 
    'ABRE_COLCHETE', 
    'FECHA_COLCHETE', 
    'ATRIBUICAO',  
    'NUM_INTEIRO', 
    'NUM_PONTO_FLUTUANTE', 
    'NUM_NOTACAO_CIENTIFICA', 
    'ID',
    'ABRE_CHAVE',
    'FECHA_CHAVE',
    'COMENTARIO'
] + list(reserved.values())


t_MAIS = r'\+'
t_MENOS = r'-'
t_MULTIPLICACAO = r'\*'
t_DIVISAO = r'/'
t_DOIS_PONTOS = r':'
t_VIRGULA = r','
t_MENOR = r'<'
t_MAIOR = r'>'
t_IGUAL = r'='
t_DIFERENTE = r'<>'
t_MENOR_IGUAL = r'<='
t_MAIOR_IGUAL = r'>='
t_E_LOGICO = '&&'
t_OU_LOGICO = '\|\|'
t_NEGACAO = '!'
t_ABRE_PARENTESE = r'\('
t_FECHA_PARENTESE = r'\)'
t_ABRE_COLCHETE = r'\['
t_FECHA_COLCHETE = r'\]'
t_ATRIBUICAO = r':=' 
t_ABRE_CHAVE = r'{' 
t_FECHA_CHAVE = r'}' 

def t_COMENTARIO(t):
    r'{[\d\D]*?}'
    t.value = str(t.value)
    return t

def t_ID(t):
     r'[a-zA-Z_à-ú][a-zA-Z_0-9à-ú]*'
     # Se não encontrar a chave nas palavras reservadas, retorna ID para o tipo
     t.type = reserved.get(t.value,'ID')    # Verifica por palavras reservadas
     return t

def t_NUM_NOTACAO_CIENTIFICA(t):
    r'\d+\.?\d*e(\+|-)?\d+'
    t.value = float(t.value)
    return t

def t_NUM_PONTO_FLUTUANTE(t):
    r'\d+\.\d+'
    t.value = str(t.value)
    return t
    
# A regular expression rule with some action code
def t_NUM_INTEIRO(t):
    r'\d+'
    t.value = int(t.value)
    return t



# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)


# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'
 
 # Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
 
 # Build the lexer
lexer = lex.lex()

if __name__ == "__main__":
    if(len(sys.argv) < 2):
        print("Erro! Informe o nome do arquivo")
    else:
        try:
            arq = open(sys.argv[1])
            lexer.input(arq.read())
            
            #Verifica token a token 
            for tok in lexer:
                print(tok)

        except FileNotFoundError as identifier:
            print("Erro! Arquivo não encontrado")
        