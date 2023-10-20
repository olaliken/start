print("hello welcome so much to our palace")
cost = input(print("what is the cost of food you taken: "))
disc = input(print("what is the discount percentage of the price: "))
if cost.isdigit() and disc.isdigit():
    cost=int(cost)
    disc=int(disc)
    if float(cost) > 5000:
        disc = (15 / 100) * cost
        print("THE PRIC AFTER DICOUNT IS: ", cost - disc)
        print("WE HAVE GIVEN A DISCOUNT OF: ", disc)
    elif int(cost < 5000):
        disc = 8 / 100 * cost
        print("THE TOTAL PRICE OF FOOD YOU ATE IS", cost - disc)
        print("WE HAVE GIVEN A DISCOUNT OF: ", disc)
else:
        print("i didn't get you well come again")


