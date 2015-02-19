import math

class triangular_mem:

    def __init__(self,a,b,c):

        self.low = float(a)
        self.mid = float(b)
        self.hi  = float(c)

    def value(self,x):

        if x <= self.low:
            return 0.0
        if x <= self.mid and x >= self.low:
            return float(x-self.lo)/(self.mid-self.lo)
        if x <= self.hi and x >= self.mid:
            return float(self.hi-x)/(self.hi-self.mid)
        return 0.0
        


class gaussmf:

    def __init__(self,a,b):

        self.sig = float(a)
        self.c = float(b)

    def value(self,x):
        sq = -(x-self.c)*(x-self.c)
        sigma = 2*self.sig*self.sig
        return math.pow(math.e,sq/sigma)



class flc_triangular:

    def __init__(self,a,b,c): ##  a = 0 for origin start

        self.low = float(a)
        self.mid = float(b)
        self.hi  = float(c)


    def value(self,x):
        
        if x <= self.low:
            return {"low":0.0,"mid":0.0,"hi":0.0} ## Value for the three zones
        elif x <= self.mid and x >= self.low:
            return {"low":float(self.mid-x)/(self.mid-self.low), "mid":float(x-self.low)/(self.mid-self.low),"hi":0.0}
        elif x <= self.hi and x >= self.mid:
            return {"low":0.0,"mid":float(self.hi-x)/(self.hi-self.mid),"hi":float(x-self.mid)/(self.hi-self.mid)}
        return {"low":0.0,"mid":0.0,"hi":0.0}

    def defuzz(self,y,zone):

        if zone == "low":
            return [0.0,0.0,self.mid-(y*(self.mid-self.low)),self.mid] ## Value for the four points of the trapezium
        if zone == "mid":
            return [0.0,self.low+(y*(self.mid-self.low)),self.hi-(y*(self.hi-self.mid)),self.hi]
        if zone == "hi":
            return [self.mid,(y*(self.hi-self.mid))+self.mid,self.hi,self.hi]
        
    def zones(self,inp):
        
        if inp < self.mid:
            return ["low","mid"]
        else:
            return ["mid","hi"]

    def trap_area(self,a,b,c,d,height):

        ar = 0.5*(b-a)*height
        ar = ar + (c-b)*height
        ar = ar + 0.5*(d-c)*height

        return ar
    
    def trap_centroid(self,a,b,c,d,height):

        x = (c-b)
        y = (d-a)
        z = (b-a)

        Cx = ((2*x*z) + (x*x) + (z*y) + (x*y) + (y*y))/(3*(x+y))
        Cy = height*((2*x) + y)/(3*(x+y))

        return [Cx,Cy]

    def CoG(self,a,b,c,d,height):
        print b+((c-b)/2)
        print (2*c+d)/3
        print (2*b+a)/3
        if a == b:
            return ((b+((c-b)/2)) + (2*c+d)/3)/2
        if c == d:
            return ((b+((c-b)/2))+(2*b+a)/3)/2
        
        return ((b+((c-b)/2))+ ((2*b+a)/3) + ((2*c+d)/3))/3

        
        
        
        



        
