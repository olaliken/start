
print("Welcome so much")
weight=input('what is you weight either in pounds or Kilograms: ')
unit=input("You entered your weight in KG/pounds").lower()
if unit== 'kg':
    print("your are")
    print("Your weight in pounds is")
    print(2.2*int(weight))
elif unit == 'pounds':
    print("Your weight in kilograms is")
    print(int(weight) / 2.2)
else:
    print("ICANT GET YOU WEL")