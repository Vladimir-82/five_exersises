def comb_1(lst1, lst2):
    '''
    распаковка значений массивов в один массив
    :param lst1:
    :param lst2:
    :return:
    '''
    lst=[]
    for i in range(len(lst1)):
        lst.append(lst1[i])
        lst.append(lst2[i])
    return lst

def comb_2(lst1, lst2):
    return list(zip(lst1, lst2))

lst1=[1, 2, 3]
lst2=[11, 22, 33]
print(comb_1(lst1, lst2))
print(comb_2(lst1, lst2))