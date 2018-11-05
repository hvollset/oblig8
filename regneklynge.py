from rack import Rack
from node import Node


class Regneklynge:
    def __init__(self, noder_per_rack):
        self._noder_per_rack = noder_per_rack
        self._racks = []

    def sett_inn_node(self, node):
        for rack in self._racks:
            if rack.get_ant_noder() < self._noder_per_rack:
                rack.sett_inn(node)
                break
            else:
                new_rack = Rack()
                new_rack.sett_inn(node)
                self._racks.append(new_rack)
                break

    def ant_prosessorer(self):
        pass

    def noder_med_nok_minne(self, paakrevd_minne):
        node_count = 0
        for rack in self._racks:
            count = rack.noder_med_nok_minne(paakrevd_minne)
            node_count += count
        return node_count

    def ant_racks(self):
        pass
