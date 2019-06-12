import pandas as pd
import json
from SPARQLWrapper import SPARQLWrapper, JSON
from pyvis.network import Network

class NetworkPlotter():
    def __init__(self, qid, filters, show):
        self.qid = qid
        self.filters = filters
        self.show = show

    def generate_query(self):
        query_header = "SELECT DISTINCT ?srna ?srnaLabel ?target ?targetLabel "
        query_condition = "WHERE{ ?srna wdt:P31 wd:" + self.filters + ". ?srna wdt:P31 wd:" + self.qid + ". ?srna wdt:" + self.show + " ?target."
        query_tail = """SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE], en". }}"""
        generated_query = query_header + query_condition + query_tail
        self.query = generated_query

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

qid = 'Q11053'
filters = 'Q427087'
show = 'P128'

plot_network = NetworkPlotter(qid, filters, show)
plot_network.generate_query()
plot_network.get_data()
plot_network.plot_graph()
