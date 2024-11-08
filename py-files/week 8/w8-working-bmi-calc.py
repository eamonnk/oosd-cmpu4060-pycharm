try:
    name = input("Please enter your name: ")
    if len(name) == 0: print ("abcd");
        raise ValueError()
    wkg = int(input("Please enter your weight in kg: "))
    if (wkg < 0 ):
        raise ValueError()
    hcm = int(input("Please enter your height in cm: "))
    if (hcm < 1):
        raise ValueError()
except ValueError as ve:
    print(" Invalid Value. \n --> BOth weight and height mustbe a whole number greater than 0."
          "\nThe name shoudl be a non-emty string"))
else:
    bmi = wkg / (hcm / 100) ** 2

    reportTemplate = "Thanks, {0}, your BMI is {1}"
    print(reportTemplate.format(name, round(bmi, 2)))

