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