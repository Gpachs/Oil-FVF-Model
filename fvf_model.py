""" Calculation of Total Oil Formation Volume Factor, (Bt) at 2000 (psia) Using
    Glaso's  Correlations and solving for volume of oil in place
    PVT Data:
    temp = 600
    gas_gravity = 0.6744
    gas_solub = 444
    oil_gravity = 0.843
    pressure = 2000 psia at bubble point, 800 psia below point presure
    fvf = 1.1752
    VOIP Data:
    area = 200
    height = 100
    porosity = 0.25
    saturation = 0.2
"""
import math

print("CALCULATION OF TOTAL FORMATION VOLUME FACTOR USING GLASO'S METHOD")
print(" ")
temp = int(input("Enter Temperature Value in Rankine: "))
if temp < 0:
    print("Error! Temperature value should be a positive integer value.")
gas_gravity = float(input("Enter Gas gravity Value: "))
if gas_gravity < 0:
    print("Error! Gas gravity should be a floating number greater than zero.")
gas_solub = int(input("Enter gas solubility in scf/STB: "))
if gas_solub < 0:
    print("Error! Gas solubility should be an integer  value greater than zero.")
oil_gravity = float(input("Enter oil gravity value in 60°/60°: "))
if oil_gravity < 0:
    print("Error! Oil gravity value should be a number greater than zero.")

pressure = int(input("Enter Pressure value in psia: "))
if pressure < 0:
    print("Error! Bubble point pressure is an integer greater than zero")

fvf = float(input("Enter value for oil FVF in bbl/STB: "))
if fvf < 0:
    print("Error! try again.")
area = int(input("enter the value of area in acres: "))
height = int(input("enter the value of height in ft: "))
porosity = float(input("enter the value of porosity: "))
satrn = float(input("enter the value of oil saturation: "))


def fvf_total():
    """ This function calculates the total formation volume factor """

    exponent_c = 2.9 * 10 ** (-0.00027 * gas_solub)

    A_star = ((gas_solub * (temp - 460) ** 0.5 * (oil_gravity) ** exponent_c) / 0.6744 ** 0.3) * pressure ** (-1.1089)

    # applying Glaso's formula for B_total
    fvf_t = 0.080135 + 0.47257 * math.log10(A_star) + 0.17351 * (math.log10(A_star)) ** 2
    fvf_final = 10 ** fvf_t
    print("----------RESULTS------------")
    print(" ")
    print("The exponent C is given as => ", "%.2f" % exponent_c)
    print(" ")
    print("standing's correlating parameter A* => ", "%.4f" % A_star)
    print(" ")
    return fvf_final


print("The Total Oil Formation Volume factor @2000 psia Bubble Point pressure is =>", "%.4f" % fvf_total(), "bbl/stb")

# solving volume of oil initially in place using the value of B_total
b_total = fvf_total()
vo = 43560*area*height*porosity*(1-satrn)/b_total
print("the volume of oil in place is =>", vo, "bbl")
