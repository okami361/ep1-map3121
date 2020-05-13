from dataclasses import dataclass
from typing import List

@dataclass
class PlotData:
    tempo : float
    datas : List[float]

    def __init__(self, tempo, datas):
        self.tempo = tempo
        self.datas = datas