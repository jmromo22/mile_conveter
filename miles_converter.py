print("How many kilometers did you cycle today?")
kms = input() #get user input
miles = float(kms)/1.60934 #converting from string to floats then divide
miles = round(miles, 2) #rounds the result
print(f"Your {kms}km ride is equal to {miles} miles")



