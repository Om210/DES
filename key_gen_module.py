# Converting the 64-bits key to 56-bit
def parity_drop(num, order):
    bin_a = format(int(num,16), '064b')  
    binary_array = [int(i) for i in bin_a]  
    mapped_order = [0]*56
    for j in range(len(order)):
        mapped_order[j] = binary_array[order[j] - 1]  
    return mapped_order

parity_drop_matrix = [57, 49, 41, 33, 25, 17, 9, 1,
                      58, 50, 42, 34, 26, 18, 10, 2,
                      59, 51, 43, 35, 27, 19, 11, 3,
                      60, 52, 44, 36, 63, 55, 47, 39,
                      31, 23, 15, 7, 62, 54, 46, 38,
                      30, 22, 14, 6, 61, 53, 45, 37,
                      29, 21, 13, 5, 28, 20, 12, 4]

# Converting the 56-bits key to 48-bits 
def compression_p(num, order):
    binary_array = [int(i) for i in num]  
    mapped_order = [0]*48
    for j in range(len(order)):
        mapped_order[j] = binary_array[order[j] - 1] 
    return mapped_order

# compression P box mapping order
comp_p = [14, 17, 11, 24, 1, 5, 3, 28,
          15, 6, 21, 10, 23, 19, 12, 4,
          26, 8, 16, 7, 27, 20, 13, 2,
          41, 52, 31, 37, 47, 55, 30, 40,
          51, 45, 33, 48, 44, 49, 39, 56,
          34, 53, 46, 42, 50, 36, 29, 32]

# KEY GENERATION
def gen_key():
    key_hex = input("Enter the key in hexadecimal format: ")

    after_parity_drop = parity_drop(key_hex, parity_drop_matrix)

    #convert the array to string
    after_parity_drop_binary =''.join(map(str, after_parity_drop))

    keyl = after_parity_drop_binary[:28]
    keyr = after_parity_drop_binary[28:56]

    keys = [0]*16
         
    for i in range(16):
        if i == 0 or i == 1 or i == 8 or i == 15:
            keyl = keyl[1:28] + keyl[0]
            keyr = keyr[1:28] + keyr[0]
        else:
            keyl = keyl[2:28] + keyl[:2]
            keyr = keyr[2:28] + keyr[:2]
        keyy = keyl + keyr
        keyy = compression_p(keyy, comp_p)
        keys[i] =''.join(map(str, keyy))
    return keys

