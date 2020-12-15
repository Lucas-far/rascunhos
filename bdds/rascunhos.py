

# todo -> STANDBY
# eneq83pqh1e1o4c4p4tt5psjjhtbyisfdseh2c2bttycvksq4sopsfaymo3vd2rlpkiv1hyrxvdkz3mp8ifsq4ubislvcaf1s6qx
# del [ POO ]
# "======================================================================================================================"
# class Livro:
#     def __init__(self, nome, autor, folhas):
#         self.__nome = nome
#         self.__autor = autor
#         self.__folhas = folhas
#
#     def __del__(self):
#         print('Um dos atributos de instância foi deletado')
#
# livro1 = Livro('A herva maligna', 'John Alfriad', 172)
# print('Acesso antes de deletar o atributo de instância', livro1._Livro__folhas)
# del livro1._Livro__folhas
# print('Acesso após deletar o atributo de instância', livro1._Livro__folhas)  # Não é alcançável [ deletado antes ]

# Acesso antes de deletar o atributo de instância 172
# Um dos atributos de instância foi deletado
# Traceback (most recent call last):
#   File "C:/Users/Lucas/Envs/lucas/@5.py", line 20, in <module>
#     print('Acesso após deletar o atributo de instância', livro1._Livro__folhas)  # Não é alcançável [ deletado antes ]
# AttributeError: 'Livro' object has no attribute '_Livro__folhas'
# "======================================================================================================================"



# todo -> STANDBY
# sq9dkndc8klu1xtp4soyj4iag11d67zdi8lywh7mtdiv4xk4cnq3e44q4eqex1nkzo6pb1jfvqa5y7zbr7pxv9evn83rgy9v9jg5
# close
# [ gerenciamento de arquivo ] [ encerramento de leitura de arquivo ] [ parâmetro vazio ]
# [ dependente de abertura de arquivo ]
# "======================================================================================================================"
# contexto = ['pós-variável']
#
# with open('z.txt', 'r') as z:
#     print(z.read())
#     z.close()
# "======================================================================================================================"



# todo -> STANDBY
# rezltwnt1c6m31a7uo6y4i8d7434plvwb3hia8l96jd4dbopsxglwnbqxuicigufjlses1o5qcejqoefpgxvafi52tdh6j6sh8p6
# decode
# [ importação mandatória ] [ instalação mandatória = pip install jsonpickle ] [ método frequente em POO ]
# [ métodos de instância com decoradores de propriedade recomendável ] [ extensão .json ] [ uso em open() r ]
# [ método baseado na instanciação de objeto como argumento ] [ decodificação de dicionário das instâncias do objeto ]
# [ decodificador de dados ]
# "======================================================================================================================"
# from os import chdir
# from jsonpickle import encode, decode
#
# chdir('c:\\users\\lucas\\desktop')
#
#
# class Dados:
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def idade(self):
#         return self.__idade
#
#     @property
#     def nacionalidade(self):
#         return self.__nacionalidade
#
#     def __init__(self, nome, idade, nacionalidade):
#         self.__nome = nome
#         self.__idade = idade
#         self.__nacionalidade = nacionalidade
#
# pessoa1 = Dados('Jeruncio', 27, 'brasileiro')
#
# "Supondo que esse arquivo tenha sido criado, ele recebeu codificação para disposição de dados em dicionário"
# with open('jsonpickle.json', 'w') as doc:
#     dados_json = encode(pessoa1)  # Criaçõa da variável que recebe o método [ encode() ] e a instância do objeto
#     doc.write(dados_json)         # O método [ write() ] recebe esses dados na forma de dicionário
#
# "A decodificação acontece na abertura do arquivo já existente em forma de leitura"
# with open('jsonpickle.json', 'r') as doc2:
#     arquivo_leitura = doc2.read()          # 1. cria-se uma variável para realizar a leitura
#     decodificar = decode(arquivo_leitura)  # 2. cria-se uma segunda variável que receberá o método [ decode() ]
#     print(decodificar)
#     print(decodificar.nome)                # 3. variável que recebeu decode.método de instância
#     print(decodificar.idade)
#     print(decodificar.nacionalidade)
# "======================================================================================================================"



