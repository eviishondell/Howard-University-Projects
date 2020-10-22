def getPhase(t, p):
    if p < 611.66:
        if t < 200:
            return "Solid"
        elif t == 200:
            return "Solid/Vapor"
        else:
            return "Vapor"
         
    if p == 611.66:
        if t < 200:
            return "Solid"
        elif t < 273.16:
            return "Solid/Vapor"
        elif t == 273.16:
            return "Solid/Liquid/Vapor"
        elif t <= 373.15:
            return "Liquid/Vapor"
        else:
            return "Vapor" 
            
    if p == 101330:
        if t >= 373.15:
            return "Liquid/Vapor"
        elif t == 273.16:
            return "Solid/Liquid"
        elif t > 273.16:
            return "Liquid"
        else:
            return "Solid"
            
    if p < 101330:
        if t < 273.16:
            return "Solid"
        elif t == 273.16:
            return "Solid/Liquid"
        elif t < 373.15:
            return "Liquid"
        elif t == 373.17:
            return "Liquid/Vapor"
        else:
            return "Vapor"
    else:
        if t < 273.16:
            return "Solid"
        elif t == 273.16:
            return "Solid/Liquid"
        else:
            return "Liquid"
            
            
            
