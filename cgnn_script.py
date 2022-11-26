import pandas as pd
#import numpy as np
import re
import networkx as nx
df = pd.read_csv('unit_cell_catalog2000.csv')

column_names = df.columns.values.tolist()
column_dict = {}
for i in column_names:
    column_dict[column_names.index(i)] = i

nodal_shape = df.iloc[: , column_names.index("Nodal_nrow"):column_names.index("Nodal_ncol")+1]

bar_shape = df.iloc[: , column_names.index("Bar_nrow"):column_names.index("Bar_ncol")+1]

nodal_positions = pd.DataFrame()
bar_connectivity = pd.DataFrame()
first_nodes = pd.DataFrame()
second_nodes = pd.DataFrame()
for index, column_name in column_dict.items():
    if re.search("^nodal_positions", column_name):
        nodal_positions[column_name] = df.iloc[: , index]

        node_number = re.search(r"^nodal_positions_(\d?)", column_name)
        print(node_number)
        globals()['']


    if re.search("^bar_connectivity", column_name):
        bar_connectivity[column_name] = df.iloc[: , index]
        if column_name.endswith("1"):
            first_nodes[column_name] = df.iloc[: , index]
        if column_name.endswith("2"):
            second_nodes[column_name] = df.iloc[: , index]

def edge_length():
    pass
edge_length()