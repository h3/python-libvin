"""
Copyright Lukasz Szybalski
VIN Vehicle information number checker,
Inputs vin number and outputs true/false 
"""

def is_valid(vin):
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


