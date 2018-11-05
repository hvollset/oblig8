class Node:
    def __init__(self, minne, ant_pros):
        self._minne = minne
        self._ant_pros = ant_pros

    def ant_prosessorer_node(self):
        return self._ant_pros

    def nok_minne(self, paakrevd_minne):
        return self._minne >= paakrevd_minne
