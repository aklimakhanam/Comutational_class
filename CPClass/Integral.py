import numpy as np
import scipy.integrate as integrate

k = 2.0  # Spring constant
m = 1.0  # Mass of the object attached

def force(x, k):
    return k * x

# Riemann Sum
def riemann_sum(func, a, b, n):
    h = (b - a) / n
    x_r = [a + i * h for i in range(n + 1)]
    a_r = [-func(x, k) / m for x in x_r]  # Calculate acceleration
    integral_r = [0]  # Initialize the integral list 
    sum_result = 0
    for i in range(n):
        sum_result += func(x_r[i], k) * h
        integral_r.append(sum_result)
    
    return x_r, integral_r, a_r

# Trapezoidal Rule
def trapezoidal(func, a, b, n):
    h = (b - a) / n
    x_t = [a + i * h for i in range(n + 1)]
    a_t = [-func(x, k) / m for x in x_t ]  
    integral_t = [0]  
    sum_result = 0
    for i in range(n):
        sum_result += (func(x_t[i], k) + func(x_t[i+1], k)) * h / 2
        integral_t.append(sum_result)
    
    return x_t, integral_t, a_t

# Simpson's Rule
def simpsons_rule(func, a, b, n):
    h = (b - a) / n
    x_s = [a + i * h for i in range(n + 1)]
    a_s = [-func(x, k) / m for x in x_s]  
    integral_s = [0]  
    sum_result = 0
    for i in range(0, n):
        sum_result += (func(x_s[i-1], k) + 4 * func(x_s[i], k) + func(x_s[i+1], k)) * h / 6
        integral_s.append(sum_result)
    
    return x_s, integral_s, a_s

def Scipy_integral(func, a, b, k, n):
    x = np.linspace(a, b, n)
    result = []
    for k in x:
        integral, _ = integrate.quad(func, a, b, args=(k,))
        result.append(integral)
    return x, result

def analytical(func, a, b, k, n):
    x = np.linspace(a, b, n)
    PE = [0.5*k*xi**2 for xi in x]
    return x, PE
    

def energy(acc, x):
    KE = []
    PE = []
    E = []
    v = []
    t = []
    for i in range(0, len(x)):
        if i == 0:
            v.append(0)
            KE.append(0)
            PE.append(0.5*k*x[i]**2)
            E.append(0.5*k*x[i]**2)
            t.append(0)
        else:
            v_temp = v[i-1]**2 + 2*acc[i]*(x[i]-x[i-1])
            v.append(np.sqrt(v_temp))
            KE.append(0.5*m*v_temp)
            PE.append(0.5*k*x[i]**2)
            E.append((0.5*m*v_temp) + (0.5*k*x[i]**2))
            t.append(((np.sqrt(v_temp)-v[i-1])/acc[i]) + t[i-1])  
            
    return KE, PE, E, t



