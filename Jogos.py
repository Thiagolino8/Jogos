import Forca
import Adivinhação
import os
import time


def cls():
    os.system("cls") or None


def sleep(x):
    time.sleep(x)


def jogos():
    cls()
    print("*********************************")
    print("************Bem vindo************")
    print("*********************************")
    jogos_por_chamada()


def jogos_por_chamada():
    while True:
        jogo = int(input("Escolha o jogo deseado:\n(1)-Adivinhação (2)-Forca\n"))
        if(jogo == 1):
            Adivinhação.adivinhação_por_chamada()
            break
        elif(jogo == 2):
            Forca.forca_por_chamada()
            break
        else:
            cls()
            print("Opção invalida!\n")
            sleep(1)


if(__name__ == "__main__"):
    jogos()
