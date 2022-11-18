import networkx as nx
import matplotlib.pyplot as plt
def Plot_graph(branches):
    G=nx.DiGraph()
    edges = "ABCDEF"
    labels = {}
    idx = 0 
    for i in branches:
        G.add_edge(i.start,i.end)
        labels[(i.start,i.end)] = edges[idx]
        idx += 1
    nx.draw_networkx(G , with_labels= True)
    pos = nx.spring_layout(G)
    nx.draw_networkx_edge_labels(G , pos , edge_labels=labels,label_pos=0.5, rotate=False, font_size=8)
    plt.axis('off')
    plt.show()

