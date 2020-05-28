import math

def LeftFractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    for k in range(n):
        ### k = n-k-1
        b_k = (pow(delta_t, a) / (math.gamma(a+1))) * (pow((n-k-1)+1, a) - pow(n-k-1, a))
        suma += b_k*f(k*delta_t)
    return suma

def RightFractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    for k in range(n):
       ### k = n-k-1    
       b_k = (pow(delta_t, a) / (math.gamma(a+1))) * (pow((n-k-1)+1, a) - pow(n-k-1, a))
       suma += b_k*f((k+1)*delta_t)
    return suma

def FractionalTrapezoidalFormul(a, t, n, f):
    delta_t = t/n
    ### when k = 0
    a_kn = (pow(delta_t, a) / (math.gamma(a+2))) * (pow(n-1, a+1) - (n-1-a)*pow(n, a))
    suma = a_kn * f(0) ### k=0 then -> t_0 = 0*t/n??
    for k in range(1, n):
        a_kn = (pow(delta_t, a) / (math.gamma(a+2))) * ( pow(n-k+1, a+1) + pow(n-1-k, a+1) - 2 * pow(n-k, a+1) )
        suma += a_kn * f(k*t/n)
    a_kn = (pow(delta_t, a) / (math.gamma(a+2))) * 1
    suma += a_kn * f(t)
    return suma


def FractionalSimpsonSFormul(a, t, n, f):
    delta = t/n
    ### when k = 0
    k = 0
    
    c_kn = (pow(delta_t, a) / (math.gamma(a+3))) * ( 4*(pow(n+1, 2+a) - pow(n, 2+a)) - (a+2)*(3* pow(n+1, 1+a)+ pow(n, 1+a)) + (a+2)*(a+1)*pow(n+1, a) )
    suma_1 = c_kn * f(k)
    
    AC_kn = (4*pow(delta_t, a) / (math.gamma(a+3))) * ( (a+2)*(pow(n+1-k, 1+a) + pow(n - k, 1+a)) - 2*(pow(n+1-k, 2+a) - pow(n-k, 2+a)) )
    x = ((k*t/n) + ((k+1)*t/n))/2
    suma_2 = AC_kn*f(x) ### t_k+1/2 = (t_k + t_k)/2
    for k in range(1, n):
        
        suma_1 += c_kn * f(k)
        c_kn = (pow(delta_t, a) / (math.gamma(a+3))) * ( 4 * (pow(n+1-k, 2+a) - pow(n-1-k, 2+a)) - (a+2)*(pow(n+1-k, 1+a) + 6*pow(n-k,1+a) + pow(n-k-1,1+a)) )
        
        ### for AC_kn
        AC_kn = (4*pow(delta_t, a) / (math.gamma(a+3))) * ( (a+2)*(pow(n+1-k, 1+a) + pow(n-k, 1+a)) - 2*(pow(n+1-k, 2+a) - pow(n-k, 2+a)) )
        x = ((k*t/n) + ((k+1)*t/n))/2
        suma_2 += AC_kn*f(x) ### x = t_k+1/2
    ### when k = n
    c_kn = 2-a
    suma_1 += c_kn*f(t)
    
    return suma_1+suma_2

def delta_f(k, t, n, f):
    return ( f((k+1)*t/n) - f(k*t/n) ) / (t/n)

def LeftCaputo_0FractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    ###left when teta = 1
    teta = 1
    for k in range(n):
        w_k = (pow(delta_t, a) / (math.gamma(2-a)) ) * ((pow((n-k-1)+1, 1-a) - pow(n-k-1, 1-a)))
        suma += w_k*( teta*delta_f(k, t, n, f) + (1-teta)* (delta_f(k+1, t, n, f)) )
    return suma

def RightCaputo_0FractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    ###right when teta = 0
    teta = 0
    for k in range(n):
        w_k = (pow(delta_t, a) / (math.gamma(2-a)) ) * ((pow((n-k-1)+1, 1-a) - pow(n-k-1, 1-a)))
        suma += w_k*( teta*delta_f(k, t, n, f) + (1-teta)* (delta_f(k+1, t, n, f)) )
    return suma

