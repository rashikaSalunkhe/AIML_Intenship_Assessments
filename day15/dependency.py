import random

print("----- INDEPENDENT EVENTS -----")

# Probability of Heads on a fair coin
P_heads = 1 / 2

# Probability of rolling a 6 on a fair die
P_six = 1 / 6

# Independent formula
P_independent = P_heads * P_six

print(f"P(Heads) = {P_heads}")
print(f"P(Rolling 6) = {P_six}")
print(f"P(Heads AND 6) = {P_independent}")
print("Final Answer (Independent) = 1/12 ≈", round(P_independent, 4))

print("\n----- DEPENDENT EVENTS -----")

# Total marbles
total_marbles = 10
red_marbles = 5

# First red
P_first_red = red_marbles / total_marbles

# After picking one red (without replacement)
P_second_red = (red_marbles - 1) / (total_marbles - 1)

# Dependent formula
P_dependent = P_first_red * P_second_red

print(f"P(First Red) = {P_first_red}")
print(f"P(Second Red | First Red) = {P_second_red}")
print(f"P(Both Red) = {P_dependent}")
print("Final Answer (Dependent) = 2/9 ≈", round(P_dependent, 4))

print("\n----- SIMULATION (Verification) -----")

trials = 100000
count_both_red = 0

for _ in range(trials):
    marbles = ['R'] * 5 + ['B'] * 5
    pick = random.sample(marbles, 2)

    if pick[0] == 'R' and pick[1] == 'R':
        count_both_red += 1

experimental_probability = count_both_red / trials

print("Experimental Probability (Both Red):", round(experimental_probability, 4))
print("Theoretical Probability:", round(P_dependent, 4))

print("\n----- REFLECTION -----")
print("The denominator changed because we removed one marble.")
print("Without replacement makes the second event dependent on the first.")
print("In NLP, the next word probability depends on the previous word.")
