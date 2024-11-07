# JÄTKE TÄHELEPANUTA EI OLE LÕPUS PROGRAMMEERIMISES

import os
from graphviz import Digraph

flowchart = Digraph("Inheritance Flowchart", filename="inheritance_flowchart", format="png")

rootdir = os.getcwd()+"\\ksk"

classes = {}
search = []
for subdir, dirs, files in os.walk(rootdir):
    for file in files:
        if file[-3:] == ".py" and "temp" not in file:
            classes[file] = os.path.join(subdir, file)
            flowchart.node(file[:-3])
            search.append(file[:-3])

with open(os.path.join(rootdir,"main.py"), 'r', encoding="UTF-8") as f:
    for line in f:
        line = line.lower()
        if "import" in line:
            print(line)
            for key in search:
                if key in line:
                    print("main", key)
                    flowchart.edge("main", key)


flowchart.render()