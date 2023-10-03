#!/usr/bin/env python
# coding: utf-8

# In[2]:


import matplotlib.pyplot as plt
import ODE
import Integral 

# Calling differentiation calculator functions from ODE module
# Parameters
N0 = 1000  # Initial quantity
lambda_dc = 0.1  # Decay constant
ti = 0  # Initial time
tf = 10  # End time
dt = 0.1  # Time step

# Solve using Euler's method
times_euler, quantities_euler, activity_euler, dNdt_euler, hlife_euler = ODE.Euler(N0, lambda_dc, ti, tf, dt)

# Solve using RK4 method
times_rk4, quantities_rk4, activity_rk4, dNdt_rk4, hlife_rk4 = ODE.RK4(N0, lambda_dc, ti, tf, dt)

# Solve using Scipy
times_sp, quantities_sp = ODE.Scipy_ode(N0, lambda_dc, ti, tf, dt)

# Exact solution
times_ex, quantities_ex = ODE.exact(N0, lambda_dc, ti, tf, dt)

#Verify rate of change wrt time
plt.figure(figsize=(12, 6))
plt.plot(times_euler, activity_euler, label="Activity calculated (Euler)")
plt.plot(times_euler, dNdt_euler, label="Activity from formula (Euler)")
plt.plot(times_rk4, activity_rk4, label="Activity calculated (RK4)")
plt.plot(times_rk4, dNdt_rk4, label="Activity from formula (RK4)")
plt.xlabel('Time')
plt.xlim(dt, tf)
plt.ylabel('Activity')
plt.legend()
plt.title('Decay rate using Euler\'s Method and RK4 Method')
plt.grid(True)
plt.savefig("Activity_vs_time.png")
plt.show()

#Visualizing solutions from different methods
plt.figure(figsize=(12, 6))
plt.plot(times_euler, quantities_euler, label="Euler's Method")
plt.plot(times_rk4, quantities_rk4, label="RK4 Method")
plt.plot(times_sp, quantities_sp, label="Scipy")
plt.plot(times_ex, quantities_ex, label="Analytical")
plt.xlabel('Time')
plt.ylabel('Quantity')
plt.xlim(0, tf)
plt.legend()
plt.title('Radioactive Decay using Euler\'s Method and RK4 Method')
plt.grid(True)
plt.savefig("Decay_vs_time.png")
plt.show()

# Calling integral calculator functions from Integral module
# Initializing variables
k = 2.0  # Spring constant
m = 1.0  # Mass of the object 

# Call the functions with appropriate arguments
x_r, integral_r, a_r = Integral.riemann_sum(Integral.force, -10, 10, 1000)
x_t, integral_t, a_t = Integral.trapezoidal(Integral.force, -10, 10, 1000)
x_s, integral_s, a_s = Integral.simpsons_rule(Integral.force, -10, 10, 1000)
x_sc, integral_sc = Integral.Scipy_integral(Integral.force, -10, 10, k, 1000)
x_an, integral_an = Integral.analytical(Integral.force, -10, 10, k, 1000)
KE_r, PE_r, E_r, t_r = Integral.energy(a_r, x_r)
KE_t, PE_t, E_t, t_t = Integral.energy(a_t, x_t)
KE_s, PE_s, E_s, t_s = Integral.energy(a_s, x_s)

#Verifying time period
print("Time period: ", 4*max(t_r))

# Plot the results, scipy function is not working, I tried many to fix it but couldn't.
plt.figure(figsize=(12, 6))

plt.plot(x_r, integral_r, label='Riemann Sum Integral', linestyle='-')
plt.plot(x_t, integral_t, label='Trapezoidal Rule Integral', linestyle='-')
plt.plot(x_s, integral_s, label='Simpsons Rule Integral', linestyle='-')
plt.plot(x_sc, integral_sc, label='Scipy Integral', linestyle='-')
plt.xlabel('Displacement (x)')
plt.ylabel('Integral Value')
plt.title('Integral Results vs. Displacement')
plt.legend()
plt.grid(True)
plt.savefig("I_vs_x.png")
plt.show()

plt.figure(figsize=(12, 6))
plt.plot(x_r, PE_r, label='PE(Riemann)', linestyle='-')
plt.plot(x_r, KE_r, label='KE(Riemann)', linestyle='-')
plt.plot(x_r, E_r, label='Total energy E(Riemann)', linestyle='-')
plt.plot(x_t, PE_t, label='PE(Trapezoidal)', linestyle='-')
plt.plot(x_t, KE_t, label='KE(Trapezoidal)', linestyle='-')
plt.plot(x_t, E_t, label='Total energy E(Trapezoidal)', linestyle='-')
plt.plot(x_s, PE_s, label='PE(Simpson)', linestyle='-')
plt.plot(x_s, KE_s, label='KE(Simpson)', linestyle='-')
plt.plot(x_s, E_s, label='Total energy E(Simpson)', linestyle='-')
plt.xlabel('Displacement (x)')
plt.ylabel('Energy')
plt.title('Energy vs. Displacement')
plt.legend()
plt.grid(True)
plt.savefig("I_energy.png")
plt.show()


# In[ ]:




