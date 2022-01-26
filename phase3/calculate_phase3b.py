#Importing python libraries and defining functions
import sys
sys.path.insert(1, 'media')
import math
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style # import style module
import test2
#print("Doses")
#print(dose,doseB)
#phase2

## Tissue Parameters

F = test2.F
Rt = test2.Rt

## Drug Parameters

Ea = test2.Ea
Ka = test2.Ka
Eb = test2.Eb
Kb = test2.Kb

## Assay Parameters

threshold = test2.threshold
capacity = test2.capacity

## Tissue Parameters

ex2_F = test2.ex2_F
ex2_Rt = test2.ex2_Rt

## Drug Parameters

ex2_Ea = test2.ex2_Ea
ex2_Ka = test2.ex2_Ka
ex2_Eb = test2.ex2_Eb
ex2_Kb = test2.ex2_Kb

## Assay Parameters

ex2_threshold = test2.ex2_threshold
ex2_capacity = test2.ex2_capacity

## Tissue Parameters

ex3_F = test2.ex3_F
ex3_Rt = test2.ex3_Rt

## Drug Parameters

ex3_Ea = test2.ex3_Ea
ex3_Ka = test2.ex3_Ka
ex3_Eb = test2.ex3_Eb
ex3_Kb = test2.ex3_Kb

## Assay Parameters

ex3_threshold = test2.ex3_threshold
ex3_capacity = test2.ex3_capacity

## Tissue Parameters

ex4_F = test2.ex4_F
ex4_Rt = test2.ex4_Rt

## Drug Parameters

ex4_Ea = test2.ex4_Ea
ex4_Ka = test2.ex4_Ka
ex4_Eb = test2.ex4_Eb
ex4_Kb = test2.ex4_Kb

## Assay Parameters

ex4_threshold = test2.ex4_threshold
ex4_capacity = test2.ex4_capacity

def froa_func():
    global dose_B
    global ex2_dose_B
    global ex3_dose_B
    global ex4_dose_B
    
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
    else:
        if dose_B == 0:
            eq1 = 1
        else:
            eq1 = (1+dose_B/Kb)
    for A in dose_A:
        list.append((A/(A+Ka*(eq1))))
#    
    if len(ex2_dose_A) == 0: 
        list2 = []
    else:
        if ex2_dose_B == 0:
            eq2 = 1
        else:
            eq2 = (1+ex2_dose_B/ex2_Kb)
    for A in ex2_dose_A:
        list2.append((A/(A+ex2_Ka*(eq2))))
#    
    if len(ex3_dose_A) == 0: 
        list3 = []  
    else:
        if ex3_dose_B == 0:
            eq3 = 1
        else:
            eq3 = (1+ex3_dose_B/ex3_Kb)
    for A in ex3_dose_A:
        list3.append((A/(A+ex3_Ka*(eq3))))
#    
    if len(ex4_dose_A) == 0: 
        list4 = []
    else:
        if ex4_dose_B == 0:
            eq4 = 1
        else:
            eq4 = (1+ex4_dose_B/ex4_Kb)
    for A in ex4_dose_A:
        list4.append((A/(A+ex4_Ka*(eq4))))
        
    return list,list2,list3,list4
                         
froa, froa2, froa3, froa4 = froa_func()

#print(froa2)

def frob_func():
    
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
    else:    
        for A in dose_A:
            list.append((dose_B/(dose_B+Kb*(1+A/Ka))))
            
    if len(ex2_dose_A) == 0: 
        list2 = []
    else:    
        for A in ex2_dose_A:
            list2.append((ex2_dose_B/(ex2_dose_B+ex2_Kb*(1+A/ex2_Ka))))
    
    if len(ex3_dose_A) == 0: 
        list3 = []
    else:    
        for A in ex3_dose_A:
            list3.append((ex3_dose_B/(ex3_dose_B+ex3_Kb*(1+A/ex3_Ka))))
    
    if len(ex4_dose_A) == 0: 
        list4 = []
    else:    
        for A in ex4_dose_A:
            list4.append((ex4_dose_B/(ex4_dose_B+ex4_Kb*(1+A/ex4_Ka))))
            
    return list,list2,list3,list4
                         
frob, frob2, frob3, frob4 = frob_func()
                         
#print("FROb_LIST")
#print(frob)

