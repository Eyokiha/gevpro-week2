#!/usr/bin/env python
# Hennie Veldthuis S2760339

#from PyQt4 import QtCore, QtGui
import sys
    
class Country(): #QtGui.QWidget

    def __init__(self, country):
        self.country = country
        self.__str__()

    def __str__(self):
        self.str_country = " ".join(self.country)
        print("Hello from", self.str_country)

def main(argv):
    if len(sys.argv) > 1:
        country = argv[1:]
        my_country = Country(country)
        #print(my_country.__str__())
    else:
        print("Enter a country name as argv.")

if __name__ == '__main__':
    main(sys.argv)