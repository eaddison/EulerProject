'''
Created on Oct 4, 2012

@author: ed
'''

if __name__ == '__main__':
    lcm_found = False
    mult = 2500
    set_num = [11,12,13,14,15,16,17,18,19,20]
    while lcm_found == False:
        for num in set_num:
            quo,mod = divmod(mult,num)
            if mod != 0:
                break
        if mod == 0:
            lcm_found = True
        else:
            mult += 2
    if lcm_found == True:
        print "The lcm is: %d" % (mult)