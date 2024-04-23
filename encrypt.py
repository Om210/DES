from key_gen_module import gen_key
from exp_map_module import exp_mapping
from ip_fp_module import mapped
from s_box_module import s_box

# Initial permutation mapping order
ip_mapping_order = [58, 50, 42, 34, 26, 18, 10, 2,
                    60, 52, 44, 36, 28, 20, 12, 4,
                    62, 54, 46, 38, 30, 22, 14, 6,
                    64, 56, 48, 40, 32, 24, 16, 8,
                    57, 49, 41, 33, 25, 17, 9, 1,
                    59, 51, 43, 35, 27, 19, 11, 3,
                    61, 53, 45, 37, 29, 21, 13, 5,
                    63, 55, 47, 39, 31, 23, 15, 7]

# Final Permutation Table
final_perm = [40, 8, 48, 16, 56, 24, 64, 32,
              39, 7, 47, 15, 55, 23, 63, 31,
              38, 6, 46, 14, 54, 22, 62, 30,
              37, 5, 45, 13, 53, 21, 61, 29,
              36, 4, 44, 12, 52, 20, 60, 28,
              35, 3, 43, 11, 51, 19, 59, 27,
              34, 2, 42, 10, 50, 18, 58, 26,
              33, 1, 41, 9, 49, 17, 57, 25]

# expansion p box mapping order
exp_p_box = [32, 1, 2, 3, 4, 5, 
             4, 5, 6, 7, 8, 9, 
             8, 9, 10, 11, 12, 13,
             12, 13, 14, 15, 16, 17, 
             16, 17, 18, 19, 20, 21, 
             20, 21, 22, 23, 24, 25, 
             24, 25, 26, 27, 28, 29, 
             28, 29, 30, 31, 32, 1]

# DES PLAIN TEXT ENCRYPTION
def encrypt_text():
    # Input plain text (64-bits max), plain text is just numbers and not alphabets etc.
    plain_text = input("A Enter a hexadecimal number of size 64-bits max: ")

    # Convert it to binary
    try:
        pt_binary = format(int(plain_text, 16), '064b')
    except ValueError:
        print("Invalid hexadecimal input. Please enter a valid hexadecimal number.")
        exit()

    # Initial permutation is the first step
    ip = mapped(int(pt_binary, 2), ip_mapping_order)
    ip_binary = ''.join(map(str, ip))
    #----------------------------------------------------------------------------------------
    keys = gen_key()
    # ROUND
    #------------
    # function f(R, K)
    bin_l = ip_binary[0:32]
    bin_r = ip_binary[32:]
    for j in range (0, 16):
        exp_bin_r = exp_mapping(int(bin_r,2), exp_p_box)
        exp_bin_r_1 = ''.join(map(str, exp_bin_r))
        s_boxop = ''.join(map(str, s_box(exp_bin_r_1, keys[j])))
        if (j!=15):
            bin_l_1 = bin_r
            bin_r = format(int(s_boxop, 2) ^ int(bin_l, 2), '032b')
            bin_l = bin_l_1
        else:
            bin_l = format(int(s_boxop, 2) ^ int(bin_l, 2), '032b')
        
    #------------

    # AFTER GETTING THE FINAL ROUND OUTPUT  
    final = bin_l + bin_r
    fp = mapped(int(final, 2), final_perm)
    fp_binary = ''.join(map(str, fp))
    print("The cipher text: ")
    print(format(int(fp_binary, 2), 'X'))

