#!/usr/bin/python3
"""Defines a base geometry class BaseGeometry."""


class BaseGeometry:
    """Base geometry."""

    def area(self):
        """Empty"""
        raise Exception("area() is not implemented")