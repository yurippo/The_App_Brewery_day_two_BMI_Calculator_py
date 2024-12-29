# BMI Calculator
# The body mass index (BMI) is a measure used in medicine to see if someone is underweight or overweight. This is the formula used to calculate it:


# bmi is equal to the person's weight divided by the person's height squared.


def main():
     
     height = float(input("Enter your height in meters: "))
     weight = float(input("Enter your weight in kilograms: "))
     squared_height = float(height**2)

     #print(square)


     bmi = weight / squared_height

     #to improve the code use the round function to round the bmi value up or down depending on the first decimal number
     # and make the code more user friendly

     round_bmi = round(bmi)
     round_bmi_str = str(round_bmi)

     print(f"Your bmi is " + round_bmi_str)

     if bmi < 18.5:
          print("underweight")
    
     elif bmi >= 18.5 and bmi < 25:
          print("normal weight")
     else:
          print("overweight")

     
     

if __name__=="__main__":
     main()
