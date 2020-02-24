def append_to_file(fname):
    cars = ["Saloon", "Hatchback", "Estate"]
    with open(fname, "a") as my_file:
        for car_type in cars:
            my_file.write(car_type + "\n")

append_to_file("cars.txt")
