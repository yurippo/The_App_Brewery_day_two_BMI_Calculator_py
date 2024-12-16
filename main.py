# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:


# bmi is equal to the person's weight divided by the person's height squared.


def main():
     
     height = 1.65 
     weight = 84
     squared_height = height**2

     #print(square)


     bmi = weight / squared_height

     #to improve the code use the round function to round the bmi value up or down depending on the first decimal number
     # and make the code more user friendly

     round_bmi = round(bmi)

     print(round_bmi)
     

if __name__=="__main__":
     main()
