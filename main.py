import numpy as np

import filter
import plots
import triangulation as tri

# Recommended filename structure
# Rx_N where x is the number of receiver and N is the measurement number, N>0
# Example: R1_1.txt, R2_1.txt
dir_name = str(input("Directory name to extract measurements from: "))
file_name = str(int(input("Which measurements number to extract values from: ")))

file_names = [dir_name + "/" + "R1_" + file_name + ".txt", dir_name + "/" + "R2_" + file_name + ".txt"]

print("0. No")
print("1. Yes")
receiver_inversion = int(input("Were the receivers faced to eachother (both facing themselves 180 deegree anthena): "))

input_angles = [[], []]

angle_avgs = [[], []]

vert_angle = [[], []]

directory = "raw_values/"

input_angle_ph = "Input angle"

file_err = False

try:
    for i, file_name in enumerate(file_names):
        with open(file_name, 'r') as f:
            for line in f.readlines():
                if input_angle_ph in line and len(input_angles) < 100:
                    input_angle = line.split("Input angle :")[-1].strip()
                    input_angles[i].append(input_angle)
except OSError as e:
    print("File", '"' + file_name + '"', "not found.")
    print("Error:", e.args)
    file_err = True

if not file_err:
    for i, filename in enumerate(file_names):
        print("Input angles: ", input_angles[i])
        directory_receiver = "R" + str(i + 1) + "_" + directory
        with open(directory_receiver + "input_angles.txt", 'w') as f:
            for angle in input_angles[i]:
                f.write(angle)
        print("Raw values have been extracted to directory: ", directory_receiver)

print("Filtering angles...")

int_input_angles = [[], []]
filtered_median_moving_avg = [[], []]

for i, filename in enumerate(file_names):
    int_input_angles[i] = [int(angle) for angle in input_angles[i]]

    filtered_median = filter.median_filter(int_input_angles[i])
    filtered_moving_avg = filter.moving_avg_filter(int_input_angles[i])

    filtered_median_moving_avg[i] = filter.moving_avg_filter(filtered_median)

    directory = "R" + str(i + 1) + "_filtered/"

    with open(directory + "median.txt", 'w') as f:
        for a in filtered_median:
            f.write(f"{int(a)}\n")

    with open(directory + "moving_avg.txt", 'w') as f:
        for a in filtered_moving_avg:
            f.write(f"{int(a)}\n")

    with open(directory + "median_moving_avg.txt", 'w') as f:
        for a in filtered_median_moving_avg[i]:
            f.write(f"{int(a)}\n")

    print("Filtered angles has been written to", directory, "directory.")

print("0. No")
print("1. Yes")
measurement_test_mode = -1
while 0 > measurement_test_mode < 1:
    measurement_test_mode = int(input("Do you want only to save R1 and R2 angles?: "))


if measurement_test_mode == 0:
    dist_x = float(input("Type X coord of Receiver 2 from Receiver 1 perspective in meters [def. is 2]: "))
    dist_y = float(input("Type Y coord of Receiver 2 from Receiver 1 perspective in meters [def. is 0]: "))

    x_arr = []
    y_arr = []

    mode_value_arr = [int_input_angles, filtered_median_moving_avg]

    print("0. Raw data")
    print("1. Filtered data by median, then moving avg")

    data_type_choice = -1
    while 0 > data_type_choice < 1:
        data_type_choice = int(input("Choose mode which data you would like to see: "))

    # Calc pos. of transmitter
    for j in range(len(mode_value_arr[data_type_choice][0])):
        if len(mode_value_arr[data_type_choice][0]) > len(mode_value_arr[data_type_choice][1]):
            mode_value_arr[data_type_choice][0] = mode_value_arr[data_type_choice][::len(mode_value_arr[data_type_choice][1])]
        x, y = tri.calculate_position(mode_value_arr[data_type_choice][0][j], mode_value_arr[data_type_choice][1][j], dist_x, dist_y, receiver_inversion)
        x_arr.append(x)
        y_arr.append(y)

    print("0. Draw approximated point of Transmiter, with two linear functions going from Receivers")
    print("1. Draw approximated points for each pair of Receivers angles")
    print("2. Draw line connecting all approximated points of Receivers angles")
    print("3. Draw all of the above")

    mode_choice = -1
    while 0 > mode_choice < 1:
        mode_choice = int(input("Choose plotting mode: "))

    R1_angle_avg = np.average(mode_value_arr[data_type_choice][0]) # average pos of R1
    R2_angle_avg = np.average(mode_value_arr[data_type_choice][1]) # average pos of R2
    R1_tan, R2_tan = tri.get_tangent(R1_angle_avg, R2_angle_avg, receiver_inversion)
    x, y = tri.calculate_position(R1_angle_avg, R2_angle_avg, dist_x, dist_y, receiver_inversion) # average pos of T1

    if mode_choice == 0:
        plots.draw_linear_functions(R1_tan, R2_tan, dist_x, dist_y, x, y)
        print(f'Approx pos. of transmitter: x = {x:.3f}, y = {y:.3f} in meters')
    elif mode_choice == 1:
        plots.draw_points(x_arr, y_arr, dist_x, dist_y)
    elif mode_choice == 2:
        plots.draw_linear(x_arr, y_arr, dist_x, dist_y)
    elif mode_choice == 3:
        plots.draw_linear_functions(R1_tan, R2_tan, dist_x, dist_y, x, y)
        print(f'Approx pos. of transmitter: x = {x:.3f}, y = {y:.3f} in meters')
        plots.draw_points(x_arr, y_arr, dist_x, dist_y)
        plots.draw_linear(x_arr, y_arr, dist_x, dist_y)


