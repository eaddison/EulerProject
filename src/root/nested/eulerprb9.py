'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    import sys
    
    a = 1
    b = 1
    c = 0
    
    for i in range(0,251,1):
        a += 1
        b = 200
        c = pow((pow(a,2) + pow(b,2)),0.5)
        #print "a = %d   b = %d  c = %d sum = %d" % (a,b,c,(a + b + c))
        if (pow(a,2) + pow(b,2) == pow(c,2) and a + b + c == 1000):
            print "We found the correct Pythagorean triplet: %d : %d : %d" % (a,b,c)
            print "The product of abc is: %d" % (a*b*c)
            sys.exit
        for j in range(1,301,1):
            b += 1
            c = pow((pow(a,2) + pow(b,2)),0.5)
            #print "a = %d   b = %d  c = %d sum = %d" % (a,b,c,(a + b +c))
            if (pow(a,2) + pow(b,2) == pow(c,2) and a + b + c == 1000):
                print "We found the correct Pythagorean triplet: %d : %d : %d" % (a,b,c)
                print "The product of abc is: %d" % (a*b*c)
                sys.exit