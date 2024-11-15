# JÄTKE TÄHELEPANUTA EI OLE LÕPUS PROGRAMMEERIMISES

import os
from graphviz import Digraph
import re

flowchart = Digraph("Import flowchart", filename="import_flowchart", directory=os.getcwd()+"\\muu_asju", format="png")

rootdir = os.getcwd()+"\\ksk"

classes = {}
search = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file[-3:] == ".py" and "temp" not in file and file != "__init__.py":
            classes[file] = os.path.join(subdir, file)
            flowchart.node(file[:-3])
            search.append(file[:-3])

print(search)

used_pairs = []

def create_chart(start, trigger=True):
    next_search = []
    if trigger:
        next_search = search.copy()
        trigger = False
    with open(start, 'r', encoding="UTF-8") as f:
        cur = start.split("\\")[-1][:-3]
        for line in f:
            line = line
            if "import" in line:
                for key in search:
                    if key in line:
                        if cur == key or [cur, key] in used_pairs:
                            break
                        flowchart.edge(cur, key)
                        used_pairs.append([cur, key])
                        used_pairs.append([key, cur])
                        next_search.append(key)
    if next_search == []:
        return
    for x in next_search:
        create_chart(classes[x+".py"], trigger=trigger)
    
                        
create_chart(classes["main.py"])


flowchart.render()