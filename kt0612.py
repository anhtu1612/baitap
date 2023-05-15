import math
class SINHVIEN:
    def __init__(self, MaSV = "", TenSV = "", NS = ""):
        slef.__MaSV = MaSV
        slef.__TenSV = TenSV
        slef.__NS = NS
    def Nhap(self):
        self.__MaSV = int(input("Nhập mã sinh viên: "))
        while True:
            if self.__MaSV != False:
                print("Mã sinh viên đã tồn tại, vui lòng nhập lại:")
                id = int(input("Nhập mã sinh viên: "))
            else:
                break
        self.__TenSV = input("Nhập tên sinh viên: ")
        self.__NS = int(input("Nhập năm sinh: "))           
    def Xuat(self):
        print("Mã sinh viên: ", self.__MaSV)
        print("Tên sinh viên: ", self.__TenSV)
        print("Năm sinh: ",self.__NS)
    def __lt__(self, other):
        if (self.__NS) < (other.__NS):
            return True
        else:
            return False
list = []
n = int(input("Nhập số sinh viên(tối đa 100 sinh viên): "))
while (n > 100):
    print("Không hợp lệ!!! Vui lòng nhập lại: ")
    n = int(input("Nhập số sinh viên(tối đa 100 sinh viên): "))
for i in range(0,n):
    SINHVIEN.Nhap(self)
for i in range(0,n):
    SINHVIEN.Xuat(self)
