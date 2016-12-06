import numpy as np
import matplotlib.pyplot as plt

M_pod = np.loadtxt('../data_files/mach_trades/M_pod.txt', delimiter = '\t')
Re = np.loadtxt('../data_files/mach_trades/Re.txt', delimiter = '\t')
A_tube = np.loadtxt('../data_files/mach_trades/A_tube.txt', delimiter = '\t')
T_tunnel = np.loadtxt('../data_files/mach_trades/T_tunnel.txt', delimiter = '\t')
L_pod = np.loadtxt('../data_files/mach_trades/L_pod.txt', delimiter = '\t')
power = np.loadtxt('../data_files/mach_trades/comp_power.txt', delimiter = '\t')
steady_vac = np.loadtxt('../data_files/mach_trades/vac_power.txt', delimiter = '\t')
total_energy = np.loadtxt('../data_files/mach_trades/total_energy.txt', delimiter = '\t')
thrust = np.loadtxt('../data_files/mach_trades/thrust.txt', delimiter = '\t')

fig = plt.figure(figsize = (3.25,3.5), tight_layout = True)
ax = plt.axes()
plt.hold(True)
plt.subplot(211)
plt.plot(M_pod, A_tube, 'b-', linewidth = 2.0)
plt.ylabel('Tube Area ($m^2$)', fontsize = 10, fontweight = 'bold')
plt.subplot(212)
plt.plot(M_pod, total_energy/(1.0e6), 'r-', linewidth = 2.0)
plt.xlabel('Mach Number', fontsize = 10, fontweight = 'bold')
plt.ylabel('Yearly Energy Cost \n (Million USD)', fontsize = 10, fontweight = 'bold')
plt.setp(ax.get_xticklabels(), fontsize=8)
plt.setp(ax.get_yticklabels(), fontsize=8)
plt.ylim(25,35)
plt.savefig('../graphs/mach_trades/pressure_vs_mach.png', format = 'png', dpi = 300)
plt.show()