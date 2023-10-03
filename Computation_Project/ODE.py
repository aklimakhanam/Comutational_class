import numpy as np
from scipy.integrate import odeint

def verify(quantities, times, dt, lambda_dc, N0):
    activity = [0]
    dNdt = [0]
    hlife = []
    
    #Loop for verifying activity
    for i in range(0, len(quantities)):
        if i==0:    #First element is zero to match the size of times list, so removing that
            continue
        else:
            rate = (quantities[i] - quantities[i-1]) / dt
            test_rate = -lambda_dc * quantities[i]
            activity.append(rate)
            dNdt.append(test_rate)
        
    #Loop for verifying half life
    for i in range(0, len(quantities)):
        if quantities[i]>=(0.5*N0 - 0.01*N0) and quantities[i]<= (0.5*N0 + 0.01*N0):
            hlife.append(times[i])
            
    print("Half-life: ",np.array(hlife)) # Print out the possible half lifes, also can be shown from the graph
    return activity, dNdt, hlife
    
# Define the function for Euler's method
def Euler(N0, lambda_dc, ti, tf, dt):
    
    #initialization of variables and lists
    times = [ti]
    quantities = [N0]
    t = ti
    N = N0
    
    #Loop for numerical calculation
    while t < tf:
        dN_dt = -lambda_dc * N
        N += dN_dt * dt
        t += dt
        times.append(t)
        quantities.append(N)
    
    activity_e, dNdt_e, hlife_e = verify(quantities, times, dt, lambda_dc, N0)
    
    return times, quantities, activity_e, dNdt_e, hlife_e

# Define the function for RK4 method
def RK4(N0, lambda_dc, ti, tf, dt):
    
    
    #initialization of variables and lists
    times = [ti]
    quantities = [N0]
    t = ti
    N = N0
    
    #Decay law equation
    def dN_dt(N, t):
        return -lambda_dc * N
        
    #Implementing RK4
    while t < tf:
        k1 = dt * dN_dt(N, t)
        k2 = dt * dN_dt(N + 0.5 * k1, t + 0.5 * dt)
        k3 = dt * dN_dt(N + 0.5 * k2, t + 0.5 * dt)
        k4 = dt * dN_dt(N + k3, t + dt)
        
        N += (k1 + 2 * k2 + 2 * k3 + k4) / 6
        t += dt
        times.append(t)
        quantities.append(N)
    
    activity_r, dNdt_r, hlife_r = verify(quantities, times, dt, lambda_dc, N0)
    
    return times, quantities, activity_r, dNdt_r, hlife_r
    
#Define function for scipy solution    
def Scipy_ode(N0, lambda_dc, ti, tf, dt):

    def dN_dt(N, t):
        return -lambda_dc * N

    #Define time step
    t = np.linspace(ti, tf, int((tf - ti) / dt) + 1)

    #Solving the ODE
    Nt = odeint(dN_dt, N0, t)
    
    return t, Nt

#Analytical Solution
def exact(N0, lambda_dc, ti, tf, dt):
    #initialization of variables and lists
    times = [ti]
    quantities = [N0]
    t = ti
    N = N0
    
    # Calculate N(t) for each time point
    while t < tf:
        N = N0 * np.exp(-lambda_dc * t)
        times.append(t)
        quantities.append(N)
        t += dt
    return times, quantities
        
        
        
        
        
