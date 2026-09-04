distance = float(input("Distance (km): "))

if distance <= 1.5:
    fare = 25
else:
    fare = 25 + (distance - 1.5) * 12

print(f"Auto Fare: {round(fare, 2)}")