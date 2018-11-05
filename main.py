from node import Node
from rack import Rack
from regneklynge import Regneklynge


if __name__ == "__main__":
    abel = Regneklynge(12)
    node1 = Node(64, 1)
    node2 = Node(1024, 2)

    abel.sett_inn_node(node1)

    abel.sett_inn_node(node2)
    print(abel._racks)

    print(abel.noder_med_nok_minne(32))
    print(abel.noder_med_nok_minne(64))
    print(abel.noder_med_nok_minne(128))
