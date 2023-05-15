def So(n):
    dem = 0
    for i in n:
        if i.isnumeric():
            dem = dem + 1
    return dem
n = input("Nhập số nguyên n: ")
print ("Số lượng ký tự số có trong n là: ", So(n))

