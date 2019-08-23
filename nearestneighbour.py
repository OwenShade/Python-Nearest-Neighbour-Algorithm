from Canvas import *
from math import *


def split_cities(filename):
    # Reading in a file and parsing the data before storing each specific part of the data in a list of dictionaries.
    city = []
    f = open(filename, "r")
    line = f.readline()
    while line != "":
        line = line[:-1]
        splitlines = line.split()
        city = city + [{"x": int(splitlines[0]),
                        "y": int(splitlines[1]),
                        "name": splitlines[2]}]
        line = f.readline()
    f.close()
    return city


def draw(cities, length):
    # Iterating through each city in the array and finding the corresponding x and y co-ordinate
    # The co-ordinates are past as a parameter to the plot points function which draws a point for the city
    # Then a line is created from the city just drawn to the next city in the array in order to show the path taken.
    city = cities[0]
    plot_points(city)
    x = city["x"]
    y = city["y"]
    i = 1
    while i < len(cities):
        city1 = cities[i]
        plot_points(city1)
        x1 = city1["x"]
        y1 = city1["y"]
        create_line(x, y, x1, y1)
        x = x1
        y = y1
        i = i + 1
    city1 = cities[0]
    x1 = city1["x"]
    y1 = city1["y"]
    create_line(x, y, x1, y1)
    create_text(200, 220, text="Tour length = %d" % length)


def plot_points(city):
    # Defining how to plot a point for cities on a canvas.
    x = city["x"]
    y = city["y"]
    name = city["name"]
    create_oval(x-3, y-3, x+3, y+3)
    create_text(x-3, y+3, text=name)


def nearest_city(cities, i):
    # Algorithm to find the next nearest city
    # Like a min/max algorithm, iterates through all remaining cities comparing one to the next and storing the nearest.
    city = cities[i]
    nearest = i + 1
    d = distance(city, cities[i+1])
    i = i + 1
    while i < len(cities) - 1:
        newd = distance(city, cities[i+1])
        if newd < d:
            d = newd
            nearest = i + 1
        i = i + 1
    return nearest


def tour_order(cities):
    i = 0
    while i < len(cities) - 2:
        second = nearest_city(cities, i)
        temp = cities[i+1]
        cities[i+1] = cities[second]
        cities[second] = temp
        i = i + 1


def length_tour(cities):
    # Iterating through each city to calculate the total length of the tour
    # Calling the function distance inside this function to do so.
    length = 0
    i = 0
    while i < len(cities)-1:
        length = length + distance(cities[i], cities[i+1])
        i = i + 1
    length = length + distance(cities[len(cities)-1], cities[0])
    return length


def distance(city1, city2):
    # Calculating the distance between two cities
    x1 = city1["x"]
    y1 = city1["y"]
    x2 = city2["x"]
    y2 = city2["y"]
    return int(sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))


cities = split_cities("Cities.txt")
tour_order(cities)
draw(cities, length_tour(cities))
complete()

