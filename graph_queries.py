import networkx as nx
G = nx.read_graphml('/root/articles_graph.graphml')

def get_articles_about(topic):
    for u,v,d in G.edges(data=True):
        if d.get('type') == 'ABOUT' and topic.lower() in v.lower():
            print(G.nodes[u].get('title','')[:80])

def get_persons():
    for n,d in G.nodes(data=True):
        if d.get('label') == 'Person':
            print(f"{d.get('name')}: {d.get('party')}")

def get_locations():
    for n,d in G.nodes(data=True):
        if d.get('label') == 'Location':
            print(f"{d.get('name')} ({d.get('type')})")

if __name__ == "__main__":
    print("Articles about Weather:")
    get_articles_about("Weather")
    print("Persons:")
    get_persons()
