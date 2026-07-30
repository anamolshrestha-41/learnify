#Boolean Masking allows us to filter arrays using conditions

import numpy as np

numbers= np.array([10,20,30,5,60,25,40])
mask= numbers>30
print(mask) #[False False False False  True False  True]
print(numbers[mask]) #[60 40]
#oR
print(numbers[numbers>30]) #[60 40]
print(numbers[(numbers>10)&(numbers<30)]) #[20 25]

#Practice task!
score= np.array([45, 78, 90, 32, 88, 60, 25])
print(f"Score greater than 50: {score[score>50]}")
print(f"Scores between 50 and 80: {score[(score > 50) & (score<80)]}")
print(f" Score below 40: {score[score<40]}")