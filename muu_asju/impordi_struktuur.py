# JÄTKE TÄHELEPANUTA EI OLE LÕPUS PROGRAMMEERIMISES

import os
from graphviz import Digraph

flowchart = Digraph("Import flowchart", filename="import_flowchart", format="png")

rootdir = os.getcwd()+"\\ksk"

classes = {}
search = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file[-3:] == ".py" and "temp" not in file:
            classes[file] = os.path.join(subdir, file)
            flowchart.node(file[:-3])
            search.append(file[:-3])

print(search)

def create_chart(start):
    next_search = []
    with open(start, 'r', encoding="UTF-8") as f:
        cur = start.split("\\")[-1][:-3]
        for line in f:
            if "import" in line:
                for key in search:
                    if key in line:
                        if cur == key:
                            break
                        flowchart.edge(cur, key)
                        next_search.append(key)
    if next_search == []:
        return
    for x in next_search:
        create_chart(classes[x+".py"])
    
                        
create_chart(classes["main.py"])


flowchart.render()