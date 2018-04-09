import sys
from collections import OrderedDict


def rating_lister(file_name):
    """Restaurant rating lister."""

    ordered_ratings = {}

    with open(file_name) as ratings:

        for line in ratings:
            rating = line.rstrip().split(':')
            ordered_ratings[rating[0]] = rating[1]

    user_ratings = add_ratings()
    ordered_ratings[user_ratings[0]] = user_ratings[1]

    return OrderedDict(sorted(ordered_ratings.items(), key=lambda t: t[0]))


def add_ratings():
    """ Allows user to rate the restaurant of his/her choice """

    resto_name = raw_input("What restaurant are you rating?\n>> ")

    while True:
        resto_score = raw_input("Please rate your restaurant on a scale of 1 to 5.\n>> ")

        try:
            if int(resto_score) not in range(1, 6):
                print "That score is outside of the 1 to 5 scale."
                continue
            return [resto_name.title(), resto_score]

        except ValueError:
            continue


for restaurant, rating in rating_lister(sys.argv[1]).iteritems():
    print '%s is rated at %s.' % (restaurant, rating)
