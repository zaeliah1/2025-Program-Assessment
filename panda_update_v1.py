import pandas
import numpy

# lists to hold ticket details
all_meats = ["Beef", "Chicken", "Lamb", "Venison", "Fish", "Turkey",
             "Duck", "Pork", "Lobster", "Mutton"]
all_meat_costs = [19, 13.60, 18, 25, 16.60, 21.20, 48.50, 14 , 100, 14]

meat_dict = {
    'Name': all_meats,
    'Meat Price': all_meat_costs,
}

# create dataframe / table from dictionary
meat_frame = pandas.DataFrame(meat_dict)

# Rearranging index
meat_frame.index = numpy.arange(1, len(meat_frame) + 1)

print(meat_frame)
print()


