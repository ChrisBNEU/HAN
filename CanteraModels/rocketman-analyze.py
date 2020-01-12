#!/usr/bin/env python
# coding: utf-8

# # Plug flow reactor simulation of Thruster
# 
# ![caption](Graphics/thruster-details.png)
# 

# In[1]:


import cantera as ct
import numpy as np

from matplotlib import pyplot as plt
import csv
import os
import itertools
import pandas as pd


# In[2]:


from ipywidgets import interact, interactive, fixed, interact_manual
import ipywidgets as widgets


# In[3]:


import json
with open('rocketman/settings.json') as fp:
    settings = json.load(fp)
cat_area_per_vol_options = list(sorted(set(np.array(settings)[:,0])))
temperature_c_options = list(sorted(set(np.array(settings)[:,1])))


# In[4]:


cat_area_per_vol_options, temperature_c_options


# In[5]:



print("Processing SLURM array job.")

rocket_array_dir = 'rocketman'

cti_file = os.path.join(rocket_array_dir,'0','chem_annotated.cti')

print(f"Using cantera input file {os.path.abspath(cti_file)}")

print(f"Settings aray is from 0 to {len(settings)-1} ")

from collections import defaultdict
setting_dict = defaultdict(dict)
for i,(a,t) in enumerate(settings):
    setting_dict[a][t] = i


# In[25]:


data_dict = defaultdict(dict)
for i,(a,t) in enumerate(settings):
    output_filename = os.path.join('rocketman',str(i),'surf_pfr_output.csv')
    print(output_filename, end=' ')
    try:
        data = pd.read_csv(output_filename)
        print(f"✅ OK  {data['Distance (mm)'].max():5.2f} mm    {data['T (C)'].min():.0f}-{data['T (C)'].max():.0f} ºC")
    except:
        print("❌ FAIL!")
        data = None
    data_dict[a][t] = data


# In[7]:


gas=ct.Solution(cti_file)
surf = ct.Interface(cti_file,'surface1', [gas])


# In[8]:


print(", ".join(gas.species_names))


# In[9]:


print(", ".join(surf.species_names))


# In[10]:


# unit conversion factors to SI
cm = 0.01 # m
minute = 60.0  # s


# In[11]:


#######################################################################
# Input Parameters for combustor
#######################################################################
mass_flow_rate =  0.5e-3 # kg/s

pressure = ct.one_atm # constant

length = 1.1 * cm  # Catalyst bed length. 11mm
cross_section_area = np.pi * (0.9*cm)**2  # Catalyst bed area.  18mm diameter circle.


# In[12]:


NReactors = 2001
def xlabels():
    #plt.xlim(0,50)
    plt.xticks([0,NReactors/4,NReactors/2,3*NReactors/4, NReactors],['0','','','',f'{length*1000:.0f} mm'])
    plt.xlabel("Distance down reactor")


# In[16]:


def f(cat_area_per_vol, temperature_c):
    
    print(f"Catalyst area per volume {cat_area_per_vol :.2e} m2/m3")
    print(f"Initial temperature {temperature_c :.1f} ºC")
    print(f"Simulation number {setting_dict[cat_area_per_vol][temperature_c]}")
    data = data_dict[cat_area_per_vol][temperature_c]
    
    data['T (C)'].plot()
    plt.ylabel('T (C)')
    xlabels()
    plt.show()
    
    data[['gas_heat','surface_heat']].plot()
    xlabels()
    #plt.savefig('gas_and_surface_heat.pdf')
    plt.show()

    species_to_plot = ['NH3(2)',
 'NH2OH(3)',
 'HNO3(4)',
 'CH3OH(5)',
 'H2O(6)',
 'N2(7)',
 'O2(8)',
 'NO2(9)',
 'NO(10)',
 'N2O(11)',
        ]
    data[species_to_plot].plot(title='gas mole fraction', logy=False)
    xlabels()
    plt.tight_layout()
    #plt.savefig(f'gas_mole_fractions_{i}.pdf')
    plt.show()
    return data
    

a = widgets.SelectionSlider(
    options=cat_area_per_vol_options,
    value=3e5,
    description='Catalyst area per volume (m2/m3)',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True
)
t = widgets.SelectionSlider(
    options=temperature_c_options,
    value=400,
    description='Initial temperature (C)',
    disabled=False,
    continuous_update=False,
    orientation='horizontal',
    readout=True
)

interact(f, cat_area_per_vol=a, temperature_c=t)


# In[18]:


data['Distance (mm)'].max()


# In[ ]:


