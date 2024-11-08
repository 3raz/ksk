# JÄTKE TÄHELEPANUTA EI OLE LÕPUS PROGRAMMEERIMISES

import os
from graphviz import Digraph





def rotate_list(lst, n):
    for i in range(n):
        lst.insert(0, lst.pop())
    return lst

flowchart = Digraph("Inheritance flowchart", filename="inheritance_flowchart", format="png")

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

used_pairs = []
for x in range(len(search)):
    for fn in search:
        fn = classes[fn+".py"]
        next_search = []
        with open(fn, 'r', encoding="UTF-8") as f:
            cur = fn.split("\\")[-1][:-3]
            for line in f:
                if "class" in line:
                    for key in search:
                        if key in line:
                            if cur == key or [cur, key] in used_pairs:
                                break
                            flowchart.edge(cur, key)
                            used_pairs.append([cur, key])
                            used_pairs.append([key, cur])
                            next_search.append(key)

    rotate_list(search, 1)
    print(search)
                    


flowchart.render()