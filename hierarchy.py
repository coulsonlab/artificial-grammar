import numpy as np

def generate_control(elements, length):
    sequence = []
    for i in range(length):
        rand_element = elements[np.random.randint(len(elements))]
        sequence.append(rand_element)
    return sequence
    
def generate_local(pairs, length):
    sequence = []
    count = 0
    while count < length:
        rand_ele_1, rand_ele_2 = pairs[np.random.randint(len(pairs))]
        sequence.append(rand_ele_1)
        sequence.append(rand_ele_2)
        count += 2
    return sequence
    
def generate_nested(pairs, length):
    if length <= 0:
        return []
    else:
        rand_ele_1, rand_ele_2 = pairs[np.random.randint(len(pairs))]
        sequence = [rand_ele_1]
        sequence += generate_nested(pairs, length-2)
        sequence.append(rand_ele_2)
        return sequence
    
def generate_crossed(pairs, length):
    selected_pairs = []
    count = 0
    while count < length:
        selected_pairs.append(pairs[np.random.randint(len(pairs))])
        count += 2
        
    sequence = []
    for ele_1, _ in selected_pairs:
        sequence.append(ele_1)
    for _, ele_2 in selected_pairs:
        sequence.append(ele_2)
    return sequence