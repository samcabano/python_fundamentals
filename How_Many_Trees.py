# Calculates and displays number of trees in Sacramento

unitSqFt = 800 # 800 square ft sample
treesPerUnit = 1 # 1 tree per 800 square ft on Google Maps
sacSqMiles =  100 # 100 square mi in Sacramento
treesPerSqFt = treesPerUnit / unitSqFt # Calculates trees per square ft
treesPerSqMile = treesPerSqFt * 27878400 # Calculates trees per square mi
treesInSac = int(treesPerSqMile * sacSqMiles) # Calculates trees in 100 square miles
print ("Average number of trees in Sacramento:", format(treesInSac,",d")) # Displays answer
