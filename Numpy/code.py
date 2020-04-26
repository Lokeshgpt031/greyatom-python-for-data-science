# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])


#Code starts here
data_file=path # path for the file
data=np.genfromtxt(data_file, delimiter=",", skip_header=1)

census = np.concatenate((data,new_record),axis=0)
print(census)


# --------------
#Code starts here
import numpy as np

age = census[:,0]


max_age=np.max(age)
min_age = np.min(age)
age_mean=np.mean(age)
age_std = np.std(age)




# --------------
#Code starts here
import numpy as np 
race_0 = np.array(census[census[:,2]==0])
race_1 = np.array(census[census[:,2]==1])
race_2 = np.array(census[census[:,2]==2])
race_3 = np.array(census[census[:,2]==3])
race_4 = np.array(census[census[:,2]==4])

len_0 = len(race_0)
len_1 = len(race_1)
len_2 = len(race_2)
len_3 = len(race_3)
len_4 = len(race_4)

minority_race = 100
"""for i in range(4):
    if (len(np.array(census[census[:,2]==i]))) < minority_race:
        minority_race = i"""

for i in range(4):
    minority_race=100
    if len(np.array(census[census[:,2]==i])) < minority_race:
        minority_race = i

print(minority_race)



# --------------
#Code starts here
import numpy as np
senior_citizens = census[census[:,0]>60]

working_hours_sum = np.sum(senior_citizens[:,6])
print(working_hours_sum)

senior_citizens_len = len(senior_citizens)
print(senior_citizens_len)

avg_working_hours = working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
import numpy as np 

high = np.array(census[census[:,1]>10])
low = np.array(census[census[:,1]<=10])


avg_pay_high = np.mean(high[:,7])
print(avg_pay_high)

avg_pay_low = np.mean(low[:,7])
print(avg_pay_low)


