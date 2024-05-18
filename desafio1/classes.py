class Pessoa():
    def __init__(self, nome, peso, idade, comendo=False, falando=False):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = comendo
        self.falando = falando

    def comer(self):
        if self.comendo:
            print(f"{self.nome} já está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode comer enquanto está falando.")
        else:
            print(f"{self.nome} está comendo.")
            self.comendo = True

    def parar_de_comer(self):
        if not self.comendo:
            print(f"{self.nome} não está comendo.")
        else:
            print(f"{self.nome} parou de comer.")
            self.comendo = False

    def falar(self):
        if self.falando:
            print(f"{self.nome} já está falando.")
        elif self.comendo:
            print(f"{self.nome} não pode falar enquanto está comendo.")
        else:
            print(f"{self.nome} está falando.")
            self.falando = True

    def parar_de_falar(self):
        if not self.falando:
            print(f"{self.nome} não está falando.")
        else:
            print(f"{self.nome} parou de falar.")
            self.falando = False

    def dormir(self):
        if self.comendo:
            print(f"{self.nome} não pode dormir enquanto está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode dormir enquanto está falando.")
        else:
            print(f"{self.nome} foi dormir.")




