from math import sin, asin, radians, degrees

def find_incidence_angle(n_1, n_2, theta_2):
    n_1 = float(n_1)
    n_2 = float(n_2)
    theta_2_radian = radians(float(theta_2))

    theta_1_radians = asin((n_2 / n_1)*sin(theta_2_radian)) #calculation needs to be in radians
    theta_1 = degrees(theta_1_radians) #convert back to degrees
    return theta_1

n_1 = input("Refractive Index 1: ")
n_2 = input("Refractive Index 2: " )
theta_2 = input("Angle of Refraction: ")
theta_1 = find_incidence_angle(n_1,n_2,theta_2)

print(f"Angle of Incidence is: {theta_1} degrees.")




