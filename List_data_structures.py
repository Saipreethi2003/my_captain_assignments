L1 = ['Maths', 'physics', 5, 7] 
L1.append(9) 
print(L1)
L1.insert(2, 3) 
print(L1)  
L2 = ['chemistry', 9]
L1.extend(L2)     
print(L1) 
List = [1, 2, 3, 4, 5, 2, 3, 1, 1, 7, 1, 5, 1, 3, 1] 
print(sum(List)) 
print(List.count(1))
print(len(List))
print(List.index(2))    
print(min(List))
print(max(List))
List.sort(reverse=True)
print(List)
sorted(List)
print(List)
print(List.pop())
del List[0] 
print(List)
List.remove(3)
print(List)
