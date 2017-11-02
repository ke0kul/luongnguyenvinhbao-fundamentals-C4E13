print("BODY MASS INDEX_PROGRAM")

h = float(input("Enter your height (cm): "))
w = float(input("Enter your weight (kg): "))

h = h/100

BMI = w / (h * h)

if h > 0 and w > 0:
    print("BMI = ", round(BMI, 2))

    if BMI < 16:
        print("Severely underweight!!!!")
    elif BMI < 18.5:
        print("Underweight")
    elif BMI < 25:
        print("Normal")
    elif BMI < 30:
        print("Overweight!!!")
    else:
        print("Obese")
else:
    print("Error, Your height and weight must be > 0!")
