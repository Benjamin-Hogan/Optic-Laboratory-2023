#!/usr/bin/env python
# coding: utf-8

# # Reflection from First-Surface Mirrors
# ## Optics Code
# ### Benjamin Hogan

# In[1]:


#Importing Modules
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# # Part 1: Reflection from First-Surface Mirrors

# ## Importing the data from Excel files
# ### See Folder in Github for excel files

# In[2]:


## Control ##
Table_1_control = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 1 Control.xlsx')
Initial_reflectance = (np.asarray((Table_1_control['Voltage'])))
Initial_reflectance_err = (np.asarray((Table_1_control['Uncertainty in Voltage'])))
print(Initial_reflectance)


## Aluminum Mirror ##
Table_2_alum = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 2 Aluminum .xlsx')
Reflectance_alum = (np.asarray((Table_2_alum['Voltage'])))
Reflectance_alum_err = (np.asarray((Table_2_alum['Uncertainty in Voltage'])))
print(Reflectance_alum)

## Gold Mirror ##
Table_3_gold = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 3 Gold.xlsx')
Reflectance_gold = (np.asarray(((Table_3_gold['Voltage']))))
Reflectance_gold_err = (np.asarray(((Table_3_gold['Uncertainty in Voltage']))))
print(Reflectance_gold)
print(type(Reflectance_gold))

## Laser Aligned Mirror ##
Table_4_laser_aligned = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 4 Laser Aligned.xlsx')
Reflectance_laser_aligned = (np.asarray((Table_4_laser_aligned['Voltage'])))
Reflectance_laser_aligned_err = (np.asarray((Table_4_laser_aligned['Uncertainty in Voltage'])))
print(Reflectance_laser_aligned)

## Aluminum Mirror with varying angle ##
Table_5_alum_angle = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 5 Aluminum Angle.xlsx')
Reflectance_alum_angle = (np.asarray((Table_5_alum_angle['Voltage'])))
Reflectance_alum_angle_err = (np.asarray((Table_5_alum_angle['Uncertainty in Voltage'])))
print(Reflectance_alum_angle)

## Laser Aligned Mirror with varying angle ##
Table_6_laser_aligned_angle = pd.read_excel('/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 1 Mirror Data/Table 6 Laser Alinged Anlge.xlsx')
Reflectance_laser_aligned_angle = (np.asarray((Table_6_laser_aligned_angle['Voltage'])))
Reflectance_laser_aligned_angle_err = (np.asarray((Table_6_laser_aligned_angle['Uncertainty in Voltage'])))
print(Reflectance_laser_aligned_angle)

## Wavelengths ## 
Wavelengths = (np.asarray((Table_1_control['Filter'])))
print(Wavelengths)

## Angles ##
Angles = (np.asarray((Table_5_alum_angle['Angle of Incidence'])))
Angles_err = (np.asarray((Table_5_alum_angle['Uncertainty In Angle'])))
print(Angles)
print(Angles_err)


# ## Manipulating the data to be usable:

# In[3]:


def Object_to_float(Object_array):
    for i in range(len(Object_array)):
        Object_array[i] = eval(Object_array[i])

Object_to_float(Initial_reflectance)
Object_to_float(Initial_reflectance_err)
print(Initial_reflectance_err)

Object_to_float(Reflectance_alum)
Object_to_float(Reflectance_alum_err)
print(Reflectance_alum)


Object_to_float(Reflectance_gold)
Object_to_float(Reflectance_gold_err)
print(Reflectance_gold)

Object_to_float(Reflectance_laser_aligned)
Object_to_float(Reflectance_laser_aligned_err)
print(Reflectance_laser_aligned)

Object_to_float(Reflectance_alum_angle)
Object_to_float(Reflectance_alum_angle_err)
print(Reflectance_alum_angle)


Object_to_float(Reflectance_laser_aligned_angle)
Object_to_float(Reflectance_laser_aligned_angle_err)
print(Reflectance_laser_aligned_angle)



# ## Creating x and y data for plotting

# In[4]:


def r_tot(control, test, new):
    for i in range(len(test)):
        d = test[i] / control[i]
        new.append(d)
        

Reflectance_alum_new = []
r_tot(Initial_reflectance, Reflectance_alum, Reflectance_alum_new )
print(Reflectance_alum_new)

Reflectance_gold_new = []
r_tot(Initial_reflectance, Reflectance_gold, Reflectance_gold_new)
print(Reflectance_gold_new)

Reflectance_laser_aligned_new = []
r_tot(Initial_reflectance, Reflectance_laser_aligned, Reflectance_laser_aligned_new)
print(Reflectance_laser_aligned_new)

Reflectance_alum_angle_new = Reflectance_alum_angle / Initial_reflectance[2]
print(Reflectance_alum_angle_new)

Reflectance_laser_aligned_angle_new = Reflectance_laser_aligned_angle / Initial_reflectance[2]
print(Reflectance_laser_aligned_angle_new)
    


