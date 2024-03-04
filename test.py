from lexilang.detector import detect

print(detect("bonjour"))   # ('fr', 0.45)
print(detect("bonjour!"))  # ('fr', 0.45)
print(detect("学中文")) # ('zh', 0.45)
print(detect("ciao mondo")) # ('it', 0.9)
print(detect("El gato doméstico")) # ('es', 0.45)
print(detect("El\"gato\",doméstico")) # ('es', 0.45)
print(detect("ciao", languages=["de", "ro"])) # ('de', 0.45)