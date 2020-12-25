from itertools import permutations as per
def bigest_number(lst):
    """
    процедура находит максимальное число, составленное из чисел в списке
    :param lst:
    :return:
    """
    res_list=[]
    string_list=[str(i) for i in lst]
    for i in per(string_list):
        strig=''
        for j in i:
            strig+=j
            res_list.append(strig)
    print(max(res_list[(len(lst)-1)::len(lst)]))

lst=[1, 10, 77, 2, 4, 3]
bigest_number(lst)