def radose_func2():
    list = []
    list2 = []
    list3 = []
    list4 = []
                
    if len(dose_A) == 0: 
        list = []
    else:    
        for A in dose_A:        
               list.append((F*Rt*(Ea*A/(A+Ka*(1+dose_B/Kb))+(Eb*dose_B/(dose_B+Kb*(1+A/Ka))))))
                
    if len(ex2_dose_A) == 0:
        list2 = []
    else:    
        for A in ex2_dose_A:        
                list2.append((ex2_F*ex2_Rt*(ex2_Ea*A/(A+ex2_Ka*(1+ex2_dose_B/ex2_Kb))+(ex2_Eb*ex2_dose_B/(ex2_dose_B+ex2_Kb*(1+A/ex2_Ka))))))

    if len(ex3_dose_A) == 0:
        list3 = []
    else:    
        for A in ex3_dose_A:        
               list3.append((ex3_F*ex3_Rt*(ex3_Ea*A/(A+ex3_Ka*(1+ex3_dose_B/ex3_Kb))+(ex3_Eb*ex3_dose_B/(ex3_dose_B+ex3_Kb*(1+A/ex3_Ka))))))
                
    if len(ex4_dose_A) == 0: 
        list4 = []
    else:    
        for A in ex4_dose_A:        
               list4.append((ex4_F*ex4_Rt*(ex4_Ea*A/(A+ex4_Ka*(1+ex4_dose_B/ex4_Kb))+(ex4_Eb*ex4_dose_B/(ex4_dose_B+ex4_Kb*(1+A/ex4_Ka))))))            
    return list, list2, list3, list4

ra, ra2, ra3, ra4 = radose_func2()

#print("exported lists")
#print(ra,ra2)

#phase1

def receptor_occupancy():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
    else: 
        for A in dose_A:
                list.append((A/(A+Ka)))
    
    if len(ex2_dose_A) == 0: 
        list2 = []
    else: 
        for A in ex2_dose_A:
                list2.append((A/(A+ex2_Ka)))
    
    if len(ex3_dose_A) == 0: 
        list3 = []
    else: 
        for A in ex3_dose_A:
                list3.append((A/(A+ex3_Ka)))
            
    if len(ex4_dose_A) == 0: 
        list4 = []
    else: 
        for A in ex4_dose_A:
                list4.append((A/(A+ex4_Ka)))
            
    return list, list2, list3, list4

rolist, rolist2, rolist3, rolist4 = receptor_occupancy()
            
def radose_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
    else: 
        for A in dose_A:
                list.append((F*Rt*Ea*(A/(A+Ka))))
                
    if len(ex2_dose_A) == 0: 
        list2 = []           
    else: 
        for A in ex2_dose_A:
                list2.append((ex2_F*ex2_Rt*ex2_Ea*(A/(A+ex2_Ka))))
      
    if len(ex3_dose_A) == 0: 
        list3 = []
    else: 
        for A in ex3_dose_A:
                list3.append((ex3_F*ex3_Rt*ex3_Ea*(A/(A+ex3_Ka))))      
                
    if len(ex4_dose_A) == 0: 
        list4 = []
    else: 
        for A in ex4_dose_A:
                list4.append((ex4_F*ex4_Rt*ex4_Ea*(A/(A+ex4_Ka))))       
                
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
    
    if len(dose_A) == 0: 
        list = []
    else:
        for A in dose_A:
            if A != 0:
                if type(A) == int or float:
                    list.append(math.log(A,10))
            else:
                 list.append(None)
                    
    if len(ex2_dose_A) == 0: 
        list2 = []
    else:
        for A in ex2_dose_A:
            if A != 0:
                if type(A) == int or float:
                    list2.append(math.log(A,10))
            else:
                 list2.append(None)
                    
    if len(ex3_dose_A) == 0: 
        list3 = []
    else:
        for A in ex3_dose_A:
            if A != 0:
                if type(A) == int or float:
                    list3.append(math.log(A,10))
            else:
                 list.append(None)
                    
    if len(ex4_dose_A) == 0: 
        list4 = []
    else:
        for A in ex4_dose_A:
            if A != 0:
                if type(A) == int or float:
                    list4.append(math.log(A,10))
            else:
                 list4.append(None)
                    
    return list, list2, list3, list4

ldlist, ldlist2, ldlist3, ldlist4 = log_dose_func()

#print(ldlist)

