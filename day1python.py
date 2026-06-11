def main():
    name=input("enter your name ")
    age=int(input("enter your age "))
    Weight=int(input("enter your Weight in kg "))
    height=float(input("enter your height in meter "))
    print(f"""
          Ms.{name} the BMI= {BMI(Weight,height)} and the BMR= {BMR(Weight,height,age)} kcal/day
          BMI (Body Mass Index): A number that estimates whether your weight is healthy for your height.
          BMR (Basal Metabolic Rate): The number of calories your body needs each day to keep you alive while resting.
          """)

def BMI(w,h):
    return w/(h*h)

def BMR(we,he,age):
    return (we*10)+(he*100*6.25)-(age*5)-161

main()