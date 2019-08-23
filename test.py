from Canvas import *
from string import *
from math import *


def split_cities(filename):
    city = []
    f = open(filename, "r")
    line = f.readline()
    while line != "":
        line = line[:-1]
        splitlines = line.split()
        city = city + [{"x": int(splitlines[0]),
                        "y": int(splitlines[1]),
                        "name": splitlines[2]}]
        line = line.readline()
    f.close()
    return city


def plot_points(cities):

    x = cities["x"]
    y = cities["y"]
    name = cities["name"]
    create_oval(x-3, y-3, x+3, y+3)
    create_text(x-3, y+3, text=name)


def draw(cities, length):
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
    create_text(100, 120, text="Tour length = %d" % length)


def distance(city1,city2):
    x1 = city1["x"]
    y1 = city1["y"]
    x2 = city2["x"]
    y2 = city2["y"]
    return int(sqrt((x1-x2)*(x1-x2) + (y1-y2)*(y1-y2)))


def nearest_city(cities,i):
    city = cities[i]
    nearest = i +1
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
    length = 0
    i = 0
    while i < len(cities)-1:
        length = length + distance(cities[i], cities[i+1])
        i = i + 1
    length = length + distance(cities[len(cities)-1], cities[0])
    return length


cities = split_cities("Cities.txt")
tour_order(cities)
draw(cities, length_tour(cities))
complete()

