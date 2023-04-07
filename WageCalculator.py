# Write a program to calculate and display the gross pay for an hourly paid employee.

# Create the variables here.
hoursWorked = int(0)
payRate = int(0)
wagesEarned = int(0)
taxRate = float(0.070)

# Create the banner
print('*********************************************************************************')
print('This program will calculate and display the gross pay for an hourly paid employee')
print('*********************************************************************************\n')


# Step 1: Get the number of hours worked
hoursWorked = float(input('Please enter the number of hours worked: '))

# Step 2: Get the hourly pay rate
payRate = float(input('Please enter the hourly pay rate: $'))

# Step 3: Multiply the number of hours worked by the hourly pay rate
wagesEarned = hoursWorked * payRate

# Step 4: Display the result of the calculation
# F-Strings ( f ) allow you to use placeholder expressions (wagesEarned) within the string literal.
print(f'Your wages earned before taxes is: ${wagesEarned:,.2f}')

# Step 5: Calculate and display the taxes dedcuted
# To round out to 2 decimal places and add commas for the dollar values, use the comma ( , )
# and the decimal place ( .2f ) format-specifier within the placeholder. EX: {placeholder:format-specifier}
taxesDeducted = wagesEarned * taxRate
print(f'The tax rate is {taxRate:.0%}')
print(f'Your taxes deducted is: ${taxesDeducted:,.2f}')

# Step 6: Deducted taxes from wages earned and display the final wages earned
wagesEarned = wagesEarned - taxesDeducted
print(f'Your wages earned after taxes is ${wagesEarned:,.2f}')

input()