# todo STANDBY
# 3t1qsgslnxyf9t4kgniphbeau567qzjdgjzujfmsr8n4xk3egzlfqxbjtrfw2yrrro65146wponskf18evqes3m5a3fhq42ul6tp
# doctest
# [ teste de código em docstrings de função (simples, tripla, dupla tripla) ]
# [ teste em terminal = python -m doctest -v nome.py ]
# [ 2 args = >>> var função()
#            resultado esperado em forma de string ]
"======================================================================================================================"
########----------------------------------------------------------------------------------------------------------------
"Passos"
# 1. Cria-se uma função
# 2. Aplica-se uma string de aspas: [ simples triplas ou duplas triplas ] [ testes acontecem no escopo dela ]
# 3. Sintaxe: >>> var(arg, arg, arg,...)
# 4. Abaixo, passa-se em [ string ], o valor esperado que quer alcançar como resultado da função

# 5. Os passos 3 e 4 podem ser repetidos múltiplas vezes para múltiplos testes com a mesma função
########----------------------------------------------------------------------------------------------------------------

###########-------------------------------------------------------------------------------------------------------------
"Exemplo 1"

# def somar(a, b):
#     """
#     >>> somar(1, 9)
#     -10
#     """
#     return a + b
###########-------------------------------------------------------------------------------------------------------------

#############################-------------------------------------------------------------------------------------------
"Resultado do teste [ True ]"
# (lucas) C:\Users\Lucas\Envs\lucas>python -m doctest -v @5.py
# Trying:
#     somar(1, 9)
# Expecting:
#     10
# ok
# 1 items had no tests:
#     @5
# 1 items passed all tests:
#    1 tests in @5.somar
# 1 tests in 2 items.
# 1 passed and 0 failed.
# Test passed.
#############################-------------------------------------------------------------------------------------------

##############################------------------------------------------------------------------------------------------
"Resultado do teste [ False ]"
# (lucas) C:\Users\Lucas\Envs\lucas>python -m doctest -v @5.py
# Trying:
#     somar(1, 9)
# Expecting:
#     -10
# **********************************************************************
# File "C:\Users\Lucas\Envs\lucas\@5.py", line 11, in @5.somar
# Failed example:
#     somar(1, 9)
# Expected:
#     -10
# Got:
#     10
# 1 items had no tests:
#     @5
# **********************************************************************
# 1 items had failures:
#    1 of   1 in @5.somar
# 1 tests in 2 items.
# 0 passed and 1 failed.
# ***Test Failed*** 1 failures.
##############################------------------------------------------------------------------------------------------

#########################################################################################-------------------------------
"Testes múltiplos com uma função [ True ] [ exemplificando um valor esperado como erro ]"

"Exemplo 2"
# def duplicar(dados):
#     """
#     >>> duplicar([1, 7, 14, 28])
#     [2, 14, 28, 56]
#
#     >>> duplicar([])
#     []
#
#     >>> duplicar([None])
#     Traceback (most recent call last):
#         ...
#     TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
#     """
#     return [2 * cada_dado for cada_dado in dados]
#########################################################################################-------------------------------

##############################################################################------------------------------------------
"Testes com tipo de erro inesperado [ exemplificando erro de detalhe mínimo ]"

# 1. Doctest usa aspas simples triplas ou duplas triplas
# 2. Mesmo colocando como valor esperado, a mesma escrita passada no retorno, o teste não passará
# 3. Por que? porque no contexto, aspas duplas não se repetem de forma aninhada (uma dentro da outra)
# 4. Contraditoriamente, é preciso passar a aspa errada para que o teste passe como certo.

"Exemplo 3"
# def cumprimento():
#     """
#     >>> cumprimento()
#     'oi'
#     """
#     return "oi"

"Exemplo 4"

# 1. O teste abaixo pode parecer inofensivo e isento de erro
# 2. Porém, em doctest, minúsculos detalhes geram erro de teste
# 3. Se na string passada como valor esperado, que é [ True ], houvesse qualquer espaçamento antes ou depois = erro
# 4. No caso da IDE Pycharm, o teste passa , pois ela automaticamente retira espaçamentos sem haver textos posteriores

# def retornar_true():
#     """
#     >>> retornar_true()
#     True
#     """
#     return True
##############################################################################------------------------------------------

def somar(a, b):
    """
    >>> somar(1, 9)
    10
    """
    return a + b


def duplicar(dados):
    """
    >>> duplicar([1, 7, 14, 28])
    [2, 14, 28, 56]

    >>> duplicar([])
    []

    >>> duplicar([None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'
    """
    return [2 * cada_dado for cada_dado in dados]


