'''
Created on Oct 3, 2012

@author: ed
'''

if __name__ == '__main__':
    fctr_lst = []
    fctr1 = 3
    fctr2 = 0
    while (fctr1 < 776000):
        print "factor we are currently working on: %d" % (fctr1)
        fctr2,mod = divmod(600851475143,fctr1)
        print "factor2: %d" % (fctr2)
        if (mod == 0 and divmod(fctr2,2)[1] != 0):
            if (fctr1 not in fctr_lst):
                isprime = True
                i = 3
                while i < fctr1:
                    if divmod(fctr1,i)[1] == 0:
                        isprime = False
                        break
                    i += 2
                if isprime is True:
                    print "We found a prime factor: %d" % (fctr1)
                    fctr_lst.append(fctr1)
            if (fctr2 not in fctr_lst):
                isprime = True
                i = 3
                while i < fctr2:
                    if divmod(fctr2,i)[1] == 0:
                        isprime = False
                        break
                    i += 2
                if isprime is True:
                    print "We found a prime factor: %d" % (fctr2)
                    fctr_lst.append(fctr2)
        fctr1 += 2
    print "factors are: %s" % (fctr_lst)