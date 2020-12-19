def sum_for(lst):
    '''
    сумма числе циклом for
    :param lst:
    :return:
    '''
    summory=0
    for i in range(len(lst)):
        summory+=lst[i]
    return summory

def sum_while(lst):
    '''
    сумма числе циклом while
    :param lst:
    :return:
    '''
    summory=0
    i=0
    while i<len(lst):
        summory+=lst[i]
        i+=1
    return summory

def sum_recursia(lst):
    '''
    сумма числе циклом рекурсия
    :param lst:
    :return:
    '''
    i=len(lst)
    if i==1:
        return lst[0]
    else:
        return lst[0] + sum_recursia(lst[1::])

lst=[10,2,3,4]
print(sum_for(lst))
print(sum_while(lst))
print(sum_recursia(lst))
