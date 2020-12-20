def bigest_number(lst):
    another_list = sorted([str(i) for i in lst], reverse=True)
    max_number=''
    for i in another_list:
        max_number+=i
    print(max_number)

lst=[1, 9, 44, 102, 7, 102]
bigest_number(lst)
