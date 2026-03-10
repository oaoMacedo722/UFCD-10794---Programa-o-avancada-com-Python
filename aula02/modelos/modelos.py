class Carro:
    def __init__(self, marca :str, modelo):
        self.marca = marca.title()
        self.modelo = modelo.title()
        self.num_km = 0.0
        
    def andar(self, velocidade: float, tempo: float):
        distancia = (velocidade * tempo) / 60
        self.num_km += distancia

    def consumo_total(self, consumo: float):
        total = self.num_km * consumo
        return total
    
"""
assuma que o carro se desloca a uma velocidade constante 

a velocidade deve ser expressa em km/h
o tempo em minutos

a função deve atualizar o num_km do carro
"""


#crie a class livro (defina apenas os atributos)
class livro:
    def init(self, titulo: str, autor: str, ano: int = None, editora: str = None, isbn: str = None,):
        self.titulo = titulo.title()
        self.autor = autor.title() 
        self.ano = None
        self.editora = None
        self.isbn = None

    def mudar_cor(self, cor: str):
        self.cor = cor.title()
#calcule o consomo de combustivel total do carro
#assuna que o consumo é constate (x l por km)
#define o x onde fize mais sentido

