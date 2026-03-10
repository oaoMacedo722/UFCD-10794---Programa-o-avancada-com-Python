class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float, peso: float):
        self.nome = nome.title()
        self.idade = idade
        self.altura = altura
        self.peso = peso  # em gramas
        self.energia = 100
        self.acordado = True

    # por cada coisa que come engorda 100g e ganha 5% energia
    def comer(self, alimento: list[str]):
        for peso in alimento:
            self.peso += 100
            self.energia += 5

    def falar(self):
        print(f"{self.nome} está a falar.")

    def andar(self):
        self.energia -= 10
        print(f"{self.nome} andou e perdeu energia.")

    # até aos 21 anos, por cada ano cresce 2.5 cm
    def envelhecer(self, anos: int = 1):
        for _ in range(anos):
            self.idade += 1
            if self.idade <= 21:
                self.crescer()

    def crescer(self, cm: float = 2.5):
        self.altura += cm

    def dormir(self):
        if self.acordado:
            self.acordado = False
            self.energia = 100
            print("A pessoa foi dormir e recuperou energia.")
        else:
            print("Já está a dormir.")

    def acordar(self):
        if not self.acordado:
            self.acordado = True
            print("A pessoa acordou.")
        else:
            print("Já está acordada.")
