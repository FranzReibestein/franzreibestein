# File: surprise.py

# Below is a dictionary of targets you want to observe.

# If you are an observational astronomer or instrumentalist, picking the correct targets
# to point the telescope at is very important. Let's practice below.

targets = {
    "Vega": {
        "RA": "18h 36m 56.3s",
        "Dec": "+38° 47′ 01″",
        "Magnitude": 0.03,
        "Spectral Type": "A0Va"
    },
    "Betelgeuse": {
        "RA": "05h 55m 10.3s",
        "Dec": "+07° 24′ 25″",
        "Magnitude": 0.42,
        "Spectral Type": "M1-M2 Ia-Ib"
    },
    "Sirius": {
        "RA": "06h 45m 08.9s",
        "Dec": "−16° 42′ 58″",
        "Magnitude": -1.46,
        "Spectral Type": "A1V"
    },
    "Rigel": {
        "RA": "05h 14m 32.3s",
        "Dec": "−08° 12′ 06″",
        "Magnitude": 0.12,
        "Spectral Type": "B8Ia"
    },
    "Polaris": {
        "RA": "02h 31m 49.1s",
        "Dec": "+89° 15′ 51″",
        "Magnitude": 1.97,
        "Spectral Type": "F7Ib"
    }
}

# --- Questions ---
# 1) Write a function that uses a loop to print the name of each star.
def name(n):
    for keys in n:
        print(keys)

# i dont have to call the print function because the name function already includes print commands
name(targets)

# 2) Write a function that uses a loop to print the name of each star with its spectral type.
def name_type(h):
    for star, type in h.items():
        print(f"The Spectral Type of {star} is {type["Spectral Type"]}.") #print the name of the star as wells

name_type(targets)

# 3) Write a function that uses a conditional to find stars with magnitudes greater than 0.1 mag.
def mag(h):
    for star, mag in targets.items():
        if mag["Magnitude"]>0.1:
            print(f"{star} has a magnitude of {mag["Magnitude"]}.")

mag(targets)

# 4) Look up another target, add all the necessary information to the targets list. 
targets["Antares"]={
    "RA": "16 h 29 m 24.5s",
    "Dec": "-26° 25' 55″",
    "Magnitude": 1.06,
    "Spectral Type": "M1.5Iab-Ib"
    }

print(targets)


# 5) Write a function that finds the brightest star whose Declination is closest to 20°.
def bright_twenty(h):
    min_distance = 100 #choose a high distance which will be undercut with a 100 percent chance
    best_star=None
    for star, cat in h.items():
        dec_str= cat["Dec"]
        dec_number = float(dec_str.replace("−", "-").split("°")[0]) #cut the decimal string into two parts and grab the first of the two elements. I also inserted a proper minus sign
        distance=abs(dec_number-20)
        if distance<min_distance:
            best_star=star
    print(f"The brightest star whose declination is closest to 20 is {best_star}. It's magnitude equals {h[best_star]["Magnitude"]}. It's Delination is {h[best_star]["Dec"]}.")
    
bright_twenty(targets)

# 6) What is your favorite constellation?
# I have no favorite constellation because I have no knowledge about constellations.

                

    