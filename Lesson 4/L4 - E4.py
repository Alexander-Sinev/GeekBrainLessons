from itertools import permutations
from itertools import repeat
from itertools import combinations
my_list = [5, 2, 7, 2, 8, 9, 1, 5, 7]
new = [el for el in my_list if my_list.count(el)==1]
print(new) 
