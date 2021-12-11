
ti = int(input("How many players "))
ch = ["Bloodhound", "Gibraltar", "Lifeline", "Pathfinder", "Wraith", "Bangalore", "Caustic", "Mirage",
    "Octane", "Wattson", "Crypto", "Revenant", "Loba", "Rampart", "Horizon", "Fuse", "Valkyrie", "Seer", "Ash"]
chs = random.sample(ch, ti)

for i in chs:   
    print(i)   
