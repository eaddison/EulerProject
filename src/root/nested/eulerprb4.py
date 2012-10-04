'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    import sys
    prefix = ''
    suffix = ''
    suf_swp = ''
    pln_str = ''
    for i in range(997,99,-1):
        prefix = str(i)
        suf_swp = str(i)
        suffix = suf_swp[2] + suf_swp[1] + suf_swp[0]
        pln_str = prefix + suffix
        pln_num = int(pln_str)
        for j in range(999,99,-1):
            quo,rmd = divmod(pln_num,j)
            if rmd == 0 and quo < 1000:
                print "We found the factors: %d, %d and the palindrome: %d" % (j,quo,pln_num)
                sys.exit()