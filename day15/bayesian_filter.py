print("----- GIVEN DATA -----")

P_spam = 0.10              # 10% emails are spam
P_ham = 1 - P_spam         # 90% emails are not spam

P_free_given_spam = 0.90   # 90% of spam contains "Free"
P_free_given_ham = 0.05    # 5% of ham contains "Free"

print("P(Spam) =", P_spam)
print("P(Ham) =", P_ham)
print("P(Free | Spam) =", P_free_given_spam)
print("P(Free | Ham) =", P_free_given_ham)

# Law of Total Probability
P_free = (P_free_given_spam * P_spam) + \
         (P_free_given_ham * P_ham)

print("\n----- TOTAL PROBABILITY -----")
print("P(Free) =", round(P_free, 4))

P_spam_given_free = (P_free_given_spam * P_spam) / P_free

print("\n----- BAYES' THEOREM RESULT -----")
print("P(Spam | Free) =", round(P_spam_given_free, 4))

print("\n----- INTERPRETATION -----")
print("Even though only 10% of emails are Spam,")
print("if an email contains the word 'Free',")
print("the probability it is Spam increases significantly.")
print("Final Answer ≈", round(P_spam_given_free * 100, 2), "%")

import random

print("\n----- SIMULATION (Verification) -----")

trials = 100000
spam_and_free = 0
free_total = 0

for _ in range(trials):
    # Step 1: Decide if email is spam
    is_spam = random.random() < P_spam
    
    if is_spam:
        contains_free = random.random() < P_free_given_spam
    else:
        contains_free = random.random() < P_free_given_ham

    if contains_free:
        free_total += 1
        if is_spam:
            spam_and_free += 1

experimental_probability = spam_and_free / free_total

print("Experimental P(Spam | Free) =", round(experimental_probability, 4))
print("Theoretical P(Spam | Free) =", round(P_spam_given_free, 4))

print("\n----- REFLECTION -----")
print("This is exactly how Naive Bayes works.")
print("We update prior belief using evidence.")
print("Posterior = (Likelihood × Prior) / Evidence")