# ## Getting Y Uncertainties

# In[5]:


def dy(measurment1, measurment1_err, measurment2, measurment2_err, new, dy):
    for i in range(len(new)):
        unc = np.sqrt( (measurment1_err[i])**2 + (measurment2_err[i] )) 
        dy.append(unc)
        
    
dy_alum = []
dy(Reflectance_alum, Reflectance_alum_err, Initial_reflectance, Initial_reflectance_err, Reflectance_alum_new, dy_alum)
print(dy_alum)

dy_gold = [] 
dy(Reflectance_gold, Reflectance_gold_err, Initial_reflectance, Initial_reflectance_err, Reflectance_gold_new, dy_gold )
print(dy_gold)

dy_laser_aligned = []
dy(Reflectance_laser_aligned, Reflectance_laser_aligned_err, Initial_reflectance, Initial_reflectance_err, Reflectance_laser_aligned_new, dy_laser_aligned )
print(dy_laser_aligned)

dy_alum_angle = []
dy(Reflectance_alum_angle, Reflectance_alum_angle_err, Initial_reflectance, Initial_reflectance_err, Reflectance_alum_angle_new, dy_alum_angle)
print(dy_alum_angle)

dy_laser_aligned_angle = []
dy(Reflectance_laser_aligned_angle, Reflectance_laser_aligned_angle_err, Initial_reflectance, Initial_reflectance_err, Reflectance_laser_aligned_angle_new, dy_laser_aligned_angle )
print(dy_laser_aligned_angle)


# # Plotting the Data

# In[6]:


## Trial 1 ##
plt.figure()
plt.errorbar(Wavelengths, Reflectance_alum_new, yerr=dy_alum, color='r', fmt='.b', label='Data Alum')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('(R_test)/(R_control)')
plt.title( 'Trial 1: Aluminum Mirror')
plt.legend()
plt.savefig('Trial 1: Aluminum Mirror')
plt.show()

## Trial 2 ##
plt.figure()
plt.errorbar(Wavelengths, Reflectance_gold_new, yerr=dy_gold, fmt='.b', color='b', label='Data Gold')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('(R_test)/(R_control)')
plt.title('Trial 2: Gold Mirror')
plt.legend()
plt.savefig('Trial 2: Gold Mirror')
plt.show()

## trial 3 ##
plt.figure()
plt.errorbar(Wavelengths, Reflectance_laser_aligned_new, yerr=dy_laser_aligned, fmt='.b', color='g', label='Data Laser Aligned')
plt.grid()
plt.xlabel('Wavelength')
plt.ylabel('(R_test)/(R_control)')
plt.title('Trial 3: Laser Aligned Mirror')
plt.legend()
plt.savefig('Trial 3: Laser Aligned Mirror')
plt.show()

## Trial 4 ##
plt.figure()
plt.errorbar(Angles, Reflectance_alum_angle_new, xerr=Angles_err, yerr=dy_alum_angle, fmt='.b', color='b', label='Data Alum')
plt.grid()
plt.xlabel('Angle (Degrees)')
plt.ylabel('(R_test)/(R_control)')
plt.title('Trial 4: Aluminum')
plt.legend()
plt.savefig('Trial 4: Aluminum')
plt.show()

## Trial 5 ##
plt.figure()
plt.errorbar(Angles, Reflectance_laser_aligned_angle_new, xerr=Angles_err, yerr=dy_laser_aligned_angle, fmt='.b', color='r', label='Data Laser Aligned')
plt.grid()
plt.xlabel('Angle (Degrees)')
plt.ylabel('(R_test)/(R_control)')
plt.title('Trial 5: Laser Aligned')
plt.legend()
plt.savefig('Trial 5: Laser Aligned')
plt.show()


# # Part 2: Lens Relay

# # Importing Image Data
# 
# ## Trial 1

# In[7]:


# Importing 1st part of Lens relay images
imagefile_1st_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/1st lense midpoint same settings OD filter 1.0.jpg'
A_1 = plt.imread(imagefile_1st_lens)

imagefile_2nd_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/2nd lesnse midpoint same settings OD filter 0.6.jpg'
A_2 = plt.imread(imagefile_2nd_lens);

imagefile_3rd_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/3rd lense mdipoint same settings.jpg'
A_3 = plt.imread(imagefile_3rd_lens);


# ## Data Manipulation to Get Irrandiance 

# In[8]:


# Performing Normalization of data and cutting the data

#1st Lense
A_1 = A_1/255                          
A_1 = np.mean(A_1[:,:,0:2],2)
print(A_1)
col_1 = round(np.shape(A_1)[1]/2)
cut_1 = (A_1[:,col_1])*10;           
softcut_1 = np.convolve(cut_1,np.ones(10),'valid')/10

# 2nd Lense
A_2 = A_2/255;                        
A_2 = np.mean(A_2[:,:,0:2],2)
print(A_2)
col_2 = round(np.shape(A_2)[1]/2)
cut_2 = (A_2[:,col_2])*10**.6                     
softcut_2 = np.convolve(cut_2,np.ones(10),'valid')/10

