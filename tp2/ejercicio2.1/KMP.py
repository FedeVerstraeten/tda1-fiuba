def itsCyclicRotation(s, d):
    t = s + s   #para realizar una busqueda ciclica se duplica s
    n=len(s)*2
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
            #print "una cadena es la rotacion ciclica de la otra"
            return True     #si quiero que funciones retornando un booleano
            #return str(i-q) #pocicion donde ocurre el patron
            q = pi[q-1]
    #print "una cadena NO es la rotacion ciclica de la otra"
    return False   #si quiero que funciones retornando un booleano

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
#--------- Ejemplo basico -----------
t = 'circo habia una vez un '
p = 'habia una vez un circo '

if itsCyclicRotation( t, p):
    print "una cadena es la rotacion ciclica de la otra"
else:
    print "una cadena NO es la rotacion ciclica de la otra"

#------------------------------------