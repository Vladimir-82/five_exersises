def most_pop(lst):
    '''
    функция ищет и возвращает наиболее часто встречаеммый элемент списка
    или возвращает,, что такого символа нету
    :param lst:
    :return:
    '''
    counter=[]
    res=[]
    for i in lst:
        counter.append(lst.count(i))
    for i in range(len(lst)):
        if counter.count(counter[i])==max(counter):
            res.append(lst[i])
    if len(res) >= 1:
        return res[0]
    else:
        return 'нет элемента, который встречается чаще всего в списке'


lst=['a', [5], 6, 'a', 7, [5], [5], 'a']
print(most_pop(lst))