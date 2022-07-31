import locations_by_data
from pprint import pprint


my_here=locations_by_data.locate("Kingdom Street")
pprint(vars(my_here))

print("\n\n--------------------------------------\n\n")

my_here=locations_by_data.locate("Tavern")
pprint(vars(my_here))

print("\n\n--------------------------------------\n\n")

my_here=locations_by_data.locate("Deep Slime Forest")
pprint(vars(my_here))