#logdose B              
def log_doseb_func():
    global dose_B
    global ex2_dose_B
    global ex3_dose_B
    global ex4_dose_B
    
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
        
    else:
        if dose_B == 0:
            for A in dose_A:
                list.append(None)
        else:        
            if type(dose_B) == int or float:
                for A in dose_A:
                    list.append(math.log(dose_B,10))
                    
    if len(ex2_dose_A) == 0: 
        list2 = []    
    else:
        if ex2_dose_B == 0:
            for A in ex2_dose_A:
                list2.append('')
        else:        
            if type(ex2_dose_B) == int or float:
                for A in ex2_dose_A:
                    list2.append(math.log(ex2_dose_B,10))
    
    if len(ex3_dose_A) == 0: 
        list3 = []    
    else:
        if ex3_dose_B == 0:
            for A in ex3_dose_A:
                list3.append('')
        else:        
            if type(ex3_dose_B) == int or float:
                for A in ex3_dose_A:
                    list3.append(math.log(ex3_dose_B,10))
                    
    if len(ex4_dose_A) == 0: 
        list4 = []    
    else:
        if ex4_dose_B == 0:
            for A in ex4_dose_A:
                list4.append('')
        else:        
            if type(ex4_dose_B) == int or float:
                for A in ex4_dose_A:
                    list4.append(math.log(ex4_dose_B,10))                
            
    return list, list2, list3, list4

ldblist, ldblist2, ldblist3, ldblist4 = log_doseb_func()

#print("LDLIST")
#print(ldlist, ldlist2, ldlist3, ldlist4)

#adjusted to include new formula

def effect_ct_func():
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    if len(dose_A) == 0: 
        list = []
    else:
        for A in ra:
            list.append((A - threshold)/(capacity - threshold)*100)
            
            
    if len(ex2_dose_A) == 0: 
        list2 = []
    else:
        for A in ra2:
            list2.append((A - ex2_threshold)/(ex2_capacity - ex2_threshold)*100)
            
         
    if len(ex3_dose_A) == 0: 
        list3 = []
    else:
        for A in ra3:
            list3.append((A - ex3_threshold)/(ex3_capacity - ex3_threshold)*100)
   
    
    if len(ex4_dose_A) == 0: 
        list4 = []
    else:
        for A in ra4:
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
    
    if len(dose_A) == 0: 
       list = []
    else:
        for A in ectlist:
            if A <= 0:
                A = 0
            elif A >= 100:
                 A = 100
            list.append(A)
    
            
    if len(ex2_dose_A) == 0: 
        list2 = []
    else:
        for A in ectlist2:
            if A <= 0:
                A = 0
            elif A >= 100:
                A = 100
            list2.append(A)
    

    if len(ex3_dose_A) == 0: 
        eaf_list3 = []
    else:
        for A in ectlist3:
            if A <= 0:
                A = 0
            elif A >= 100:
                A = 100
            list3.append(A)
    
    if len(ex4_dose_A) == 0: 
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

def doseb():   
    list = []
    list2 = []
    list3 = []
    list4 = []
    
    for A in dose_A:
        list.append(dose_B)
    for A in ex2_dose_A:
        list2.append(ex2_dose_B)
    for A in ex3_dose_A:
        list3.append(ex3_dose_B)
    for A in ex4_dose_A:
        list4.append(ex4_dose_B)
    return list, list2, list3, list4 

doseb_list, doseb_list2, doseb_list3, doseb_list4 = doseb()

####



zippedList = list(zip(dose_A, ldlist, froa, doseb_list, ldblist, frob, ra, ectlist, ealist))

zippedList2 = list(zip(ex2_dose_A, ldlist2, froa2, doseb_list2, ldblist2, frob2, ra2, ectlist2, ealist2))

zippedList3 = list(zip(ex3_dose_A, ldlist3, froa3, doseb_list3, ldblist3, frob3, ra3, ectlist3, ealist3))

zippedList4 = list(zip(ex4_dose_A, ldlist4, froa4, doseb_list4, ldblist4, frob4, ra4, ectlist4, ealist4))

#(zippedList2)


##
df = pd.DataFrame(zippedList, columns = ['Dose A','log(Dose A)','FRO A','Dose B','log(Dose B)','FRO B','RA','Effect(C-T)','Effect(Assay)'])
#use nan if no results (mainly for consistency)
df = df.fillna(value=np.nan)

dfrounded = df.round({"Dose A":4,"log(Dose A)":2,"FRO A":2, "Dose B":4,"log(Dose B)":2, "FRO B":2,"RA":2, "Effect(C-T)":2, "Effect(Assay)":2})

#removing columns for students
df_remove = dfrounded.filter(['Dose A','log(Dose A)','Dose B','log(Dose B)','Effect(Assay)'])

##
df2 = pd.DataFrame(zippedList2, columns = ['Dose A','log(Dose A)','FRO A','Dose B','log(Dose B)','FRO B','RA','Effect(C-T)','Effect(Assay)'])
df2 = df2.fillna(value=np.nan)

