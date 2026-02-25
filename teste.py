#1.	Solicite ao usuário 5 leituras de velocidade do motor.

#2.	Armazene os valores em uma lista.

#3.	Crie funções para:

#○	calcular média

#○	encontrar maior valor

#○	encontrar menor valor

#○	calcular total

#4.	Exiba um relatório final com:

#○	lista de valores

#○	média

#○	maior leitura

#○	menor leitura

#○	total

#5.	Pergunte se o usuário deseja realizar nova coleta.

#6.	Use boas práticas de programação.


#LISTA
lista = []
#SOLICITA AS 5 VELOCIDADES DOS MOTORES
def velocidade_motor():
    for i in range(5):
        while True:
            try:
                valores = float(input(f"Digite a {i+1}° velocidade:"))
                lista.append(valores) 
                break
            except ValueError:
                print("Valor invalido, tente novamente!")
        
        
#FUNÇÕES

#MÉDIA
def media():
    media = sum(lista) / len(lista)
    print("\nA sua média é:", media)
    return media
#MAIOR VALOR
def maior_valor():
    maior = max(lista) 
    print("\nO maior numero digitado da sua lista foi:", maior)
    return maior
#MENOR VALOR
def menor_valor():
    menor = min(lista)
    print("\nO menor numero digitado da sua lista foi:", menor)
    return menor
#SOMA TOTAL
def total():
    total = sum(lista)
    print("\nA soma total da sua lista foi:", total)
    return total
    

#CHAMANDO AS FUNÇÕES
velocidade_motor()

print("---- R E L A T Ó R I O ----") 
media()
maior_valor()
menor_valor()
total() 
#PEDINDO SE QUER REALIZAR UMA NOVA COLETA, SE QUISER REPETE O CODIGO SE NÃO ENCERRA O PROGRAMA
while True:
    decisao = str(input("Você deseja realizar nova coleta? (Sim ou Não):"))
    if(decisao == "Sim"):
        lista.clear
        velocidade_motor()

        print("---- R E L A T Ó R I O ----") 
        media()
        maior_valor()
        menor_valor()
        total() 
    elif decisao == "Não":
        print("Obrigado por utilizar nosso programa de coleta de dados :) , até mais!")
        break
    else :
        print("Dados inválidos insira uma das opções abaixo: \n(Sim/Não)")