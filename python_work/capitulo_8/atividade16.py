'''
atividade 8.16 Imports: Usando um programa que você escreveu e que tenha apenas uma
função, armazene essa função em um arquivo separado. Importe a função para o arquivo
de programa principal e chame a função usando cada uma dessas abordagens... página 203
'''
import greet
from greet import greet_user
from greet import greet_user as gt
import greet as g
from greet import *
