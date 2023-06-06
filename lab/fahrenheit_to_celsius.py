#!/usr/bin/env python3

# question
IN = float(input("What temperature (in Fahrenheit) would you like converted to Celsius? "))

# calculation
OUT = round(
        ((IN - 32)*5) / 9
        , 2
      )

# output of converted values
print(str(IN) + " F is " + str(OUT) + " C")
