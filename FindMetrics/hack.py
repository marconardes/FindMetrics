import numpy as np

#code used to eliminate wrong commit lines from file final.csv. 
#every user should have only 10 commits. This file corrects this.
#notice the lines are hardcoded

f = open("temp.csv","r")
lines = f.readlines()
f.close()

f = open("final.csv","w")

for x in range(0, 114):
    if (x == 0 or x == 6 or x == 8 or x == 9 #Asub10
        or x == 14 #Asub5
        or x == 25 #Asub7
        or x == 36 or x == 37  #Asub9
        or x == 48 or x == 55  #Bsub10
        or x == 60 or x == 68 or x == 71 #Bsub11
        or x == 73 or x == 74  #Bsub5
        or x == 85 or x == 86 or x == 95  #Bsub7
        or x == 98 or x == 99 or x == 100 or x == 107 or x == 108 or x == 110 #Bsub9 
    ) :
        pass
    else:
        f.write(lines[x])
    
f.close()


#for x in range(0, 127):
#    if (x == 0 or x == 6 or x == 8 or x == 9 #Asub10
##        or x == 14 #Asub5
##        or x == 25 #Asub7
#        or x == 36 or x == 37  #Asub9
#        or x == 49 or x == 50  #
#        or x == 61 or x == 68
#        or x == 73 or x == 81 or x == 84
#        or x == 86 or x == 87
#        or x == 98 or x == 99 or x == 108
#        or x == 111 or x == 112 or x == 113 or x == 120 or x == 121 or x == 123
#    ) :
#        pass
#    else:
#        f.write(lines[x])
    
#f.close()
