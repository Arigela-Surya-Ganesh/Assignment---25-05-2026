#6.Perimeter of Triangle
#Question: Calculate the perimeter of a triangle. - 
#Formula: Perimeter = side1 + side2 + side3 - Input: - Side1 = 5, Side2 = 6, Side3 = 7 - Output: - Perimeter of triangle is: 18
side1 = 5
side2 = 6
side3 = 7
perimeter = side1 + side2 + side3
print("perimeter of Triangle : " + str(perimeter))


#7. Break Amount into 1000s, 500s, and Remaining Change
#Question: Break the total amount into denominations. - Input: - Amount = 3700 - Output: - 1000s: 3 - 500s: 1 - Remaining: 200
#amount = 3700
amount = 3700
a = amount//1000
print("1000s : " + str(a))

b = amount - (a*1000)
#print(b)
c = b//500
print("500s : " + str(c))

d = b - c*500
print("Remaining : " + str(d))

#8. Convert Seconds into Hours, Minutes, and Seconds
#Question: Convert total seconds into hours, minutes, and seconds. - Input: - Total seconds = 3672 - Output: - Hours: 1 - Minutes: 1 - Seconds: 12
total_seconds = 3672
hours = 3672//3600
print("Hours : " + str(hours))

minutes = hours//60
print("Minutes : " + str(minutes))

total_seconds = 3672

# Calculate hours
hours = total_seconds // 3600

# Remaining seconds after hours
remaining_seconds = total_seconds % 3600

# Calculate minutes
minutes = remaining_seconds // 60

# Remaining seconds after minutes
seconds = remaining_seconds % 60

print("Hours:",  hours)
print("Minutes:", minutes)
print("Seconds:", seconds)


#9. Sum of Marks (Maths, Physics, Chemistry)
#Question: Calculate the sum of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Total marks: 263
maths = 85
physics = 90
chemistry = 88
total_Marks = maths + physics + chemistry
print("Total Marks : " + str(total_Marks))

#10. Average of Marks (Maths, Physics, Chemistry)
#Question: Calculate the average of marks in 3 subjects. - Input: - Maths = 85 - Physics = 90 - Chemistry = 88 - Output: - Average marks: 87.67
maths = 85
physics = 90
chemistry = 88

Average = (maths + physics + chemistry)/3
print("Average marks : " + str(Average))