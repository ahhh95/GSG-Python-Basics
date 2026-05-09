# Question 1
print("Answer Question 1")
## 1
print("Answer Question 1, section 1")

coffee_cost = 25
coffee_no = 2
cake_cost = 40
cake_no = 1
water_cost = 10
water_no = 3

## 2
print("Answer Question 1, section 2")

total_bill = coffee_cost*coffee_no + cake_cost*cake_no + water_cost*water_no


## 3
print("Answer Question 1, section 3")

print(total_bill)

print(total_bill > 100)

print(total_bill == 120)

## bonus
print("Answer Question 1, Bonus section")

coffee_cost += 5
print(coffee_cost)

print("========================================")
# Question 2
print("Answer Question 2")
customer_points = 40
customer_points += 20
customer_points -= 10
customer_points *= 2

print(customer_points)
print(customer_points >= 100) # True means VIP
print(total_bill > 150 or customer_points >= 100)

print("========================================")
# Question 3
print("Answer Question 3")
## Part A
print("Part A")
result = 10 + 5 * 2 
print(result) # 20
result = (10 + 5) * 2 
print(result) # 30

## Part B
print("Part B")
print(True or False and False) # F
print((True or False) and False) # F

## Part C
print("Part C")
total_bill = 120 
points = 20 
premium_member = True 
print(total_bill > 150 and points > 50 or premium_member) # T
print(total_bill > 150 and (points > 50 or premium_member)) # F

