#code

def clearBit(num, i):
    #print "bin(",num,"):","{0:b}".format(num);
    #print "1 <<",i,":", "{0:b}".format((1 << i));
    mask = ~(1 << i);
    #print "mask:","{0:b}".format(mask);
    print "{0:b}".format((num & mask)) ;

def getBit(num,i):
    print i,"th bit of",num," 1 ?", (num & (1 << i) !=0);
    
    
def setBits(num, i):
    print "{0:b}".format((num | (1 << i)));


print "=======CLEAR BIT=======";
print "Clear 3rd bit of 28:",;
clearBit(28,3);
print "=======GET BIT=======";
getBit(28,3);
print "=======SET BIT=======";
print "Set 0th bit of 28:",;
setBits(28,0);
    