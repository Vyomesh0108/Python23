# Online Retailer Sells two products "Widgets" and "Gizmos"

# Widget weighs 75 grams
widget_weight = 75

# Gizmos weighs 112 grams
gizmos_weight = 112

# Taking number of widgets order as input from the user
widget1 = int(input("Enter Number of Widgets: "))

# Taking number of widgets order as input from the user
gizmos1 = int(input("Enter Number of Gizmos: "))

# Multiplying the number of Widgets order with a single Widgets weight
total_weight_of_widgets = widget1 * widget_weight

# Multiplying the number of Gizmos order with a single Gizmos weight
total_weight_of_gizmos = gizmos1 * gizmos_weight

# Finding the total order's weight by adding the weight of Widgets and Gizmos
order_total_weight = total_weight_of_widgets + total_weight_of_gizmos

# Printing the total order's weight
print("Total order weight: "+str(order_total_weight)+" grams")
