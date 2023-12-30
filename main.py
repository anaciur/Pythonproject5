import csv
from pyvis.network import Network

from Visualize_Protein_Network import NetworkVisualizer, generate_random_color, rgb_to_hex
from File_processor import InteractionProcessor

graph = Network(notebook=True, cdn_resources="remote", height="600px", width="100%", bgcolor="#ffffff",
                font_color="black")
graph1 = Network(notebook=True, cdn_resources="remote", height="600px", width="100%", bgcolor="#ffffff",
                 font_color="black")
total_proteins = []
total_proteins_nested_list = []


def create_nested_list_of_layers(file_path):
    A = total_proteins_nested_list
    sublist = []
    interaction_processor = InteractionProcessor(file_path)
    interaction_processor.process_interactions()
    # network_visualizer = NetworkVisualizer(interaction_processor.total_proteins)
    new_A = interaction_processor.total_proteins
    for protein in new_A:
        ok = 0
        for l in A:
            for p in l:
                if protein.name == p.name:
                    ok = 1
                    break
        if ok == 0:
            sublist.append(protein)
    total_proteins_nested_list.append(sublist)


def extend_graph(file_path, s, Graph):
    # file_path = 'scaffolds.tsv'
    interaction_processor = InteractionProcessor(file_path)
    interaction_processor.process_interactions()
    # network_visualizer = NetworkVisualizer(interaction_processor.total_proteins)
    total_proteins.extend(interaction_processor.total_proteins)

    # this is a trial
    if Graph == graph1:
        create_nested_list_of_layers(file_path)
    # this is a trial

    random_color = generate_random_color()
    hex_color = rgb_to_hex(*random_color)
    # Add nodes to the network
    for protein in total_proteins:
        Graph.add_node(protein.name, label=protein.name, shape="dot", size=s, color=hex_color)
    # Add edges to the network
    for protein in total_proteins:
        for interacting_protein in protein.interactions:
            Graph.add_edge(protein.name, interacting_protein.name,
                           label=protein.interactions[interacting_protein],
                           title=protein.interactions[interacting_protein])


extend_graph('scaffolds.tsv', 30, graph1)
extend_graph('scaffolds#.tsv', 30, graph1)

extend_graph('scaffolds.tsv', 30, graph)
extend_graph('2nd_layer.tsv', 27, graph)
extend_graph('3rd_layer.tsv', 25, graph)
extend_graph('4th_layer.tsv', 20, graph)

extend_graph('combined_file_all.tsv', 15, graph)
extend_graph('6th_layer.tsv', 12, graph)
extend_graph('7th_layer.tsv', 10, graph)
extend_graph('8th_layer.tsv', 9, graph)
for lst in total_proteins_nested_list:
    print(f"layer {total_proteins_nested_list.index(lst)}")
    print(','.join(pr.name for pr in lst))
    print(f"{len(lst)}")
# Set the physics configuration to enable node dragging
graph.set_options(
    """
    var options = {
        "physics": {
            "enabled": true,
            "barnesHut": {
                "springLength": 100
            }
        }
    }
    """
)

# Show the graph

# Render the graphs into the HTML
graph.show("main.html")
graph1.show("main.html")


def main():
    '''file_path = 'scaffolds.tsv'

    # Task 1: Interaction Processing

    # filter through the file_path, and create a dictionary of each 2 proteins + the likelihood of their interaction
    interaction_processor = InteractionProcessor(file_path)
    interaction_processor.process_interactions()

    # Task 2: Network Visualization
    network_visualizer = NetworkVisualizer(interaction_processor.total_proteins)
    network_visualizer.visualize_network()'''

    QDPR_file_path = 'QDPR.tsv'

# if __name__ == "__main__":
# main()
# Press the green button in the gutter to run the script.
