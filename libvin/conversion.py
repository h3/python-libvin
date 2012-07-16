"""
Copyright Lukasz Szybalski
VIN Vehicle information number checker,
"""

def convert(field):
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
    

