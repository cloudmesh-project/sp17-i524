import matplotlib as mpl
mpl.use('Agg')

import pandas as pd
import numpy as np
import datetime
import os

import warnings
warnings.filterwarnings("ignore")
import matplotlib.pyplot as plt


#READ 3 MILLIONS ROWS DATASET 
d=pd.read_csv("/home/cc/h1b_m3Rows.csv")

#READ TWO MILLIONS ROWS DATASET FOR BENCHMARKING
#d=pd.read_csv("/home/cc/h1b_m2Rows.csv")
#READ ONE MILLIONS ROWS DATASET FOR BENCHMARKING
#d=pd.read_csv("/home/cc/h1b_m1Rows.csv")
#READ DATASET SUBSET BY DATA SCEINCE RELATED JOB_TITLE ONLY FOR BENCHMARKING
#d=pd.read_csv("/home/cc/h1b_DataScienceOnly.csv")



#CASE_STATUS DISTRIBUTION
print('--------------------------------------------------------------------')
print('****************** CASE STATUS DISTRIBUTION ************************')
print('--------------------------------------------------------------------')
print(d['CASE_STATUS'].value_counts())
print('--------------------------------------------------------------------')
print(' ')

#PETITION PER STATE PER YEAR
d['STATE']=d['WORKSITE'].str.split(', ').str[1]
state_data=d.groupby(['STATE', 'YEAR']).size()
state_year_data=state_data.unstack()
state_year_data['TOTAL'] = state_year_data.sum(axis=1)
print('--------------------------------------------------------------------------------')
print('************************** PETITION PER STATE PER YEAR *************************')
print('--------------------------------------------------------------------------------')
print(state_year_data)
print('--------------------------------------------------------------------------------')
print(' ')


#LOCATION HIRE DATA SCIENTIST THE MOST
location=d[d['JOB_TITLE']=='DATA SCIENTIST']
print('--------------------------------------------------------------------')
print('**************** TOP 25 LOCATION HIRING DATA SCIENTIST *************')
print('--------------------------------------------------------------------')
print(location['WORKSITE'].value_counts().head(25))
print('--------------------------------------------------------------------')
print(' ');

#TOP EMPLOYER HIRE DATA SCIENTIST
employer=d[d['JOB_TITLE']=='DATA SCIENTIST']
print('--------------------------------------------------------------------')
print('************* TOP 25 COMPANY HIRING DATA SCIENTIST *****************')
print('--------------------------------------------------------------------')
print(employer['EMPLOYER_NAME'].value_counts().head(25))
print('--------------------------------------------------------------------')
print(' ')


#DATA SCIENTISTS WAGE DIFFER ACROSS STATES
d.loc[:,'WORKSITE'] = d.loc[:,'WORKSITE'].apply(lambda x:x.split(',')[-1][1:])
job_title_group = d.groupby('JOB_TITLE')
for key in job_title_group.groups.keys():
        if key == 'DATA SCIENTIST':
                d = job_title_group.get_group(key)[['WORKSITE','PREVAILING_WAGE']]


d.boxplot(column = 'PREVAILING_WAGE', by = 'WORKSITE' , fontsize = 6)
plt.xticks(rotation = 45)
plt.savefig("/home/cc/images/wage.png")
