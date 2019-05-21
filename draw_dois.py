import urllib.request
import json
import networkx as nx
import matplotlib.pyplot as plt

# the program defines what arguments it requires, figures out how to parse
# automatically generates help and usage messages and issues errors when
# users give the program invalid arguments
import argparse


# get from reference dois'
def get_dois(doi):
    url = "https://api.crossref.org/works/"
    doi_json_data = urllib.request.urlopen(url + doi)
    doi_json_data_content = doi_json_data.read()
    doi_data = json.loads(doi_json_data_content)
    ref_doi_lst = [] # empty list
    for reference in doi_data["message"]["reference"]:
        try:
            ref_doi_lst.append(reference["DOI"]) # fügt in die liste die dois aus der reference
        except KeyError:
            pass
    return ref_doi_lst # returns list of dois


def draw_graph(doi):
    doi_lst = get_dois(doi)

    try:
        for new_doi in doi_lst:
            G.add_edge(doi, new_doi)
        for i in doi_lst:              # recursion: function calls itself
            draw_graph(i)
    except:
        pass


def arg_parse():
    parser = argparse.ArgumentParser(description='network of dois')
    parser.add_argument('-d', '--doi', type=str, required=True, help='start with a doi')
    params = parser.parse_args()
    return params


if __name__ == '__main__':
    params = arg_parse()
    G = nx.Graph()          # empty graph

    # man beginnt mit einem Knoten und fügt danach erst mehrere hinzu
    G.add_node(params.doi)  # add dois' as nodes- Knoten

    draw_graph(params.doi)
    nx.draw(G)
    plt.savefig('doi_graph.pdf')  # save graph as pdf file

# doi = "10.1371/journal.pcbi.1004668" -