def perguntar(idade):
    """
    >>> perguntar(19)
    'Vamos em frente'
    """
    if idade >= 18:
        return 'Vamos em frente'
    else:
        return 'Você não têm a permissão'
"======================================================================================================================"



# todo -> STANDBY
# bz91z2opms3zd3mdsycknrqwk63rvcci5ashsxcg38c8oahjhs4kts3tk76lcbjx8cihptrarx94c9y7xeb3wpnij9mwjsblmu8e
# dump
# [ importação mandatória ] [ criação/escrita de instâncias de objetos de forma binarizada ] [ método prefixado ]
# [ 2 args = instância de objeto, variável do documento criado ] [ extensão .pickle opcional, mas recomendável ]
# [ modo de formatação wb maandatório ]
# "======================================================================================================================"
# from pickle import dump
# class Conta:
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def senha(self):
#         return self.__senha
#
#     def __init__(self, nome, senha):
#         self.__nome = nome
#         self.__senha = senha
#
#     def mesclar(self):
#         return self.__nome + ' ' + self.__senha
#
# pessoa = Conta('Alfredo', 'x_y_z')
#
# with open('pickle_dump.pickle', 'wb') as doc:
#     dump(pessoa, doc)
# "======================================================================================================================"



# todo -> STANDBY
# ik9wowpy9v1nr5fgyfqged84u2ku4n5cideaa7ffbyq7kvubu9zgp4ozp6bdnmwzsveyumomku7qho7i36klg6vw1gz457l4k58k
# encode
# [ importação mandatória ] [ instalação mandatória = pip install jsonpickle ] [ método frequente em POO ]
# [ métodos de instância com decoradores de propriedade recomendável ] [ extensão .json ] [ uso em open() w ]
# [ método baseado na instanciação de objeto como argumento ] [ criação de dicionário das instâncias do objeto ]
# [ codificador de dados ]
# "======================================================================================================================"
# from os import chdir
# from jsonpickle import encode
#
# chdir('c:\\users\\lucas\\desktop')
#
#
# class Dados:
#     @property
#     def nome(self):
#         return self.__nome
#
#     @property
#     def idade(self):
#         return self.__idade
#
#     @property
#     def nacionalidade(self):
#         return self.__nacionalidade
#
#     def __init__(self, nome, idade, nacionalidade):
#         self.__nome = nome
#         self.__idade = idade
#         self.__nacionalidade = nacionalidade
#
# pessoa1 = Dados('Jeruncio', 27, 'brasileiro')
#
# with open('jsonpickle.json', 'w') as doc:
#     dados_json = encode(pessoa1)  # Criaçõa da variável que recebe o método [ encode() ] e a instância do objeto
#     doc.write(dados_json)         # O método [ write() ] recebe esses dados na forma de dicionário
# "======================================================================================================================"



