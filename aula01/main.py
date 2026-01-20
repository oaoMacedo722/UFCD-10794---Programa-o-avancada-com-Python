'''
#Crie uma variavel com um nome na consola
nome = "João"
print(nome)

# escreva na consola a msg "Olá <nome>" , utilize as 3 formas diferentes de formatação de strings

ano = 2026
print("Olá", nome, "em", ano)  

print("Olá " + nome + " em " + str(ano))

print(f"Olá {nome}") # 

print("Olá {}".format(nome,ano))# metodo pre f-string


print("-------------------")

n1 = 10.0
n2 = 10.0

soma = n1 + n2
print(soma)

sub = n1 - n2
print(sub)

multip = n1 * n2
print(multip)

divisao = n1 / n2
print(divisao)

print(type(n1))
print(type(n2))
print("-------------------")

# tendo o codigo : 

idade = 18 
# verificar se a idade é maior que 18
if idade > 18:
    print("Maior de idade")

else:
    print("Menor de idade")

# verifique se a pessoa e 
# - adulta /um adulto tem mais de 18 anos) 
# - adolescente ( 12 aos 18 anos)
# - criança (tem menos de 12 anos)

if idade > 18:
    print("Adulto")

elif idade >= 12:
    print("Adolescente")

else:
    print("Criança")

print("-------------------")




#crie uma app que receba 2 notas 

# se o as dduas notas forem positivas (maior que 10) o aluno esta aprovado
# se apenas um das notas for positiva pod fazer recuperação
# se as duas notas forem negativas o aluno esta reprovado

nota1 = float(input("Insira a primeira nota: "))
nota2 = float(input("Insira a segunda nota: "))

if nota1 >= 10 and nota2 >= 10:
    print("Aluno aprovado")

elif nota1 >= 10 or nota2 >= 10:
    print("Aluno em recuperação")

else: 
    print("Aluno reprovado")


# Crie um menu com 3 opções: 
# na opt 1 mostre a msg "ola mundo"
# na opt 2 mostre a msg "bom dia"
# na opt 3 mostre a msg "boa noite"
# se a opt for invalida indique que a opt é invalida
while True:
    print("Menu:")
    print("1 - Olá Mundo")
    print("2 - Bom dia")
    print("3 - Boa noite")
    print("0 - Sair")

    escolha = int(input("Escolha uma opção: "))

    match escolha : 
        case 1:
            print("Olá Mundo")
        case 2:
            print("Bom dia")
        case 3:
            print("Boa noite")
        case 0:
            print("Adeus")
            break
        case _:
            print("Opção inválida")

print("-------------------")



# loops 
# Faça uma ap que mostre o resultada da tabuada 
# deve pedir o num da tabuada 
#adapte o seu menu para esta sempre a pedir uma opção ate ser inserida a opção 0 para sair 
while True:
    num = int(input("Escreve o numero da tabuada 1-10 ou 0 para sair: "))
    if num == 0:
        print("Programa terminado.")
        break
    elif num < 1 or num > 10:
        print("Numero invalido\n")
    else:
        for i in range(1, 11):
            resultado = num * i
            print(f"{num} x {i} = {resultado}")

lst = ["elm1", "elm2", "elm3"]
print(lst)
lst.append("elm4")
print(lst)
lst.append(30)
print(lst)
lst.remove("elm4")
lst.pop(0)
print(lst)

cnt = lst.count("elm1")
print(cnt)

print(len(lst))
print(lst.len())

nome = "João"
print(nome.len())

print(lst[0])

print("-------------------")

# Escreva um nome 
nomes = []
for i in range(5):
    nome = input("Digite um nome: ")
    nomes.append(nome)
print("Nomes inseridos:", nomes)

# Crie um programa que nome ate ser inserido 0 
# e mostre os nomes pedidos , deve mostrar um nome por linha 

nomes = []
while True:
    nome = input("Digite um nome (ou 0 para sair): ")
    if nome == "0":
        print("Adeus")
        break
    nomes.append(nome)
    for nome in nomes:
        print(nome)
'''
