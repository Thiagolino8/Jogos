import random
import Jogos
import os
import time


def cls():
    os.system("cls") or None


def sleep(x):
    time.sleep(x)


def bem_vindo():
    cls()
    print("*********************************")
    print("Bem vindo ao jogo de adivinhação!")
    print("*********************************")


def seletor_de_dificuldade():
    while True:
        dificuldade = int(input("\nDefina o nível de dificuldade desejada\n(1)-Fácil (2)-Médio (3)-Difícil\n"))
        if(dificuldade == 1):
            dificuldade = 10
            break
        elif(dificuldade == 2):
            dificuldade = 5
            break
        elif(dificuldade == 3):
            dificuldade = 3
            break
        else:
            cls()
            print("Opção invalida!\n")
            sleep(1)
    cls()
    return dificuldade


def jogo(dificuldade, numero_secreto, pontos):
    for rodada in range(0, dificuldade):
        print(f"\n\nRodada {rodada + 1} de {dificuldade}")
        chute = int(input("Digite o seu chute: "))

        if(chute < numero_secreto):
            cls()
            print("\nSeu chute foi menor que o número secreto!")
            sleep(1)
            pontos = abs(pontos - chute)
            continue
        elif (chute > numero_secreto):
            cls()
            print("\nSeu chute foi maior que o número secreto!")
            sleep(1)
            pontos = abs(pontos - chute)
            continue
        else:
            cls()
            print("\nVocê acertou!")
            sleep(1)
            break
    return pontos


def replay():
    while True:
        novamente = input("Deseja jogar novamente?\n").strip()
        cls()
        if novamente == "sim":
            novamente = True
            break
        elif novamente == "não":
            novamente = False
            break
        else:
            cls()
            print("Opção inválida!")
            sleep(1)
    return novamente


def voltar_ao_seletor():
    while True:
        cls()
        voltar = input("Deseja voltar para o seletor de jogos?\n").strip()
        if voltar == "sim":
            cls()
            Jogos.jogos_por_chamada()
            break
        elif voltar == "não":
            voltar = False
            break
        else:
            cls()
            print("Opção inválida!")
            sleep(1)


def adivinhação_por_chamada():
    cls()
    adivinhação()
    voltar_ao_seletor()


def adivinhação():
    bem_vindo()
    numero_secreto = random.randrange(1, 101)
    pontos = 1000
    novamente = True

    while novamente:
        dificuldade = seletor_de_dificuldade()
        pontos = jogo(dificuldade, numero_secreto, pontos)

        print(f"\n\nFim de jogo!\nO número secreto era: {numero_secreto}\
            \nSua pontuação foi de: {pontos} pontos")
        sleep(1)
        novamente = replay()


if(__name__ == "__main__"):
    adivinhação()
