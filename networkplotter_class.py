import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON
from pyvis.network import Network

class NetworkPlotter():
    def __init__(self, query):
        self.query = query

    def get_data(self):
        sparql = SPARQLWrapper('https://query.wikidata.org/sparql')
        sparql.setQuery(self.query)
        sparql.setReturnFormat(JSON)
        data = sparql.query().convert()
        result = pd.io.json.json_normalize(data['results']['bindings'])
        self.result = result

    def plot_graph(self):
        net = Network()

        srna = self.result['srnaLabel.value']
        target = self.result['targetLabel.value']
        source = self.result['srna.value']

        edge_data = zip(srna, target, source)

        for e in edge_data:
            srna = e[0]
            target = e[1]
            src = e[2]

            net.add_node(srna, title=srna)
            net.add_node(target, title=target)
            net.add_edge(srna, target, title=src)

        return net.show('networkplotter.html')
