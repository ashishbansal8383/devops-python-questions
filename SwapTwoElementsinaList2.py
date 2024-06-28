
def SwapElements(list, pos1, pos2):
   temp = list[pos1]
   list[pos1] = list[pos2]
   list[pos2] = temp
   return list

##excution
list =  [11,12,13,14,15,16]
pos1, pos2 = 1, 4

print(SwapElements(list, pos1-1, pos2-1))