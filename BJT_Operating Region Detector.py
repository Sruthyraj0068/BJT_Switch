def bjt_operating_region(V_BE, V_CE, I_B, I_C, beta):
  
    # Cutoff Region
    if V_BE < 0.7 or I_B == 0:
        return "Cutoff Region"
    
    # Saturation Region
    elif V_CE < 0.2:
        return "Saturation Region"
    
    # Active Region
    elif I_C == beta * I_B:
        return "Active Region"
    
    else:
        return "Unknown Region"

V_BE = float(input("Enter Base-Emitter Voltage (V_BE) in volts: "))
V_CE = float(input("Enter Collector-Emitter Voltage (V_CE) in volts: "))
I_B = float(input("Enter Base Current (I_B) in amperes: "))
I_C = float(input("Enter Collector Current (I_C) in amperes: "))
beta = float(input("Enter Current Gain (β): "))

region = bjt_operating_region(V_BE, V_CE, I_B, I_C, beta)


print(f"The BJT is in the {region}.")