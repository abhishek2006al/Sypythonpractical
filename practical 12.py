cord_gateway=(12.2344,13.4567,45, "India gate","Active")
cord_tower=(13.456,15.567,46,"iffle tower","Active")
cord_statue=(34.567,11.234,56,"statu of liberty","Active")

latitude=cord_gateway[0]
longitude=cord_gateway[1]
place=cord_gateway[3]
status=cord_gateway[4]

print("Firat two value:",cord_gateway[0:3])


print("Location Coordinate")
print("Latitude:",latitude)
print("Longitude:",longitude)
print("Place:",place)
print("Status:",status)

new_touple=cord_gateway+cord_tower+cord_statue

print({new_touple})

