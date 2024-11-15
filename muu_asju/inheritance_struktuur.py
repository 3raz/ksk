# JÄTKE TÄHELEPANUTA EI OLE LÕPUS PROGRAMMEERIMISES

import os
from graphviz import Digraph
import re

def rotate_list(lst, n):
    for i in range(n):
        lst.insert(0, lst.pop())
    return lst

flowchart = Digraph("Inheritance flowchart", filename="inheritance_flowchart", directory=os.getcwd()+"\\muu_asju", format="png")

rootdir = os.getcwd()+"\\ksk"

pattern = r'\(([A-Za-zÄÖÜÕäöüõ]+)\)'

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
for x in range(len(search)):
    for fn in search:
        fn = classes[fn+".py"]
        next_search = []
        with open(fn, 'r', encoding="UTF-8") as f:
            cur = fn.split("\\")[-1][:-3]
            for line in f:
                if "class" in line:
                    parent = re.findall(pattern, line)
                    if parent == []:
                        continue
                    if cur == parent[0] or [cur, parent[0]] in used_pairs:
                        break
                    flowchart.edge(cur, parent[0])
                    used_pairs.append([cur, parent[0]])
                    used_pairs.append([parent[0], cur])
                    next_search.append(parent[0])

    rotate_list(search, 1)
                    


flowchart.render()