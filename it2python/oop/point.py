import math
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y 
        print("Point Created: ")

    def show(self):
        print("( ",self.x,",",self.y," )")
    
    def calc_distance(self,point2):
        powers=math.pow((self.x-point2.x),2)+math.pow((self.y-point2.y),2)

        result=math.sqrt(powers)
        return result

    def print_mid_point(self,point2):
        midx=(self.x+point2.x)/2
        midy=(self.y+point2.y)/2
        midPoint=Point(midx,midy)
        return midPoint
        




#point 1
        
point1= Point(4,6)
point1.show()
print(type(point1))

point2=Point(89,32)

point2.show()

dis=point1.calc_distance(point2)
print("distance ",dis)

point3=Point(4,6)
point4=Point(6,7)
result=point3.calc_distance(point4)
point3.show()
point4.show()
print("distance ",result)

point3.print_mid_point(point4)

p5=Point(10,10)
p6=Point(1,1)

midPoint=p5.print_mid_point(p6)
midPoint.show()

result1=midPoint.calc_distance(p5)
print(result1)