def delta_2f(k, t, n, f):
    return ( f((k+1)*t/n) - 2 * f(k*t/n) + f((k-1)*t/n) ) / (t/n)

def LeftCaputo_1FractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    ###left when teta = 1
    teta = 1
    for k in range(n):
        w_k = (pow(delta_t, 1-a) / (math.gamma(3-a)) ) * ((pow((n-k-1)+1, 2-a) - pow(n-k-1, 2-a)))
        suma += w_k*( teta*delta_2f(k, t, n, f) + (1-teta)* (delta_2f(k+1, t, n, f)) )
    return suma

def RightCaputo_1FractionalRectangularFormul(a, t, n, f):
    delta_t = t/n
    ###right when teta = 0
    teta = 0
    for k in range(n):
        w_k = (pow(delta_t, 1-a) / (math.gamma(3-a)) ) * ((pow((n-k-1)+1, 2-a) - pow(n-k-1, 2-a)))
        suma += w_k*( teta*delta_2f(k, t, n, f) + (1-teta)* (delta_2f(k+1, t, n, f)) )
    return suma

def delta_fel(k, t, n, f):
    return ( f((k+1)*t/n) - f((k-1)*t/n) ) / 2*(t/n)

def Caputo_0FractionalTrapezoidalFormul(a, m, t, n, f):
    delta_t = t/n
    #when k=0
    a_0n = ( pow(delta_t, m-a) / (math.gamma(m+2-a)) ) * (pow(n-1, m-a+1) - (n-1-m+a)*pow(n,m-a))
    suma = a_0n * (-3*f(0) +2*f(1*t/n) - f(2*t/n) ) / (2*delta_t)
    for k in range(1, n):
        a_kn = ( pow(delta_t, m-a) / (math.gamma(m+2-a)) ) * (pow(n-k+1, m-a+1) + pow(n-1-k, m-a+1) - 2*pow(n-k, m-a+1) )
        suma += a_kn*dela_fel(k, t, n, f)
    a_kn = 1
    suma += a_kn*delta_fel(n, t, n, f)
    return suma

def Caputo_1FractionalTrapezoidalFormul(a, t, n, f):
    delta_t = t/n
    #when k=0
    a_0n = ( pow(delta_t, m-a) / (math.gamma(m+2-a)) ) * (pow(n-1, m-a+1) - (n-1-m+a)*pow(n,m-a) )
    suma = a_0n * (f(1*t/n) -2*f(0) + f(-delta_t) ) / (pow(delta_t, 2) )
    for k in range(1, n):
        a_kn = ( pow(delta_t, m-a) / (math.gamma(m+2-a)) ) * (pow(n-k+1, m-a+1) + pow(n-1-k, m-a+1) - 2*pow(n-k, m-a+1) )
        suma += a_kn*dela_2f(k, t, n, f)
    a_kn = 1
    suma += a_kn*delta_2f(n, t, n, f)
    return suma

def LeftRectangularFormal(t, n, f):
    delta_t = t/n
    suma = 0
    for k in range(n): 
        suma += delta_t*f(k*delta_t)
    return suma

def RightRectangularFormal(t, n, f):
    delta_t = t/n
    suma = 0
    for k in range(n): 
        suma += delta_t*f((k+1)*delta_t)
    return suma

def MidRectangularFormal(t, n, f):
    delta_t = t/n
    suma = 0
    for k in range(n): 
        ### a = ( k + (k+1) ) /2   f(a*t/n)
        suma += ((k+1)-k)*f((k+1+k)*t/2*n)
    return suma

def SimpsonsFormul(t, n, f):
    delta_t = t/n
    suma = 0
    for k in range(1, n):
        ### (b-a/6)  * ( f(b) + 4*f((a+b)/2) + f(a) )  
        suma += ( delta_t/6 ) * ( f((k-1)*delta_t) + 4*f( (k-1/2 ) *delta_t ) + f(k*delta_t) )
    return suma

def TrapezoidalFormul(t, n, f):
    delta_t =t/n
    suma = 0
    for k in range(1, n+1):
        suma +=(delta_t/2) * ( f(k*delta_t) + f((k+1)*delta_t) )
    return suma