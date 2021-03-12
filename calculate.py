#Importing python libraries and defining functions

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def radose_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
        list = []
    else: 
        for A in dose:
                list.append(round((F*Rt*E*(A/(A+Kd))),2))
                
    if len(dose2) == 0: 
        list2 = []           
    else: 
        for A in dose2:
                list2.append(round((ex2_F*ex2_Rt*ex2_E*(A/(A+ex2_Kd))),2))
      
    if len(dose3) == 0: 
        list3 = []
    else: 
        for A in dose3:
                list3.append(round((ex3_F*ex3_Rt*ex3_E*(A/(A+ex3_Kd))),2))         
                
    if len(dose4) == 0: 
        list4 = []
    else: 
        for A in dose4:
                list4.append(round((ex4_F*ex4_Rt*ex4_E*(A/(A+ex4_Kd))),2))         
                
    return list, list2, list3, list4

ralist, ralist2, ralist3, ralist4 = radose_func()

#testing# print(ralist, ralist2)
                
def log_dose_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
        list = []
    else:
        for A in dose:
                if type(A) == int or float:
                    list.append(round(math.log(A,10),1))
                    
    if len(dose2) == 0: 
        list2 = []              
    else:                
        for A in dose2:
                if type(A) == int or float:
                    list2.append(round(math.log(A,10),1))
                    
    if len(dose3) == 0: 
        list3 = []             
    else:                
        for A in dose3:
                if type(A) == int or float:
                    list3.append(round(math.log(A,10),1)) 
                    
    if len(dose4) == 0: 
        list4 = []               
    else:                           
        for A in dose4:
                if type(A) == int or float:
                    list4.append(round(math.log(A,10),1))
    return list, list2, list3, list4

ldlist, ldlist2, ldlist3, ldlist4 = log_dose_func()

#Testing# print(ldlist, ldlist2)
                   

def effect_ct_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
        list = []
    else:
        for A in ralist:
            list.append((A - threshold)/(capacity - threshold)*100)
  
            
    if len(dose2) == 0: 
        list2 = []
    else:
        for A in ralist2:
            list2.append((A - ex2_threshold)/(ex2_capacity - ex2_threshold)*100)
            
         
    if len(dose3) == 0: 
        list3 = []
    else:
        for A in ralist3:
            list3.append((A - threshold)/(capacity - threshold)*100)
   
    
    if len(dose4) == 0: 
        list4 = []
    else:
        for A in ralist4:
            list4.append((A - threshold)/(capacity - threshold)*100)
            
    return list,list2,list3,list4

ectlist, ectlist2, ectlist3, ectlist4 = effect_ct_func()

def effect_assay_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
        list = []
    else:
        for A in ralist:
            if A <= 0:
                A = 0
            if A >= 100:
                A = 100
            list.append(round(A,2))
    
            
    if len(dose2) == 0: 
        list2 = []
    else:
        for A in ralist2:
            if A <= 0:
                A = 0
            if A >= 100:
                A = 100
            list2.append(round(A,2))
    

    if len(dose3) == 0: 
        list3 = []
    else:
        for A in ralist3:
            if A <= 0:
                A = 0
            if A >= 100:
                A = 100
            list3.append(round(A,2))
    
    if len(dose4) == 0: 
        list4 = []
    else:
        for A in ralist4:
            if A <= 0:
                A = 0
            if A >= 100:
                A = 100
            list4.append(round(A,2))
    
    return list,list2,list3,list4

ealist, ealist2, ealist3, ealist4 = effect_assay_func()
   
zippedList = list(zip(dose, ldlist, ectlist))
zippedList2 = list(zip(dose2, ldlist2, ectlist2))
zippedList3 = list(zip(dose3, ldlist3, ectlist3))
zippedList4 = list(zip(dose4, ldlist4, ectlist4))

calculations_zl = list(zip(ralist, ectlist, ealist))
calculations_zl2 = list(zip(ralist2, ectlist2, ealist2))
calculations_zl3 = list(zip(ralist3, ectlist3, ealist3))
calculations_zl4 = list(zip(ralist4, ectlist4, ealist4))

# Creating the DataFrame 

df = pd.DataFrame(zippedList, columns = ['Dose','log(Dose)','effect_assay'])
df2 = pd.DataFrame(zippedList2, columns = ['Dose','log(Dose)','effect_assay'])
df3 = pd.DataFrame(zippedList3, columns = ['Dose','log(Dose)','effect_assay'])
df4 = pd.DataFrame(zippedList4, columns = ['Dose','log(Dose)','effect_assay'])

# Display Calculations
#
# Effect(C-T) determines gross effect as %MPE in assay given Threshold T and Ceiling C as Effect=((RA-T)/(C-T))*100
#
#

calculations1 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations2 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations3 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])
calculations4 = pd.DataFrame(zippedList, columns =  ['RA(Dose)','Effect(C-T)', 'Effect(Assay)'])

from matplotlib import style # import style module
style.use("ggplot")

#fig = plt.figure(figsize=(8,5))

#ax = fig.add_subplot(121)

f, ax = plt.subplots(figsize=(10,8))

ax.set_xscale('log')
ax.set_xlim(.001,1000)
ax.set_xticks([.001,.01,.1,1,10,100,1000])
ax.set_xticklabels([.001,.01,.1,1,10,100,1000])

ax.scatter(df['Dose'], df['effect_assay'], label = "EXP1")
ax.plot(df['Dose'], df['effect_assay'])

ax.scatter(df2['Dose'], df2['effect_assay'], label = "EXP2")
ax.plot(df2['Dose'], df2['effect_assay'])

ax.scatter(df3['Dose'], df3['effect_assay'], label = "EXP3")
ax.plot(df3['Dose'], df3['effect_assay'])

ax.scatter(df4['Dose'], df4['effect_assay'], label = "EXP4")
ax.plot(df4['Dose'], df4['effect_assay'])

plt.title("Log(Dose) Effect Curve")
plt.xlabel("Dose")
plt.ylabel("Effect Assay")
plt.legend(loc = 2)

plt.show()

print('EXP1')
display(df)

print('EXP2')
display(df2)

print('EXP3')
display(df3)

print('EXP4')
display(df4)
