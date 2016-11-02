#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Child-classes of car module."""

import car


class CustomCar(car.Car):
    """A child-class of car.Car."""

    def __init__(self, color='red', tires=None):
        """Constructor for the CustomCar() class.

        Args:
            color (string): The color of the car. Defaults to 'red'.
            tires (list): A list of CustomTire() objects. Defaults to None.
        """
        car.Car.__init__(self, color)
        if tires is None:
            self.tires = []
            list_tires = ['a', 'b', 'c', 'd']
            for each in list_tires:
                each = CustomTire()
                self.tires.append(each)
        else:
            self.tires = tires


class CustomTire(car.Tire):
    """A child-class of car.Tire."""

    def __init__(self, miles=0):
        """Constructor for the CustomTire() class.

        Args:
            miles (int): The number of miles on the CustomTire. Defaults to 0.

        Attributes:
           miles (int): The number of miles on the CustomTire.
           maximum_miles (int): A pseudo-private class attribute. The number of
                                maximum miles of the CustomTire.
        """
        car.Tire.__init__(self, miles)
        self.__maximum_miles = 500
