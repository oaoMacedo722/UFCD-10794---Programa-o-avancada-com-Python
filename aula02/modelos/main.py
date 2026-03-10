from aula02.modelos.modelos import Carro

c1 = Carro("BWM", " X5")
c2 = Carro("ford", " Puma")

print(c1.marca, c2.marca)

c1.marca = "Baverische Motoren Werke"


c3 = Carro("Fiat", " Toro")
c3.andar(60, 120)

print(c3.num_km)
print(c3.consumo_total(0.14))