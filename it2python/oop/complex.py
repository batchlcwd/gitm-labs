class ComplexNum:
    def __init__(self,x,y):
        self.x=x 
        self.y=y 

    def show(self):
        print(f'( {self.x} , {self.y}i )')
    
    def add(self,num2):
        real=self.x+num2.x 
        img=self.y+num2.y 
        return ComplexNum(real,img)
    

def main():
    num1=ComplexNum(5,7)
    num1.show()
    num3=ComplexNum(2,8)
    num3.show()

    resultNum=num1.add(num3)
    resultNum.show()


if __name__=='__main__':
    main()