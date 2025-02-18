import numpy as np
import matplotlib.pyplot as plt

def bjt_switch(v_be):
    threshold_voltage = 0.7
    return "ON" if v_be >= threshold_voltage else "OFF"

v_be_range = np.linspace(0, 1, 100)
states = []
for v_be in v_be_range:
    state = bjt_switch(v_be)
    states.append(state)

#print(states)  

plt.figure(figsize=(8, 5))
plt.plot(v_be_range, states, label="BJT State", color="blue")
plt.axvline(x=0.7, color="red", linestyle="--", label="Threshold (0.7V)")
plt.title("BJT Switch Simulation (ON/OFF)")
plt.xlabel("Base-Emitter Voltage (V_BE)")
plt.ylabel("Transistor State")
plt.yticks(["OFF", "ON"])
plt.legend()
plt.grid(True)
plt.show()