# 3rd Lense
A_3 = A_3/255;                          
A_3 = np.mean(A_3[:,:,0:2],2)
print(A_3)
col_3 = round(np.shape(A_3)[1]/2)
cut_3 = A_3[:,col_3];                     
softcut_3 = np.convolve(cut_3,np.ones(10),'valid')/10


# ## Creating x-Coordinates

# In[9]:


# X Data for graphing

x_1 = np.linspace(0, 100, num = 1024, endpoint = True, retstep = False, dtype = None)
x_2 = np.linspace(0, 100, num = 1015, endpoint = True, retstep = False, dtype = None)


# ## Plotting Data

# In[10]:


plt.figure()
plt.grid()
plt.plot(x_1,cut_1, label='Closest Lens');                      
plt.plot(x_1,cut_2, label='Middle Lens');
plt.plot(x_1,cut_3, label='Farthest Lens'); 
plt.xlabel('Distance Along Cut (%)')
plt.ylabel('(Irradiance')
plt.title('Trial 1: Lens Relay Rough')
plt.legend()
plt.savefig('Trial 1: Lens Relay Rough')
plt.show()

plt.figure()
plt.grid()
plt.plot(x_2,softcut_1, label='Closest Lens')                      
plt.plot(x_2,softcut_2, label='Middle Lens');                     
plt.plot(x_2,softcut_3, label='Farthest Lens');
plt.xlabel('Distance Along Cut (%)')
plt.ylabel('Irradiance')
plt.title('Trial 1: Lens Relay Smoothed')
plt.legend()
plt.savefig('Trial 1: Lens Relay Smoothed')
plt.show()


# ## Trial 2
# 
# ##### Key Difference was the 3rd lense and the 2nd lense were swapped

# In[11]:


# Importing 1st part of Lens relay images
imagefile_1st_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/1st lense midpoint same settings 3rd and 2nd mirrors swapped OD 1.0 Filter.jpg'
A_1 = plt.imread(imagefile_1st_lens)

imagefile_2nd_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/2nd lense midpoint same settings 3rd and 2nd mirrors swapped OD 0.3 filter.jpg'
A_2 = plt.imread(imagefile_2nd_lens);

imagefile_3rd_lens = '/Users/benjaminhogan/Library/Mobile Documents/com~apple~CloudDocs/School/Optics/Chapter 2/Part 2 Image Data/3rd lense midpoint same settings 3rd and 2nd mirrors swapped.jpg'
A_3 = plt.imread(imagefile_3rd_lens);


# In[12]:


# Performing Normalization of data and cutting the data

#1st Lense
A_1 = A_1/255                          
A_1 = np.mean(A_1[:,:,0:2],2)
print(A_1)
col_1 = round(np.shape(A_1)[1]/2)
cut_1 = (A_1[:,col_1])*10;           
softcut_1 = np.convolve(cut_1,np.ones(10),'valid')/10

# 2nd Lense
A_2 = A_2/255;                        
A_2 = np.mean(A_2[:,:,0:2],2)
print(A_2)
col_2 = round(np.shape(A_2)[1]/2)
cut_2 = (A_2[:,col_2])*10**.3                     
softcut_2 = np.convolve(cut_2,np.ones(10),'valid')/10

# 3rd Lense
A_3 = A_3/255;                          
A_3 = np.mean(A_3[:,:,0:2],2)
print(A_3)
col_3 = round(np.shape(A_3)[1]/2)
cut_3 = A_3[:,col_3];                     
softcut_3 = np.convolve(cut_3,np.ones(10),'valid')/10


# In[13]:


# X Data for graphing

x_1 = np.linspace(0, 100, num = 1024, endpoint = True, retstep = False, dtype = None)
x_2 = np.linspace(0, 100, num = 1015, endpoint = True, retstep = False, dtype = None)


# In[14]:


plt.figure()
plt.grid()
plt.plot(x_1,cut_1, label='Closest Lens');                      
plt.plot(x_1,cut_2, label='Middle Lens');
plt.plot(x_1,cut_3, label='Farthest Lens'); 
plt.xlabel('Distance Along Cut (%)')
plt.ylabel('(Irradiance')
plt.title('Trial 2: Lens Relay Rough')
plt.legend()
plt.savefig('Trial 2: Lens Relay Rough')
plt.show()

plt.figure()
plt.grid()
plt.plot(x_2,softcut_1, label='Closest Lens')                      
plt.plot(x_2,softcut_2, label='Middle Lens');                     
plt.plot(x_2,softcut_3, label='Farthest Lens');
plt.xlabel('Distance Along Cut (%)')
plt.ylabel('Irradiance')
plt.title('Trial 2: Lens Relay Smoothed')
plt.legend()
plt.savefig('Trial 2: Lens Relay Smoothed')
plt.show()

