num_ic_scoops=(int(input("How many Ice Cream scoops would you like? : ")))
age=int(input(" How old are you?:" ))
discount=.8 #(20% discount results in .8 of the value )
price_per_scoop=1.2

if age  > 65:
    discounted_price=round(((num_ic_scoops) * (price_per_scoop) * (discount)), 2)
    print((str(num_ic_scoops)) + " scoops of ice cream will cost you €" + " " + (str(discounted_price))  + " " + "." +  "This includes a 20% discount for over 65s")

else:
    full_price='{:.2f}'.format(((num_ic_scoops) * (price_per_scoop)))
    print((str(num_ic_scoops)) + " scoops of ice cream will cost you €" + (str(full_price)) + " " + "  ")

