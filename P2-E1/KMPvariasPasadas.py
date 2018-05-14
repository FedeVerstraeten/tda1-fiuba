def cyclicShiftStr(str):
    n = len(str)
    str2 = str
    str2 = str[1:]+str[0:1]
    return str2

def KMP_match(t, d):
    n=len(t)
    m=len(d)

    pi = compute_prefix_function(d)
    q = 0
    i = 0
    while i < n:
        if d[q]==t[i]:
            q=q+1
            i = i + 1
        else:
            if q != 0:
                q = pi[q-1]
            else:
                i = i + 1
        if q == m:
            return True
    return False

def compute_prefix_function(p):
    m=len(p)
    pi =range(m)
    k=1
    l = 0
    while k < m:
        if p[k] <= p[l]:
            l = l + 1
            pi[k] = l
            k = k + 1
        else:
            if l != 0:
                l = pi[l-1]
            else:
                pi[k] = 0
                k = k + 1
    return pi

def itsCyclicRotation(p,t):
    n=len(p)
    m=len(t)

    if m != n:
        return False

    i=0
    while  i < n:
        if KMP_match(p,t):
            return True
        p = cyclicShiftStr(p)
        i=i+1
    return False

#-------- Ejemplo basico ----------

t = 'abracadabra'
p = 'cadabraabra'

if itsCyclicRotation( t, p):
    print "una cadena es la rotacion ciclica de la otra"
else:
    print "una cadena NO es la rotacion ciclica de la otra"
#----------------------------------