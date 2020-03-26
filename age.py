from time import *


# a function to find your age
def age():
    print("Enter Your Date of Birth")
    d = input("Day:")
    m = input("Month:")
    y = input("Year:")
    # get the current time in tuple format
    a = gmtime()
    # difference in day
    dd = a[2] - int(d)
    # difference in month
    dm = a[1] - int(m)
    # difference in year
    dy = a[0] - int(y)
    # checks if difference in day is negative
    if dd < 0:
        dd = dd + 30
        dm = dm - 1
        # checks if difference in month is negative when difference in day is also negative
        if dm < 0:
            dm = dm + 12
            dy = dy - 1
    # checks if difference in month is negative when difference in day is positive
    if dm < 0:
        dm = dm + 12
        dy = dy - 1
    print("你现在的年龄 %s 岁 %s 月 %s 天" % (dy, dm, dd))

if __name__ == '__main__':

    age()


