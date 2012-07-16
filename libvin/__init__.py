"""
Copyright Lukasz Szybalski
VIN Vehicle information number checker,
Inputs vin number and outputs true/false 
"""
def check_vin(vin):
    """Vehicle Information Number. This will return whether the entered vin number is authentic/correct.
    Example:
    import vin
    vin.check_vin(my_vin_number)
    """
    vin=str(vin).strip()
    if len(vin) != 17:
        return False
    else:
        converted=[]
        vin=vin.upper()
        for i in range(len(vin)):
            converted.insert(i,convert_vin(vin[i]))
        multiplier=[8,7,6,5,4,3,2,10,0,9,8,7,6,5,4,3,2]
        add=0
        for i in range(len(vin)):
            add+=(converted[i]*multiplier[i])
        final= (add%11)
        if final ==10:
            final='x'
        if str(final)==vin[8]:
            return True
        else:
            return False
        

def convert_vin(field):
    """Stores alpha to number conversion as defined by the vehicle information number standard.
    """
    if not field.isalpha():
        return int(field)
    else:
        if field == "A":
            return 1
        elif field=="B":
            return 2    
        elif field=="C":
            return 3    
        elif field=="D":
            return 4    
        elif field=="E":
            return 5    
        elif field=="F":
            return 6    
        elif field=="G":
            return 7    
        elif field=="H":
            return 8    
        elif field=="I":
            return 9    
        elif field=="J":
            return 1    
        elif field=="K":
            return 2    
        elif field=="L":
            return 3    
        elif field=="M":
            return 4    
        elif field=="N":
            return 5    
        elif field=="O":
            return 6    
        elif field=="P":
            return 7    
        elif field=="Q":
            return 8    
        elif field=="R":
            return 9    
        elif field=="S":
            return 2    
        elif field=="T":
            return 3    
        elif field=="U":
            return 4    
        elif field=="V":
            return 5    
        elif field=="W":
            return 6    
        elif field=="X":
            return 7    
        elif field=="Y":
            return 8    
        elif field=="Z":
            return 9
        else:
            return False
    
