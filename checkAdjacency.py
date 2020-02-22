#Adjacentcy returns # of adjacent black. Black is +, white is -
import math

def get_neighbour_number(str_puzzle, char_index):
    num_white = 0
    num_black = 0

    n_size = math.sqrt(len(str_puzzle))
#    print("string length: " + str(len(str_puzzle)))
#    print("n-size: "+str(int(n_size)))
#    print("piece on index: "+str_puzzle[char_index])
    if (str_puzzle[char_index] == "0"):
        num_white += 1
    else:
        num_black += 1
#    print("piece index: " + str(char_index))

    if(((char_index% n_size))>0):
#        print("left from index is index: "+ str(char_index -1))
#        print("piece: " + str_puzzle[char_index -1])
        if(str_puzzle[char_index -1] == "0"):
            num_white += 1
        else:
            num_black += 1

    if (((char_index+1) % n_size) >0):
#        print("right from index is index: " + str(char_index + 1))
#        print("piece: " + str_puzzle[char_index + 1])
        if (str_puzzle[char_index + 1] == "0"):
            num_white += 1
        else:
            num_black += 1


    if (((char_index-n_size)) >=0):
#        print("top from index is index: " + str(int((char_index-n_size))))
#        print("piece: " + str_puzzle[int(char_index-n_size)])
        if (str_puzzle[int(char_index-n_size)] == "0"):
            num_white += 1
        else:
            num_black += 1

    if (((char_index+ (n_size))< len(str_puzzle))):
#        print("bot from index is index: " + str((char_index+ (n_size))))
#        print("piece: " + str_puzzle[int(char_index+ (n_size))])
        if (str_puzzle[int(char_index+ (n_size))] == "0"):
            num_white += 1
        else:
            num_black += 1

    ratio = num_white-num_black  # 1 more white, return -1
#    print("black pieces: "+ str(num_black))
#    print("white pieces: "+ str(num_white))

#    print("blk-white ratio: "+str(ratio))
  #  h_pt = ratio*h_weight
    return ratio ##don't wnat a - heuristic

#heuristic_pt = get_neighbour_number("0110111100010101", 4) #heuristic is 13.33
heuristic_pt = get_neighbour_number("0110111100010101", 7) #heuristic is 0
#heuristic_pt = get_neighbour_number("111101111", 4) #heuristic is 0

#0110->3
#1111->7
#0001->11
#0101->15

print("heuristic: "+ str(heuristic_pt))