df2rounded = df2.round({"Dose A":4,"log(Dose A)":2,"FRO A":2, "Dose B":4,"log(Dose B)":2, "FRO B":2,"RA":2, "Effect(C-T)":2, "Effect(Assay)":2})

df2_remove = df2rounded.filter(['Dose A','log(Dose A)','Dose B','log(Dose B)','Effect(Assay)'])

##
df3 = pd.DataFrame(zippedList3, columns = ['Dose A','log(Dose A)','FRO A','Dose B','log(Dose B)','FRO B','RA','Effect(C-T)','Effect(Assay)'])

df3 = df3.fillna(value=np.nan)

df3rounded = df3.round({"Dose A":4,"log(Dose A)":2,"FRO A":2, "Dose B":4,"log(Dose B)":2, "FRO B":2,"RA":2, "Effect(C-T)":2, "Effect(Assay)":2})

df3_remove = df3rounded.filter(['Dose A','log(Dose A)','Dose B','log(Dose B)','Effect(Assay)'])

##
df4 = pd.DataFrame(zippedList4, columns = ['Dose A','log(Dose A)','FRO A','DoseB','log(Dose B)','FRO B','RA','Effect(C-T)','Effect(Assay)'])
df4 = df4.fillna(value=np.nan)

df4rounded = df4.round({"Dose A":4,"log(Dose A)":2,"FRO A":2, "Dose B":4,"log(Dose B)":2, "FRO B":2, "RA":2, "Effect(C-T)":2, "Effect(Assay)":2})

df4_remove = df4rounded.filter(['Dose A','log(Dose A)','Dose B','log(Dose B)','Effect(Assay)'])

#dfrounded = df.round({"Dose":4,"DrugB":1})

#df2 = pd.DataFrame(zippedList2, columns = ['Dose','DrugB'])
#df2rounded = df2.round({"Dose":4,"DrugB":1})
                           
#df3 = pd.DataFrame(zippedList3, columns = ['Dose','DrugB'])
#df3rounded = df3.round({"Dose":4,"DrugB":1})
                          
#df4 = pd.DataFrame(zippedList4, columns = ['Dose','DrugB'])
#df4rounded = df4.round({"Dose":4,"DrugB":1})                           

style.use("ggplot")

#fig = plt.figure(figsize=(8,5))

#ax = fig.add_subplot(121)

f, ax = plt.subplots(figsize=(8,5))

ax.set_xscale('log')
ax.set_xlim(.001,1000)
ax.set_ylim(-5,105)
ax.set_xticks([.001,.01,.1,1,10,100,1000])
ax.set_xticklabels([.001,.01,.1,1,10,100,1000])

ax.scatter(dfrounded['Dose A'], dfrounded['Effect(Assay)'], label = "EXP1")
ax.plot(dfrounded['Dose A'], dfrounded['Effect(Assay)'])

ax.scatter(df2rounded['Dose A'], df2rounded['Effect(Assay)'], label = "EXP2")
ax.plot(df2rounded['Dose A'], df2rounded['Effect(Assay)'])

ax.scatter(df3rounded['Dose A'], df3rounded['Effect(Assay)'], label = "EXP3")
ax.plot(df3rounded['Dose A'], df3rounded['Effect(Assay)'])

ax.scatter(df4rounded['Dose A'], df4rounded['Effect(Assay)'], label = "EXP4")
ax.plot(df4rounded['Dose A'], df4rounded['Effect(Assay)'])                           
    
#ax.scatter(df2rounded['Dose'], df2rounded['DrugB'], label = "EXP2")
#ax.plot(df2rounded['Dose'], df2rounded['DrugB'])
                           
#ax.scatter(df3rounded['Dose'], df3rounded['DrugB'], label = "EXP3")
#ax.plot(df3rounded['Dose'], df3rounded['DrugB'])                           

#ax.scatter(df4rounded['Dose'], df4rounded['DrugB'], label = "EXP4")
#ax.plot(df4rounded['Dose'], df4rounded['DrugB'])                           
                           
plt.title("Combinaton of 2 Drugs: Drug A + Fixed Dose of Drug B")
plt.xlabel("Dose")
plt.ylabel("Effect(Assay)")
plt.legend(loc = 2)

plt.show()

print('EXP1')
display(df_remove)

print('EXP2')
display(df2_remove)
                           
print('EXP3')
display(df3_remove)
                           
print('EXP4')
display(df4_remove)
