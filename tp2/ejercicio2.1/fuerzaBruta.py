def cyclicShiftStr(str):    # por lo tanto es de O(n)
    n = len(str)            # O(n)
    str2 = str              # O(cte)
    str2 = str[1:]+str[0:1] # O(n)
    return str2             # O(cte)

def isAnCyclicRotation(s1,s2):
    n=len(s1)   # O(n)
    i=0

    while s1 != s2 and i < n:           #el while en total es O(n2)
        i=i+1                           #O(cte)
        s2=cyclicShiftStr(s2)           #O(n)

    if s1==s2:                          #O(n)
        return True                     #O(cte)
    return False                        #O(cte)

#--------------- Ejemplo basico --------------------

s1 = "abracadabra"
s2 = "cadabraabra"

if isAnCyclicRotation(s1,s2):
    print "una es la rotacion ciclica de la otra"
else:
    print "una NO es la rotacion ciclica de la otra"
#---------------------------------------------------