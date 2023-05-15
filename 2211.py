class Htron:
    count = 0.0
    def __init__(self, r = 0.0, x = 0.0, y = 0.0):
        self.__r = r
        self.__x = x
        self.__y = y
        Htron.count = Htron.count + 1
    def Hienthi(self):
        print(self.__r, self.__x, self.__y)
    def Chuvi(self):
        print(self.__r*2*3.14)
    def Dientich(self):
        print(self.__r*self.__r*3.14)
h=Htron(1,2,3)
print(Htron.count)
h.Hienthi()
h.Chuvi()
h.Dientich()

