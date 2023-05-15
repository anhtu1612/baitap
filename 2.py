#Viết chương trình xác định chữ số cuối của phép tính Lamda = a*b*c*d với bốn số nguyên a,b,c,d cho trước.
#dòng duy nhất chứa bốn số nguyên a,b,c,d cách nhau ký tự trắng, thoả điều kiện 2 <= a,b,c,d <= 10^9
a,b,c,d = map(int,input("Nhập a,b,c,d: ").split())
hangchuc = 0
hangdonvi = 0
tich = a*b*c*d
hangdonvi = tich%10
tich = tich/10
hangchuc = tich/10
if hangchuc != 0:
    print("Chữ số cuối của phép tính là: ",hangchuc,hangdonvi)
else :
    print("Chữ số cuối của phép tính là: ",hangdonvi)
