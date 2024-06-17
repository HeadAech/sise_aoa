import math


def get_tangent(ang1_deg, ang2_deg, inversion):
    # Deg to Rad
    # Jeśli inversion == 1, odwróć kąt ang2_deg o 180 stopni
    if inversion == 1:
        ang1_deg = (ang1_deg - 270) % 360
    else:
        ang1_deg = (ang1_deg - 90) % 360
    ang2_deg = (ang2_deg - 90) % 360
    # Zamiana stopni na radiany
    ang1_rad = math.radians(ang1_deg)
    ang2_rad = math.radians(ang2_deg)

    # Obliczenie tangensów kątów
    tan1 = math.tan(ang1_rad)
    tan2 = math.tan(ang2_rad)

    return tan1, tan2


def calculate_position(ang1_deg, ang2_deg, x_dist, y_dist, receiver_inversion):
    tan1, tan2 = get_tangent(ang1_deg, ang2_deg, receiver_inversion)

    # Coords of transmitter /choose one of the functions to calculate y cord
    if tan1 - tan2 != 0:
        x_cord = ((-x_dist * tan2) + y_dist) / (tan1 - tan2)
    else:
        x_cord = ((-x_dist * tan2) + y_dist) / 0.00001
    y_cord = tan1 * x_cord

    return x_cord, y_cord
