class fraction :
    def __Init__ (self, real=None, image=None):
        self.x = real
        self.y = image

    def Multiple(self, second):
        result=fraction()
        result.x= self.x * second.x - self.y * second.y
        result.y= self.x * second.y - self.y * second.x
        return result

    def Show(self):
        return str(self.x) +'+('+str(self.y) +')i'

    def Sub(self, second):
        result=fraction()
        result.x= self.x - second.x
        result.y= self.y - second.y
        return result

    def Sum(self, second):
        result=fraction()
        result.x= self.x + second.x
        result.y= self.y + second.y
        return result

Real_1 = int(input('Enter Number 1 (Real) :'))

image_1 = int(input('Enter Number 1 (image) :'))

Real_2 = int(input('\nEnter Number 2 (Real) :'))

image_2 = int(input('Enter Number 1 (image) :'))

Temp_1 = fraction(Real_1,image_1)
Temp_2 = fraction(Real_2,image_2)
print('\nsum: %s\tsub: %s\tmul: %s'% ((Temp_1.Sum(Temp_2)).Show(),(Temp_1.Sub(Temp_2)).Show(),(Temp_1.Multiple(Temp_2)).Show()))