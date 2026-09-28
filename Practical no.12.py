print("Location Coordinate Processing System\n")

locations = (
    ("Gateway of India", 18.9220, 72.8347),
    ("Tajmahal", 18.5196, 73.8553),
    ("India Gate", 28.6129, 77.2295)
)

print("Number of locations:", len(locations))

print("\nIndex of each location:")

for i in range(len(locations)):
    print(i, "->", locations[i][0])


gateway = locations[0]

print("\nGateway of India index:")
print(locations.index(gateway))

print("\nCount of Gateway of India:")
print(locations.count(gateway))

print("\nCheck if Gateway of India exists:")

if gateway in locations:
    print("Gateway of India is present.")
else:
    print("Gateway of India is not present.")


coordinate = (18.9220, 72.8347)

found = False

for location in locations:
    if (location[1], location[2]) == coordinate:
        found = True
        print("\nCoordinate found:", location[0])
        break

if not found:
    print("\nCoordinate not found.")

print("\nAll GPS Locations:")

for location in locations:
    name, latitude, longitude = location

    print(
        f"{name}: "
        f"Latitude = {latitude}, "
        f"Longitude = {longitude}"
    )