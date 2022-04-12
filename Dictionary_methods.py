dic = {1:'ant', 2:'bat', 3:'cat', 4:'dog', 5:'eagle'}
print('original: ', dic)
print(dic.get(1))
print(dic.keys())
print(dic.values())
print(dic.items())
print(dic.values())
print(dic.popitem())
abc = dic.copy()
print("copied dictionary : ", abc)
Second_value = dic.setdefault('2')
print("2nd value: ", Second_value)
pop_two = dic.pop(2)
print('Dictionary after deletion: ', dic)
dic1 = {3:'kangaroo'}
dic.update(dic1)
print("Dictionary after updating : ", dic)
dic.clear() 
print("dic : ", dic)
alp = {'a', 'b', 'c', 'd', 'e'}
l1 = [1, 2]
fin_dic = dict.fromkeys(alp, l1)
print("The newly created dict with list values : ", fin_dic)

 
 
