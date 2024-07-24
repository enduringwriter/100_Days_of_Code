# Paint Can Calculator

import math


def paint_calculator(height, width, coverage):
    # print(height, width, coverage)
    area = int(height)*int(width)/int(coverage)
    # print(area)
    cans_of_paint = math.ceil(area)
    # print(cans_of_paint)
    return f"You'll need {cans_of_paint} cans of paint"


print(paint_calculator(2, 4, 5))
