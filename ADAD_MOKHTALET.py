class complex :

    def __init__(self, real=None, image=None):
        self.x = real
        self.y = image
        
    def sub(self, second):
        result=complex()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result

    def sum(self, second):
        result=complex()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result

    def multiple(self, second):
        result=complex()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result

    def show(self):
        return str(self.x) +'+('+str(self.y) +')i'

    print('Enter Complex Number 1 :')
    Real_1 = int(input('Enter (Real) :'))
    Image_1 = int(input('Enter (Image) :'))
    Number_1 = complex(Real_1,Image_1)

    print('Enter Complex Number 2 :')
    Real_2 = int(input('Enter (Real) :'))
    Image_2 = int(input('Enter (Image) :'))
    n2 = complex(Real_1, Image_2)

    while True:

        print("\n1.Add")
        print("2.Sub")
        print("3.Mul")
        print("4.Exit")

        c = int(input())
        
        if c==1:
            print(Number_1.sum(n2).show())
        if c==2:
            print(Number_1.sub(n2).show())
        if c==3:
            print(Number_1.multiple(n2).show())
        if c==4:
            break