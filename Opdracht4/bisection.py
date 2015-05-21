def findRoot(f,a,b,epsilon):
    while True:
        m = float((a+b)/2)
        if abs(float(a-b)) <= epsilon:
            return(m)
        elif (f(m) < 0 and f(a) > 0) or (f(m) > 0 and f(a) < 0):
            b = m
        elif (f(m) > 0 and f(b) < 0) or (f(m) < 0 and f(b) > 0):
            a = m
