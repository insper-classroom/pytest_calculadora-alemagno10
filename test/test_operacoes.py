import pytest
import numpy as np
from matematica.Calculadora import soma,sub,multiplicacao,divisao,media_lista_valores

@pytest.mark.op_simples
def test_soma_dois_valores_positivos():
    v1 = 5.0
    v2 = 7.0
    12 == soma(v1,v2)

@pytest.mark.op_simples
def test_subtração_2_valores():
    5 == sub(10,5)

@pytest.mark.op_simples
def test_multiplicacao_valor_positivo_e_negativo():
    -63 == multiplicacao(7,-9)

@pytest.mark.op_complexo
def test_divisão_segundo_numero_diferente_de_zero():
    9 == divisao(81,9)

@pytest.mark.op_complexo
def test_media_de_numeros_de_uma_lista():
    3 == media_lista_valores([1,2,3,4,5])


@pytest.mark.exercicio1
def test_media_lista_vazia():
    0 == media_lista_valores([])

@pytest.mark.exercicio1
def test_divisão_por_zero():
    np.inf == divisao(30,0)

@pytest.mark.exercicio1
def test_caracteres_nao_validos_media():
    15 == media_lista_valores([10,5,'teste',5,10])