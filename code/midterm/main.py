from room_sensor import RoomSensor
rooms = [RoomSensor("Kitchen", 28, 72, 220), RoomSensor("Bedroom", 22, 50, 190), RoomSensor("Balcony", 30, 70, 250)]
for room in rooms:
    room.show_info()
    print("Comport Level:", room.comfort_level())
    print("Light Status:", room.light_status())
    print("")

Comfortable = 0
Warning = 0
Nomal = 0

for room in rooms:
    stauts = room.comfort_level()
    if stauts == "Comfortable":
        Comfortable += 1
    elif stauts == "Warning":
        Warning += 1
    elif stauts == "Nomal":
        Nomal += 1

print("Comfortable:", Comfortable)
print("Normal:", Nomal)
print("Warning:", Warning)
    