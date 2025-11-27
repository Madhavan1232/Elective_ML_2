import numpy as np

np.random.seed(42)

n = int(input())

die1 = np.random.randint(1, 7, n)
die2 = np.random.randint(1, 7, n)
sums = die1 + die2

simple_prob = np.sum(sums > 8) / n

even_first = (die1 % 2 == 0)
second_gt_3 = die2 > 3
joint_prob = np.sum(even_first & second_gt_3) / n

first_4 = die1 == 4
sum_7 = sums == 7
count_first_4 = np.sum(first_4)
count_both = np.sum(first_4 & sum_7)
if count_first_4 > 0:
    cond_prob = count_both / count_first_4
else:
    cond_prob = 0.0

print("Simple Probability (Sum > 8):")
print(simple_prob)
print("\nJoint Probability (First even AND Second > 3):")
print(joint_prob)
print("\nConditional Probability (Sum = 7 | First die = 4):")
print(cond_prob)