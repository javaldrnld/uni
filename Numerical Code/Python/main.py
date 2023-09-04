import pandas as pd


# Problem Set #2: Find the root using the bisection method. Find Relative True Error
# with interval of [2.5, 3.5]. With 𝜺t(%) of 1%


def func(x: int) -> int:
    return x**2 - 7

def bisect(func: int, xl: int, xr: int, mini_error: int) -> int:
    
    # Initialize variable of vt, and iteration
    vt = 2.64575
    i = 1

    df  = pd.DataFrame(columns=['xl', 'xr', 'xm', 'f(xl)', 'f(xr)', 'f(xm)', 'ɛt(%)'])

    while True:
        # Update the values
        xm = (xl + xr)/2
        fxm = func(xm)

        if i == 1:
            et = abs((vt-xm)/vt)*100
        else:
            et = 100

        # round to 5 decimal
        non_rounded = [xl, xr, xm, func(xl), func(xr), fxm, et]
        rounded = [round(num, 5) for num in non_rounded]
        # append to the table
        df.loc[i] = rounded

        if et < mini_error:
            break

        # Update the boundary
        if func(xl) < 0 and fxm > 0:
            xl = xm
        else:
            xr = xm

        i += 1

    return df

table = bisect(func, xl=2.5, xr=3.5, mini_error=1)
print(table)

