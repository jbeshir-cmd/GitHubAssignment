""""JEMAL BESHIR"""
""" Find cities near a specified location. """

from argparse import ArgumentParser
import sys

from haversine import haversine

class Cities:
    """Class to read city data and find nearby cities."""

    def __init__(self, filename):
        """Initialize with city data from the given file.

        Args:
            filename (str): Path to the CSV file containing city data.
                            Each line should have area, city, latitude, and longitude.
        """
        self.cities = {}
        with open(filename, "r", encoding="utf-8") as f:
            for line in f:
                area, city, lat, lon = line.strip().split(",")
                self.cities[(area, city)] = (float(lat), float(lon))

    def nearest(self, point):
        """Return the 5 closest cities to the given point.

        Args:
            point (tuple): A tuple with latitude and longitude as floats.

        Returns:
            list: List of 5 (area, city) tuples representing the closest cities.
        """
        sorted_keys = sorted(
            self.cities.keys(),
            key=lambda city_key: haversine(point, self.cities[city_key])
        )
        return sorted_keys[:5]


def main(filename, arg1, arg2):
    """Main function to find nearest cities.

    Args:
        filename (str): Path to the city data file.
        arg1 (str): Either a latitude value or an area name.
        arg2 (str): Either a longitude value or a city name.

    Side effects:
        Prints the five nearest cities to stdout.
    """
    cities = Cities(filename)

    try:
        lat = float(arg1)
        lon = float(arg2)
        point = (lat, lon)
        label = f"{lat}, {lon}"
    except ValueError:
        key = (arg1, arg2)
        if key not in cities.cities:
            sys.exit(f"Error: {key} not found in {filename}")
        point = cities.cities[key]
        label = f"{arg1}, {arg2}"

    nearest_cities = cities.nearest(point)

    print(f"For {label}, the nearest cities from the file are")
    for area, city in nearest_cities:
        print(f"    {area}, {city}")


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument("filename")
    parser.add_argument("arg1")
    parser.add_argument("arg2")
    args = parser.parse_args()

    main(args.filename, args.arg1, args.arg2)
