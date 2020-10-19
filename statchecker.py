import math

def statCheck(stat, baseStat, scale, lvl):
    if (stat == baseStat + math.floor(scale * lvl)):
        return
    else:
        return baseStat + math.floor(scale * lvl)

def healthCheck(hp, base, vitality, tank):
    scale = 3
    if (tank == True):
        scale = 2

    if (hp == base + math.ceil(vitality / scale)):
        return
    else:
        return base + math.ceil(vitality / scale)

# valPer is how much stat you need to gain 1 modifier.
def modCheck(mod, stat, valPer):
    if (mod == math.floor(stat / valPer)):
        return
    else:
        return math.floor(stat / valPer)