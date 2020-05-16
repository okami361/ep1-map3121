from dataclasses import dataclass

@dataclass
class ExercicioData:
    nome : str
    f : object
    u0 :object
    g1 :object
    g2 :object
    f_exato :object

    def __init__(self, nome, f, u0, g1, g2, f_exato):
        self.nome = nome
        self.f = f
        self.u0 = u0
        self.g1 = g1
        self.g2 = g2
        self.f_exato = f_exato