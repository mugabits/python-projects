__author__ = 'jmugz3'


def digit_sum(n):

    x =0


    while n:

        x += n % 10
        n /= 10
    return x



digit_sum(1234)