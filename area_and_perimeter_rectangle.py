#!/usr/bin/env python3

# Created by: Daria Bernice Calitis
# Created on: Sep 2021
# This program calculates the area and perimeter of a rectangle
#    with the radius that the user has given.


def main():
    # This calculates the area and perimeter of the rectangle

    # input
    length = int(input("Enter the length of the rectangle (cm): "))
    width = int(input("Enter the width of the rectangle (cm): "))

    # process
    area_of_rectangle = length * width
    perimeter_of_rectangle = 2 * (length + width)

    # output
    print("The area will be {0} cm²".format(area_of_rectangle))
    print("The perimeter will be {0} cm".format(perimeter_of_rectangle))


if __name__ == "__main__":
    main()
