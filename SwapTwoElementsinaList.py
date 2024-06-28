def SwapElements(list, pos1, pos2):
   list[pos1], list[pos2] = list[pos2], list[pos1]
   return list

list = [21, 22, 23, 24, 25]
pos1 = 2
pos2 = 5

print(SwapElements(list, pos1-1, pos2-1))
