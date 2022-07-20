# FIRSTLY INSTALL THE REQUIRED PACKAGES USING THE COMMANDS GIVEN BELOW
# pip install bs4

from geoNews import fetchGeoNews
from aryNews import fetchAryNews


def main():
    fetchGeoNews()
    fetchAryNews()


main()
