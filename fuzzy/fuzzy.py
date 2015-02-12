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
        
    def zones(self,x):
        
        if x <= self.mid and x >= self.low:
            return ["low","hi"]
        else:
            return ["mid","hi"]
    
        
        



        
