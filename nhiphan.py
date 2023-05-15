
def kt(x):
    p_set = set(x)
    s_set = {'0','1'}
    if (p_set == s_set or p_set == {'0'} or p_set == {'1'}):
        print ("Chuỗi trên là chuỗi nhị phân")
    else: print("Chuỗi trên không phải là chuỗi nhị phân")
p = (input("Nhập chuỗi để kiểm tra: "))
kt(p)
