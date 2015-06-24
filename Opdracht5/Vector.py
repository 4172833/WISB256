class Vector:
    lst = []
    
    def __init__(self,i,j=0):
        if type(j) == list:
            self.lst = j
        else:
            for x in range(i):
                self.lst.append(j)
            
    def __str__(self):
        string = ""
        for a in range(len(self.lst)):
            string += str("{0:.6f}".format(self.lst[a])) + "\n"
        return(string)
    
    def lincomb(self, other, alpha, beta):
        lijst = []
        for b in range(len(self.lst)):
           lijst.append(alpha*self.lst[b] + beta*other.lst[b])
        
        w = Vector(self, lijst)
        return(w)
    
    def scalar(self,alpha):
        lijst2 = []
        for c in range(len(self.lst)):
            lijst2.append(alpha*self.lst[c])
            
        w = Vector(self, lijst2)
        return(w)
        
    def inner(self, other):
        d = 0
        for e in range(len(self.lst)):
            d = d + (self.lst[e]*other.lst[e])
            
        return(d)
    
    def norm(self):
        f = 0
        
        for g in range(len(self.lst)):
            f = f + ((self.lst[g])**2)
        h = f**0.5
        return(h)
        
    