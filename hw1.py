# A16379923

#!python3
import math
import numpy as np

def main():
    ## Test cases
    print("test1: p1=p2")
    p1 = [1,1]
    p2 = [1,1]
    q = [2,2]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test2: Vertical line, q close to segment")
    p1 = [0,0]
    p2 = [0,1]
    q = [1,0.5]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test3: horizontal line, q close to segment")
    p1 = [0,0]
    p2 = [1,0]
    q = [0.5,1]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test4: angled line, q close to segment")
    p1 = [1,1]
    p2 = [10,3]
    q = [2,6]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test5: angled line, q close to p1")
    p1 = [1,1]
    p2 = [10,3]
    q = [-10,-4]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test5: angled line, q close to p2")
    p1 = [1,1]
    p2 = [10,3]
    q = [11,4]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

    print("test6: angled line, q = p2")
    p1 = [1,1]
    p2 = [10,3]
    q = [10,3]
    print("line through two points")
    a,b,c = computeLineThroughTwoPoints(p1,p2)
    print(a,b,c)
    print("Distance to line")
    d = computeDistancePointToLine(q,p1,p2)
    print(d)
    print("distance to line segment")
    w,d = computeDistancePointToSegment(q,p1,p2)
    print(w,d)
    print()

def computeLineThroughTwoPoints(p1,p2):
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if abs(x1-x2) <= 1e-8 and abs(y1-y2) <= 1e-8:# check if points are the same
        print("Error: p1 = p2")
        return 0,0,0
    elif abs(x1-x2) <= 1e-8: #check if vertical
        print("Line is vertical")
        a = 0
        b = -1
        c = y1
    else:
        a = (y2-y1)/(x2-x1)# slope m
        b = -1# solve y = m*x+c --> 0 = m*x - y + c
        c = y2 - (y2-y1)*x1/(x2-x1)
        den = np.sqrt(a**2 + b**2)# normalize
        a = a/den
        b = b/den
        c = c/den
    return a,b,c

def computeDistancePointToLine(q,p1,p2):
    xq = q[0]
    yq = q[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if abs(x1-x2) <= 1e-8 and abs(y1-y2) <= 1e-8: # check if points are the same
        print("Error: p1 = p2")
        return 0,0
    a,b,c = computeLineThroughTwoPoints(p1,p2)# find equation for line
    d = abs(a*xq+b*yq+c)/(a**2+b**2)**0.5 # compute distance
    return d

def computeDistancePointToSegment(q,p1,p2):
    xq = q[0]
    yq = q[1]
    x1 = p1[0]
    y1 = p1[1]
    x2 = p2[0]
    y2 = p2[1]
    if abs(x1-x2) <= 1e-8 and abs(y1-y2) <= 1e-8: # check if points are the same
        print("Error: p1 = p2")
        return 0,0
    dp = np.dot([xq-x1,yq-y1],[x2-x1,y2-y1])# dot product of p1->q1 and p1->p2
    if dp <= 0:# if negative, q away from p2 from p1
        w = 1
        d = ((xq-x1)**2+(yq-y1)**2)**0.5
    elif dp >= np.dot([x2-x1,y2-y1],[x2-x1,y2-y1]):# if true, q beyond p2 from p1
        w = 2
        d = ((xq-x2)**2+(yq-y2)**2)**0.5
    else:# between p1 and p2, so segment is closest
        w = 0
        d = computeDistancePointToLine(q,p1,p2)
    return d,w

if __name__ == "__main__": 
    main()
    
