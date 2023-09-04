## Bisection Method using Python.
import math as mth

# Initialize the function 
def bisect(f: int, xl: int, xr: int, minimum_error: int, max_iter: int):
    """Calculating the root of the given function

    Args:
        f (int): The root we're finding
        xl (int): Lower boundary
        xr (int): Higher boundary
        minimum_error (int): Pre-specified tolerance that satisfy the condition
        max_iter (int): Optional

    Returns:
        xm: Return the root of the equation
    """

    # Initalize variables
    i = 1 

    # table header
    print("{:<4} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15} {:<15}".format(
        "i", "xl", "xr", "xm", "f(xl)", "f(xr)", "f(xm)", "Relative Approx Error"
    ))

    # Iterate until the max_iter or the relative approx error is satisfied.
    while i <= max_iter:
        # Calculate the midpoint
        xm = (xl + xr)/2

        # calculate the f(xm) to compare the values
        fxm = f(xm)

        # Calculate the approx errord

        if i > 1:
            ea = abs((xm - x_old) / xm)
        else:
            ea = 100.0 # set it to the high

        # print the current values and then update
        print("{:<4} {:<15.5f} {:<15.5f} {:<15.5f} {:<15.5f} {:<15.5f} {:<15.5f} {:<15.5%}".format(
            i, xl, xr, xm, f(xl), f(xr), fxm, ea
        ))

        if fxm == 0 or ea < minimum_error:
            break


        # Update the boundary
        if f(xl) < 0 and fxm > 0:
            xl = xm
        else:
            xr = xm

        # update the xm
        x_old = xm

        # Increment
        i += 1

    return xm
        


def f(x): #Function that we want to solve
    return mth.sin(5*x) + mth.cos(2*x)


# Determine the root of the equation. F(x) = sin5x + cos2x, with minimum 5% approx error.
# Interval of [-0.525, -0.51875]

xl = -0.525
xr = -0.51875
minimum_error = 0.05
max_iter = 50

root = bisect(f, xl, xr, minimum_error, max_iter)

print(f"The root is: {root:.5f}")
