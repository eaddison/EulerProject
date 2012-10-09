'''
Created on Oct 7, 2012

@author: ed
'''

if __name__ == '__main__':
    from time import ctime
    i = 1
    tri_num = 0
    factors = 0
    print "Starting calculations at ", ctime()
    while factors <= 500:
        factors = 0
        tri_num += i
        if tri_num > 10000000:
            for j in range(int(tri_num**0.5),0,-1):
                if divmod(tri_num,j)[1] == 0:
                    factors += 1
        factors *= 2
        #print "Triangle number %d with factors %d" % (tri_num,factors)
                    
        i += 1
    print "completed calculations at ", ctime()
    print "The first triangle number to have over 500 factors is: ", tri_num