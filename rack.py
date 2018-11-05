from node import Node


class Rack:
    def __init__(self):
        self._noder = []

    def sett_inn(self, node):
        self._noder.append(node)

    def get_ant_noder(self):
        return len(self._noder)

    def ant_prosessorer_rack(self):
        prosessorer = 0
        for node in self._noder:
            prosessorer += node.ant_prosessorer_node()
        return prosessorer

    def noder_med_nok_minne(self, paakrevd_minne):
        gode_noder = 0
        for node in self._noder:
            if node.nok_minne(paakrevd_minne):
                gode_noder += 1
            else:
                gode_noder += 0