def report_rates(n=8):
    print("\nHighest net rates of progress, gas")
    for i in np.argsort(abs(gas.net_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {gas.reaction_equation(i):48s}  {gas.net_rates_of_progress[i]:8.1g}")
    print("\nHighest net rates of progress, surface")
    for i in np.argsort(abs(surf.net_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {surf.reaction_equation(i):48s}  {cat_area_per_vol*surf.net_rates_of_progress[i]:8.1g}")
    print("\nHighest forward rates of progress, gas")
    for i in np.argsort(abs(gas.forward_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {gas.reaction_equation(i):48s}  {gas.forward_rates_of_progress[i]:8.1g}")
    print("\nHighest forward rates of progress, surface")
    for i in np.argsort(abs(surf.forward_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {surf.reaction_equation(i):48s}  {cat_area_per_vol*surf.forward_rates_of_progress[i]:8.1g}")
    print("\nHighest reverse rates of progress, gas")
    for i in np.argsort(abs(gas.reverse_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {gas.reaction_equation(i):48s}  {gas.reverse_rates_of_progress[i]:8.1g}")
    print("\nHighest reverse rates of progress, surface")
    for i in np.argsort(abs(surf.reverse_rates_of_progress))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {surf.reaction_equation(i):48s}  {cat_area_per_vol*surf.reverse_rates_of_progress[i]:8.1g}")

    print(f"\nSurface rates have been scaled by surface/volume ratio {cat_area_per_vol:.1e} m2/m3")
    print("So are on a similar basis of volume of reactor (though porosity not yet accounted for)")
    print(" kmol / m3 / s")
report_rates()


# In[ ]:


def report_rate_constants(n=8):
    print("\nHighest forward rate constants, gas")
    for i in np.argsort(abs(gas.forward_rate_constants))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {gas.reaction_equation(i):48s}  {gas.forward_rate_constants[i]:8.1e}")
    print("\nHighest forward rate constants, surface")
    for i in np.argsort(abs(surf.forward_rate_constants))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {surf.reaction_equation(i):48s}  {surf.forward_rate_constants[i]:8.1e}")
    print("\nHighest reverse rate constants, gas")
    for i in np.argsort(abs(gas.reverse_rate_constants))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {gas.reaction_equation(i):48s}  {gas.reverse_rate_constants[i]:8.1e}")
    print("\nHighest reverse rate constants, surface")
    for i in np.argsort(abs(surf.reverse_rate_constants))[-1:-n:-1]: # top n in descending order
        print(f"{i:3d} : {surf.reaction_equation(i):48s}  {surf.reverse_rate_constants[i]:8.1e}")

    print("Units are a combination of kmol, m^3 and s, that depend on the rate expression for the reaction.")
report_rate_constants()


# In[ ]:





# In[ ]:


sim.time


# In[ ]:


gas.TDY = TDY
r.syncState()
r.thermo.T


# In[ ]:


r.thermo.X - gas.X


# In[ ]:


report_rate_constants()


# In[ ]:


def xlabels():
    plt.xticks([0,NReactors/4,NReactors/2,3*NReactors/4, NReactors],['0','','','',f'{length*1000:.0f} mm'])
    plt.xlabel("Distance down reactor")


# In[ ]:


data['T (C)'].plot()
plt.ylabel('T (C)')
xlabels()


# In[ ]:


data[['NH2OH(3)', 'HNO3(4)', 'CH3OH(5)']].plot()
plt.ylabel('Mole fraction')
xlabels()


# In[ ]:


list(data.columns)[:4]


# In[ ]:


data[['T (C)', 'alpha']].plot()
xlabels()


# In[ ]:


ax1 = data['T (C)'].plot()
plt.ylabel('Temperature (C)')
xlabels()
plt.legend()
ax2 = ax1.twinx()
data['alpha'].plot(ax=ax2, color='tab:orange')
ax2.set_ylim(-2, 2)
plt.legend()
plt.ylabel('alpha')
plt.tight_layout()
plt.savefig('temperature-and-alpha.pdf')
plt.show()


# In[ ]:


data.columns


# In[ ]:


data[['gas_heat','surface_heat']].plot()
#plt.ylim(-1e7, 1e7)
xlabels()
plt.savefig('gas_and_surface_heat.pdf')
plt.show()


# In[ ]:


ax1 = data[['gas_heat','surface_heat']].plot()
plt.ylim(-1e9, 1e9)
xlabels()
plt.ylabel('Heat consumption rate (kJ/m3/s)')
plt.legend(loc='upper left')
ax2 = ax1.twinx()
data['alpha'].plot(ax=ax2, style='k:', alpha=0.5)
ax2.set_ylim(-10, 10)
plt.legend(loc='lower right')
plt.ylabel('alpha')
plt.tight_layout()
plt.savefig('heats-and-alpha.pdf')
plt.show()


# In[ ]:


data[['T (C)']].plot()
plt.ylabel('Temperature (C)')
xlabels()
plt.tight_layout()
plt.savefig('temperature.pdf')
plt.show()


# In[ ]:


data[['alpha']].plot(logy=True)
xlabels()


# In[ ]:


data.plot(x='T (C)',y='alpha')


# In[ ]:


specs = list(data.columns)
specs = specs[4:-1]

gas_species = [s for s in specs if 'X' not in s]
adsorbates = [s for s in specs if 'X' in s]

gas_species, adsorbates


# In[ ]:


data[gas_species[0:5]].plot(logy=True, logx=True)


# In[ ]:


for i in range(0,len(gas_species),10):
    data[gas_species[i:i+10]].plot(title='gas mole fraction', logy=False)
    xlabels()
    plt.tight_layout()
    plt.savefig(f'gas_mole_fractions_{i}.pdf')
    plt.show()
    
for i in range(0,len(adsorbates),10):
    data[adsorbates[i:i+10]].plot(title='surface coverages', logy=False)
    xlabels()
    plt.tight_layout()
    plt.savefig(f'surface_coverages_{i}.pdf')
    plt.show()


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




