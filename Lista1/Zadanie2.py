isDay = False
isRaining = False
isFog = True

brightness = 0

if isDay and not isRaining and not isFog:
    brightness = 50
elif isDay and (isRaining or isFog):
    brightness = 70
elif not isDay and not isRaining and not isFog:
    brightness = 90
elif not isDay and (isRaining or isFog):
    brightness = 100

print(brightness)