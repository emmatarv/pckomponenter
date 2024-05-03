from CPU import CPU
from GPU import GPU
from RAM import RAM

komponent1 = CPU("16", "4", "1600mhz", "CPU", "i7", "Intel", 2400)
komponent2 = GPU("12gb", "3600mhz", "4", "GPU", "RTX 3080", "Nvidia", 12000)
komponent3 = RAM("16gb", "1600mhz", "RAM", "Kingston RAM", "Kingston", 1450)
print(komponent1.skrivut())
print(komponent2.skrivut())
print(komponent3.skrivut())
input("")