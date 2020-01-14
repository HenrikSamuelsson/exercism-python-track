def convert(number) -> str:
    # Start with an empty string for the rain drop sound
    rain_drop_sound = ""

    # Possibly add sounds based on divisibility of the input number
    if number % 3 == 0:
        rain_drop_sound += "Pling"
    if number % 5 == 0:
        rain_drop_sound += "Plang"
    if number % 7 == 0:
        rain_drop_sound += "Plong"

    # Shall return the number itself if it does not produce any sound
    if rain_drop_sound == "":
        rain_drop_sound = str(number)

    return rain_drop_sound
