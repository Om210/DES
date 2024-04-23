def exp_mapping(num, order):
    bin_a = format(num, '032b')  
    binary_array = [int(i) for i in bin_a]  
    mapped_order = [0] * 48
    for j in range(len(order)):
        mapped_order[j] = binary_array[order[j] - 1]
    return mapped_order
