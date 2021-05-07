from hierarchy import generate_control, generate_local, generate_nested, generate_crossed

elements = ['A', 'B', 'C']
pairs = [('A1', 'A2'), ('B1', 'B2'), ('C1', 'C2')]

print(generate_control(elements, 6))
print(generate_local(pairs, 6))
print(generate_nested(pairs, 6))
print(generate_crossed(pairs, 6))