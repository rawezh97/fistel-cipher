def stringToBinary(n):
    binary = ''.join(format(ord(n), 'b'))
    if len(binary) == 8:
        return binary
    elif len(binary) == 7 :
        return "0" + binary
    elif len(binary) == 6 :
        return "00" + binary

binary_LIST = []
def encode(the_binary):
    
    
    key_1 = "0110"
    key_2 = "1100"

    bin_part_one = []
    bin_part_two = []

    array_key_1 =[]
    array_key_2 =[]

    #make the key to be in array
    for i in key_1:
        array_key_1.append(i)
    for i in key_2:
        array_key_2.append(i)

    # aplit the 8 bit to 4 per part
    for i in the_binary[:4]:
        bin_part_one.append(i)
    for i in the_binary[4:]:
        bin_part_two.append(i)

    #calculation   0110 0001
    result_part_one = []  
    # print("bin_part_two: ",bin_part_two) #0001
    # print("array_key_1 :" ,array_key_1)  #0110
    # or bin_part2 with key1
    for i in range(0,4):  
        if (array_key_1[i] == "0" and bin_part_two[i] == "0"): # or key eith the secound part of binary
            result_part_one.append("0")
        else :
            result_part_one.append("1")
    # print("result :",result_part_one)

    #   0110  0001
    #   0001 [step1]

    # xor result with the bin_part_one
    step1 = []
    for i in range(0,4):
        if (result_part_one[i] != bin_part_one[i]):
            step1.append("1")
        else:
            step1.append("0")
    # print("first_step :" ,step1)

    #first step do or with key2

    #  0110   0001
    #  0001   0001
    #  0001  [step2]

    result_part_two = []
    for i in range(0,4):
        if (step1[i] == "0" and array_key_2[i] == "0"):
            result_part_two.append("0")
        else:
            result_part_two.append("1")
    #print(result_part_two)

    step2 = []
    for i in range(0,4):
        if (result_part_two[i] != bin_part_two[i]):
            step2.append("1")
        else:
            step2.append("0")
    # print("secound_step :",step2)

    cipher_bin = ''.join(step2) +''.join(step1)
    binary_LIST.append(cipher_bin)

plaintext = input("Enter your word :")
for i in plaintext:
    plaintext = stringToBinary(i)
    # print(plaintext)
    the_binary = plaintext
    encode(the_binary)

print (' '.join(binary_LIST))
