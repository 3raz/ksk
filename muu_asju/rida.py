import os
import ast

def analyze_python_file(file_path):
    """Analyze a single Python file to count classes, functions, and lines."""
    with open(file_path, "r", encoding="utf-8") as file:
        tree = ast.parse(file.read())

    num_functions = len([node for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)])
    num_classes = len([node for node in ast.walk(tree) if isinstance(node, ast.ClassDef)])
    num_lines = sum(1 for line in open(file_path, encoding="utf-8"))

    return num_lines, num_functions, num_classes

root_dir = "./"

total_lines = 0
total_functions = 0
total_classes = 0

for root, _, files in os.walk(root_dir):
    for file in files:
        if file.endswith(".py"):
            if "rida" in file:
                continue
            file_path = os.path.join(root, file)
            lines, functions, classes = analyze_python_file(file_path)
            print(f"{file_path}: {lines} lines, {functions} functions, {classes} classes")
            total_lines += lines
            total_functions += functions
            total_classes += classes

print("\n--- Projekti kokkuvõte ---")
print(f"Koodiridade koguarv: {total_lines}")
print(f"Funktsioonide koguarv: {total_functions}")
print(f"Klasside koguarv: {total_classes}")

