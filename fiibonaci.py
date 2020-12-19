def fibonaci(limit):
    """
    числа Фибоначи до 100
    :param limit:
    :return:
    """
    c = 0
    a = 0
    b = 1
    lst = []
    while c <= limit:
        c = a + b
        lst.append(c)
        a = b
        b = c

    return lst[:-1:]

lim = 100
print(fibonaci(lim))