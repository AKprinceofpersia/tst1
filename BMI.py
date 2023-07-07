import math
print("be barname mohasebe bmi khosh omadid")
height=int(input("ghad shoma(be santimetr): "))
weight=int(input("vazn shoma(be kilogeram): "))
Bmi=int(weight/((height*height)/(100*100)))
if Bmi<18.5:
    print("your Bmi: ",Bmi," (underweight)")
if Bmi>=18.5 and Bmi<25:
    print("your Bmi: ",Bmi," (normal)")
if Bmi>=25 and Bmi<30:
    print("your Bmi: ",Bmi," (overweight)")
if Bmi>=30 and Bmi<35:
    print("your Bmi: ",Bmi," (obese)")
if 35<=Bmi:
    print("your Bmi: ",Bmi," (exteremly obese)")