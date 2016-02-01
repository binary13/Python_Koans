#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Triangle Project Code.

# Triangle analyzes the lengths of the sides of a triangle
# (represented by a, b and c) and returns the type of triangle.
#
# It returns:
#   'equilateral'  if all sides are equal
#   'isosceles'    if exactly 2 sides are equal
#   'scalene'      if no sides are equal
#
# The tests for this method can be found in
#   about_triangle_project.py
# and
#   about_triangle_project_2.py
#
def triangle(a, b, c):
    '''
        Determines the number of non-matching sides using len(set()). Then uses dictionary mapping to
        return the type of triangle based on the number of unique side lengths.
    '''

    unique_sides = len({a, b, c})

    type = {
        3: "scalene",
        2: "isosceles",
        1: "equilateral"
    }

    def sides_positive():
        if a>0 and b>0 and c>0:
            return True
        else:
            return False

    def sides_reach():
        if a<b+c and b<a+c and c<a+b:
            return True
        else:
            return False


    if unique_sides in range(1,4) and sides_positive() and sides_reach():
        return type.get(unique_sides)
    else:
        raise TriangleError

# Error class used in part 2.  No need to change this code.
class TriangleError(Exception):
    pass
