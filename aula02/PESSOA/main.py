from pessoa import Pessoa
p1 = Pessoa("joao", 18, 170.0, 65000)

print("Estado inicial:")
print(p1.nome, p1.idade, p1.altura, p1.peso, p1.energia, p1.acordado)

p1.comer(["maçã", "sandes", "sumo"])
print("\nDepois de comer:")
print("Peso:", p1.peso, "Energia:", p1.energia)

p1.andar()
print("\nDepois de andar:")
print("Energia:", p1.energia)

p1.dormir()
print("Acordado?", p1.acordado)

p1.acordar()
print("Acordado?", p1.acordado)

p1.envelhecer(3)
print("\nDepois de envelhecer 3 anos:")
print("Idade:", p1.idade, "Altura:", p1.altura)