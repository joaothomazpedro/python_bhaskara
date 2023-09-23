import math

# Values for function     
# Feel free to adapt the value of cofficients 
a, b, c = 12, 20, 2

# Delta Function/Lambda
delta = lambda a, b, c: pow(b, 2) - (4 * a * c)

# Delta Value ready for use!
delta_value = (abs(delta(a, b, c)))

# Delta's root
delta_root = math.sqrt(round(delta_value, 3))

# Bhaskara calculation
bhaskara_pos = 0 
bhaskara_neg = 0

if delta_root > 0:
    bhaskara_pos = (-b + delta_root) / (2 * a)
    bhaskara_neg = (-b - delta_root) / (2 * a)
    print(f"Positive Equation: {round(bhaskara_pos,3)}\n"
          f"Negative Equation: {round(bhaskara_neg, 3)}")
    
elif delta_root == 0:
    bhaskara_neg = (-b) / (2 * a)
    print(f"Delta 0 Equation: {round(bhaskara_neg, 3)}")
    
elif delta_root < 0:
    print("This equation doesn't exists")