# todo -> STANDBY
# e8emu43br6qpaml5zf2gmytozncesniyoyha6aumgn1m398qbbbav1fve6dayuv3cv57uqt4om89n1r7naiqwzhn8qdn5q9jqjts
# gil [ python global interpreter locker ] [ interpretador CPython ] [ GIL existe apenas em CPython ]
# [ interpretadores disponíveis = CPython Jython IronPython PyPy = C, Java, C#, Python]
# "======================================================================================================================"
# from sys import getrefcount
# from time import time
# from threading import Thread
# from multiprocessing import Pool
#
# # 1. [ GIL ] é conhecido como [ mutex ] ou [ lock ]
#
# "Não entendi"
# # 2. [ GIL ] permite apenas uma [ thread ] tome conta do interpretador Python [ single thread ]
#
# # 3. [ GIL ] não é nocivo a performance para programas com código [ single thread ]
# # 4. [ GIL ] é nocivo a performance para programas com código [ multi thread ]
# # 5. [ GIL ] pode ter seu impacto ser mitigado/suavizado
# # 6. Python utiliza [ reference counting ] para gerenciamento de memória [ from sys import getrefcount ]
#
# "Usando [ getrefcount() ]"
# a = []
# b = a
# # print(getrefcount(a))  # contador de referências em memória que um objeto detêm
#
# # 7. [ getrefcount ] precisa de proteção contra um fenômeno da computação chamado de [ race conditions ]
#
# "Não entendi"
# # 8.  [ race conditions ] é quando duas [ threads ] aumentam ou diminuem seu valor simultaneamente
# # 8.  [ race conditions ] é quando duas [ threads ] disputam quem vai pegar um determinado recurso
#
# # 9.  [ race conditions ] pode causar bloqueio na liberação ou liberação incorreta de memória, gerando [ crashes, bugs ]
# # 10. [ locks ] é um recurso adicionado em toda a estrutura de dados
# # 11. [ locks ] é o aprisionamento de um recurso enquanto ele é usado, para depois ser pego pelo [ garbage collector ]
# # 12. [ deadlocks ] problema quando é adicionado mais de 1 lock em [ um objeto ou grupo de objetos ]
# # 13. Outro efeito colateral da criação de múltiplos locks: decaimento de performance
# # 14. [ GIL ] transforma códigos em [ single thread ], evitando [ deadlocks ]
# # 15. [ GIL ] pode ser subtituido de [ multi-threading ] para [ multi-processing ]
# # 16. [ multi-processing ] é mais performático que [ multi-threading ], mas demanda mais recursos
#
# "Exemplo com [ single thread ]"  #######################################################################################
#
# "A importação não é usada, pois, segundo o professor, o Python já executa o código em [ single thread ]"  # não entendi
# "O [ GIL ] é perfomático em [ single threads ]"
# CONTADOR = 5_000_000
#
#
# def contagem_regressiva(n):
#     while n > 0:
#         n -= 1
# inicio = time()
# contagem_regressiva(CONTADOR)
# fim = time()
# print('Tempo decorrido: {}'.format(fim - inicio))
#
# "Exemplo com [ multi thread ]"  ########################################################################################
#
# "Normalmente [ multi thread ] é mais rápido, mas a diferença não é muito menor (mesmo havendo divisão de tarefas)"
# "Segundo o professor, isso acontece por causa do [ GIL ]"
# CONTADOR2 = 5_000_000
#
#
# def contagem_regressiva2(n):
#     while n > 0:
#         n -= 1
# teste1 = Thread(target=contagem_regressiva2, args=(CONTADOR2 // 2,))
# teste2 = Thread(target=contagem_regressiva2, args=(CONTADOR2 // 2,))
# inicio2 = time()
# teste1.start()
# teste2.start()
# teste1.join()
# teste2.join()
# fim2 = time()
# print('Tempo decorrido: {}'.format(fim2 - inicio2))
#
# "Exemplo com [ multi processing ]"  ####################################################################################
# "[ multi processing ] é mais rápido, e não parece sofrer impacto do [ GIL ]"
#
# CONTADOR3 = 5_000_000
#
#
# def contagem_regressiva3(n):
#     while n > 0:
#         n -= 1
# if __name__ == '__main__':
#     pool = Pool(processes=2)
#     tempo_inicial = time()
#     teste1_1 = pool.apply_async(contagem_regressiva, [CONTADOR3 // 2])
#     test2_2 = pool.apply_async(contagem_regressiva3, [CONTADOR3 // 2])
#     tempo_final = time()
#     print('Tempo decorrido: {}'.format(tempo_final - tempo_inicial))
# "======================================================================================================================"



# # i63fm4fcwgglv5k1rah3wtjmalkzhq5ar6z8jn1ieupi6xrsdpctea6soeffisrdhsok8ydbq8qle7o51l1g5kaungbek4zi6tzy
# # mypy
# # [ pip install mypy ] [ pip install --upgrade pip ] [ pip --version ] [ consulta por terminal = mypy nome.py ]
# # [ testagem de erro em módulo ] [ não detector de erros múltiplos ]
# "======================================================================================================================"
# "Supondo que haja um módulo de nome qualquer, por exemplo: [ arq.py ]"
# "Supondo que há dois erros no módulo [ arq.py ]"
# # var = len(7)
# # var2 = 2020.center(50)
#
# "Como se usa o [ mypy ]?"
# # Abre-se o terminal, digita-se [ mypy + nome do módulo ]
#
# "Erro"
# # (lucas) C:\Users\Lucas\Envs\lucas>mypy arq.py
# # arq.py:4: error: invalid syntax
# # Found 1 error in 1 file (checked 1 source file)
#
# "Testando com [ mypy ] um módulo do próprio ambiente virtual [ bdd_tutoriais.py ]"  # mypy bdd_tutoriais.py
# resultado = "Found 474 errors in 1 file (checked 1 source file)"
# "======================================================================================================================"
