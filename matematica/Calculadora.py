import numpy as np

def soma(va: float, vb: float):
    ''' Função que retorna a soma entre dois valores
    '''
    return va + vb

def sub(va: float, vb: float):
    ''' Função que retorna a subtração entre dois valores
    '''
    return va - vb

def multiplicacao(va: float, vb: float):
    ''' Função que retorna a multiplicação entre dois valores
    '''
    return va * vb

def divisao(va: float, vb: float):
    ''' Função que retorna a divisão entre dois valores
    '''
    if vb != 0:
        return va / vb
    else: return np.inf

def media_lista_valores(v:list):
    ''' Função que retorna a média entre N valores
    '''
    
    v_numeros = [x for x in v if isinstance(x,(int,float))]
    return np.mean(v_numeros)
