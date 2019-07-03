import pandas as pd
import json
import requests
import urllib.request
import numpy as np
from SPARQLWrapper import SPARQLWrapper, JSON

base_url = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0"
result_format = "json"

df = pd.read_csv("https://raw.githubusercontent.com/foerstner-lab/Publication_list/master/Publications.tsv", sep="\s")

desired_width=320
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns',10)

def main():
    df["PMID"] = df.DOI.apply(doi_to_pmid)
    df["PMCID"] = df.DOI.apply(doi_to_pmcid)
    df["Wikidata_item_identifier"] = df.DOI.apply(doi_to_wikiID)
    df["Titel"] = df.DOI.apply(test)
    print(df)

def doi_to_pmid(doi):
    full_url = f"{base_url}?ids={doi}&format={result_format}"
    request_data_of_doi = urllib.request.urlopen(full_url).read()
    result_of_doi_as_dict = doi_data = json.loads(request_data_of_doi)
    
    try:
        for result_pmid in result_of_doi_as_dict["records"]:
            return result_pmid["pmid"]
    except:
        pass

def doi_to_pmcid(doi):
    full_url = f"{base_url}?ids={doi}&format={result_format}"
    request_data_of_doi = urllib.request.urlopen(full_url).read()
    result_of_doi_as_dict = doi_data = json.loads(request_data_of_doi)
    try:
        for result_pmcid in result_of_doi_as_dict["records"]:
            return result_pmcid["pmcid"]
    except:
        pass


def doi_to_wikiID(doi):
    endpoint_url = "https://query.wikidata.org/sparql"
    query_header = "SELECT ?item ?itemLabel  "
    query_condition = 'WHERE{ ?item wdt:P356 "' + doi.upper() + '".'
    query_tail = """}"""
    generated_query = query_header + query_condition + query_tail
    sparql = SPARQLWrapper(endpoint_url)
    sparql.setQuery(generated_query)
    sparql.setReturnFormat(JSON)
    sparql_data = sparql.query().convert()
    try:
        for result in sparql_data["results"]["bindings"]:
            q_id = result["item"]["value"]
            q_id_split = q_id.split("http://www.wikidata.org/entity/")
            return "".join(q_id_split)
    except:
        pass


def test(doi):
    url = "https://api.crossref.org/works/"
    doi_json_data = urllib.request.urlopen(url + doi).read()
    json_data_content = json.loads(doi_json_data)
    return "".join(json_data_content["message"]["title"])
