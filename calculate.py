#Importing python libraries and defining functions

import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style # import style module

def radose_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
        list = []
    else: 
        for A in dose:
                list.append((F*Rt*E*(A/(A+Kd))))
                
    if len(dose2) == 0: 
        list2 = []           
    else: 
        for A in dose2:
                list2.append((ex2_F*ex2_Rt*ex2_E*(A/(A+ex2_Kd))))
      
    if len(dose3) == 0: 
        list3 = []
    else: 
        for A in dose3:
                list3.append((ex3_F*ex3_Rt*ex3_E*(A/(A+ex3_Kd))))      
                
    if len(dose4) == 0: 
        list4 = []
    else: 
        for A in dose4:
                list4.append((ex4_F*ex4_Rt*ex4_E*(A/(A+ex4_Kd))))       
                
    return list, list2, list3, list4

ralist, ralist2, ralist3, ralist4 = radose_func()

#print("RALIST")
#print(ralist, ralist2, ralist3, ralist4)

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
                    list.append(math.log(A,10))
                    
    if len(dose2) == 0: 
        list2 = []              
    else:                
        for A in dose2:
                if type(A) == int or float:
                    list2.append(math.log(A,10))
                    
    if len(dose3) == 0: 
        list3 = []             
    else:                
        for A in dose3:
                if type(A) == int or float:
                    list3.append(math.log(A,10))
                    
    if len(dose4) == 0: 
        list4 = []               
    else:                           
        for A in dose4:
                if type(A) == int or float:
                    list4.append(math.log(A,10))
    return list, list2, list3, list4

ldlist, ldlist2, ldlist3, ldlist4 = log_dose_func()
                   
#print("LDLIST")
#print(ldlist, ldlist2, ldlist3, ldlist4)

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
            list3.append((A - ex3_threshold)/(ex3_capacity - ex3_threshold)*100)
   
    
    if len(dose4) == 0: 
        list4 = []
    else:
        for A in ralist4:
            list4.append((A - ex4_threshold)/(ex4_capacity - ex4_threshold)*100)      
    return list, list2, list3, list4

ectlist, ectlist2, ectlist3, ectlist4 = effect_ct_func()

#print("ECT LIST")
#print(ectlist, ectlist2, ectlist3, ectlist4)


def effect_assay_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose) == 0: 
       list = []
    else:
        for A in ectlist:
            if A <= 0:
                A = 0
            elif A >= 100:
                 A = 100
            list.append(A)
    
            
    if len(dose2) == 0: 
        list2 = []
    else:
        for A in ectlist2:
            if A <= 0:
                A = 0
            elif A >= 100:
                A = 100
            list2.append(A)
    

    if len(dose3) == 0: 
        eaf_list3 = []
    else:
        for A in ectlist3:
            if A <= 0:
                A = 0
            elif A >= 100:
                A = 100
            list3.append(A)
    
    if len(dose4) == 0: 
        eaf_list4 = []
    else:
        for A in ectlist4:
            if A <= 0:
                A = 0
            elif A >= 100:
                A = 100
            list4.append(A)
    return list, list2, list3, list4

ealist, ealist2, ealist3, ealist4 = effect_assay_func()

#print("EA List")
#print(ealist, ealist2, ealist3, ealist4)

#creating zipped lists

zippedList = list(zip(dose, ldlist, ralist, ectlist, ealist))
zippedList2 = list(zip(dose2, ldlist2, ralist2, ectlist2, ealist2))
zippedList3 = list(zip(dose3, ldlist3, ralist3, ectlist3, ealist3))
zippedList4 = list(zip(dose4, ldlist4, ralist4, ectlist4, ealist4))

# Creating the DataFrame
# Adding new columns Dose, log(Dose), RA, Effect(C-T), Effect(Assay)

df = pd.DataFrame(zippedList, columns = ['Dose','log(Dose)','RA', 'Effect(C-T)','Effect(Assay)'])
dfrounded = df.round({"Dose":4,"log(Dose)":1,"RA":1, "Effect(C-T)":1, "Effect(Assay)":1})

df2 = pd.DataFrame(zippedList2, columns = ['Dose','log(Dose)','RA', 'Effect(C-T)','Effect(Assay)'])
df2rounded = df2.round({"Dose":4,"log(Dose)":1,"RA":1, "Effect(C-T)":1, "Effect(Assay)":1})

df3 = pd.DataFrame(zippedList3, columns = ['Dose','log(Dose)','RA', 'Effect(C-T)','Effect(Assay)'])
df3rounded = df3.round({"Dose":4,"log(Dose)":1,"RA":1, "Effect(C-T)":1, "Effect(Assay)":1})

df4 = pd.DataFrame(zippedList4, columns = ['Dose','log(Dose)','RA', 'Effect(C-T)','Effect(Assay)'])
df4rounded = df4.round({"Dose":4,"log(Dose)":1,"RA":1, "Effect(C-T)":1, "Effect(Assay)":1})

style.use("ggplot")

#fig = plt.figure(figsize=(8,5))

#ax = fig.add_subplot(121)

f, ax = plt.subplots(figsize=(8,5))

ax.set_xscale('log')
ax.set_xlim(.001,1000)
ax.set_ylim(-5,105)
ax.set_xticks([.001,.01,.1,1,10,100,1000])
ax.set_xticklabels([.001,.01,.1,1,10,100,1000])

ax.scatter(dfrounded['Dose'], dfrounded['Effect(Assay)'], label = "EXP1")
ax.plot(dfrounded['Dose'], dfrounded['Effect(Assay)'])

ax.scatter(df2rounded['Dose'], df2rounded['Effect(Assay)'], label = "EXP2")
ax.plot(df2rounded['Dose'], df2rounded['Effect(Assay)'])

ax.scatter(df3rounded['Dose'], df3rounded['Effect(Assay)'], label = "EXP3")
ax.plot(df3rounded['Dose'], df3rounded['Effect(Assay)'])

ax.scatter(df4rounded['Dose'], df4rounded['Effect(Assay)'], label = "EXP4")
ax.plot(df4rounded['Dose'], df4rounded['Effect(Assay)'])

plt.title("Log(Dose) Effect Curve")
plt.xlabel("Dose")
plt.ylabel("Effect(Assay)")
plt.legend(loc = 2)

plt.show()

print('EXP1')
display(dfrounded)

print('EXP2')
display(df2rounded)

print('EXP3')
display(df3rounded)

print('EXP4')
display(df4rounded)
