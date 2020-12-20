def bigest_number(lst):
    another_list = sorted([str(i) for i in lst], key=lambda i:len(i), reverse=False)
    max_number=''
    for i in another_list:
        max_number+=i
    print(max_number)

lst=[1, 12, 7777777]
bigest_number(lst)
