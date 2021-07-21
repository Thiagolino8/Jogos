import random
import Jogos
import os
import time


def cls():
    os.system("cls") or None


def sleep(x):
    time.sleep(x)


def voltar_ao_seletor():
    while True:
        voltar = input("Deseja voltar para o seletor de jogos?\n")
        cls()
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


def bem_vindo():
    cls()
    print("*********************************")
    print("***Bem vindo ao jogo de forca!***")
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
    return dificuldade


def seletor_de_palavra():
    with open("Palavras.txt", "r") as arquivo:
        lista_de_palavras = []
        for linha in arquivo:
            linha = linha.strip()
            lista_de_palavras.append(linha.upper())
    palavra_secreta = lista_de_palavras[random.randrange(0, len(lista_de_palavras))]
    return palavra_secreta


def verifica_fim(forca, erros, dificuldade, palavra_secreta):
    if forca.count("_") == 0:
        print("PARABÉNS! VOCÊ VENCEU!")
        return True
    elif erros == dificuldade:
        print(f"QUE PENA! VOCÊ PERDEU!\nA palavra secreta era {palavra_secreta}")
        return True


def imprime_forca(forca):
    for k in range(len(forca)):
        print(forca[k], end=' ')
    print("\n")


def jogo(dificuldade):
    novamente = True
    while novamente:
        palavra_secreta = seletor_de_palavra()
        forca = ["_" for letra in palavra_secreta]
        erros = 0
        cls()
        print("Jogando...")
        acabou = False
        while not acabou:
            print(f"Você tem {dificuldade - erros} vidas restantes")
            imprime_forca(forca)
            chute = input("Insira seu chute: ").strip().upper()
            cls()
            if chute in forca:
                print("Você já tentou essa letra")
            elif chute in palavra_secreta and chute not in forca:
                print("Você acertou!")
                for j in range(len(palavra_secreta)):
                    if palavra_secreta[j].upper() == chute:
                        forca.pop(j)
                        forca.insert(j, chute.upper())
            else:
                print("Você errou!")
                erros += 1
            acabou = verifica_fim(forca, erros, dificuldade, palavra_secreta)
        novamente = replay()


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
            sleep()
    return novamente


def forca_por_chamada():
    forca()
    voltar_ao_seletor()


def forca():
    bem_vindo()
    dificuldade = seletor_de_dificuldade()
    jogo(dificuldade)


if __name__ == "__main__":
    forca()
