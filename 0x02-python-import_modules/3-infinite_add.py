#!/usr/bin/python3

if __name__ == "__main__":
    """Print the addition of all arguments."""
    import sys

    ad = 0
    for x in sys.argv:
        if x != sys.argv[0]:
            ad += int(x)
    print(ad)
