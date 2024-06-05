class Sum:
    def __init__(self):
        print("Sum object created:")

    # def do_sum(self,x,y,z):
    #     print("sum --",(x+y))

    def do_sum(self,x,y,z=0):
        if z==0:
            # do arguement
            pass 
        print("sum",(x+y+z))






ob1=Sum()
ob1.do_sum(30,60,123)
ob1.do_sum(2,4,6)





