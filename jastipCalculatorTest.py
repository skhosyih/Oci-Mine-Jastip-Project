# Jastip Calculator

# Initial value of variables
percentageJastipFee = 0
packaging = 0
transportFee = 0
mealFee = 0
result = 0

# The price product amount
priceProduct = 1300000

# print("Enter the price product:")
# priceProduct = input()

# Condition if the price product amount <= 100000, the percentage of jastip fee is 10%
if (priceProduct <= 100000):
    percentageJastipFee = 0.1
    jastipFee = percentageJastipFee * priceProduct
    
    fullTransportFee = 40000
    transportFee = fullTransportFee / 5
    
    fullMealFee = 150000
    mealFee = fullMealFee / 5
    
    result = priceProduct + jastipFee + packaging + transportFee + mealFee

# Condition if the price product amount > 100000, the percentage of jastip fee is 12%
elif (priceProduct > 100000):
    percentageJastipFee = 0.12
    jastipFee = percentageJastipFee * priceProduct
    
    fullTransportFee = 40000
    transportFee = fullTransportFee / 5
    
    fullMealFee = 150000
    mealFee = fullMealFee / 5
    
    result = priceProduct + jastipFee + packaging + transportFee + mealFee

# The result
print("The result is: ", result)
print("Here's the detail:")
print()
print("Price Product: ", priceProduct)
print("Jastip Fee: ", jastipFee)
print("Packaging: ", packaging)
print("Transport Fee: ", transportFee)
print("Meal Fee: ", mealFee)