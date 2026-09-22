
favorable_outcomes= 1
total_outcomes= 6
prob_of_rol_four=favorable_outcomes / total_outcomes
print(f"{prob_of_rol_four * 100} %")

# using dataset
salaries=[35000, 42000, 55000, 70000, 95000]
# What is the probability that a randomly selected employee earns more than 60000?
favorable_outcomes=2
total_outcomes=5
prob_of_sixthou_more= favorable_outcomes/total_outcomes
print(f"{prob_of_sixthou_more * 100}%")

sample_space= {1,2,3,4,5,6}
event={2,4,6}
prob= len(event)/len(sample_space)
print(f"{prob*100}%")

#using dataset
ages=[22,25,28, 30, 35, 40, 45, 50, 55, 60]
old_than_forty=[age for age in ages if age >40]
prob= len(old_than_forty)/len(ages)
print(f" {prob*100}% ")

a={45, 50, 55, 60}
b={50, 55, 60, 70}
print(f"A OR B: {a|b} , A AND B: {a&b} ")

dice={1,2,3,4,5,6}
odd= [d for d in dice if d%2!=0]
print(f"prob: {(len(odd)/len(dice))*100}%")

#complement rule
p_rain= 0.30
p_norain= 1-p_rain
print(p_norain)

#addition rule
p_a_or_b= len(a)+len(b)-len(a & b)
print(f" Additional Rule: {p_a_or_b}  ")

from scipy.stats import bernoulli, binom, uniform, norm, poisson, expon
result= bernoulli.rvs(0.7)
print(result)
result= binom.rvs(
    n=10,
    p=0.5
)
print(result)
result= uniform.rvs(
    loc=0, scale=1, size=10
)
print(result)
result= norm.rvs(
    loc=0,
    scale=1,
    size=10
)
print(result)

values = poisson.rvs(
    mu=5,
    size=10
)

print(values)

values = expon.rvs(
    scale=2,
    size=10
)

print(values)

import pandas as pd

data = pd.DataFrame({
    "gender": ["Male", "Male", "Female", "Female"],
    "sport": ["Football", "Cricket", "Football", "Cricket"]
})

pd.crosstab(
    data["gender"],
    data["sport"],
    margins=True
)