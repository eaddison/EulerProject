'''
Created on Oct 3, 2012

@author: ed
'''

if __name__ == '__main__':
    count = 1
    res = 0
    num_lst = []
    while (count < 1000 ):
        mul3 = 3 * count
        mul5 = 5 * count
        if mul3 not in num_lst and mul3 < 1000:
            num_lst.append(mul3)
        if mul5 not in num_lst and mul5 < 1000:
            num_lst.append(mul5)
        count += 1
        #print "count = %d, mul3 = %d, mul5 = %d, res %d, num_lst %s" % (count,mul3, mul5,res,num_lst.__repr__())
    res = sum(num_lst)
    print "result = %d  and the count = %d" % (res, count)