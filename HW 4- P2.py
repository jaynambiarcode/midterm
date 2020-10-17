def count_frequency(mylist):
    dict = {}
    for n in mylist:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict
mylist=["one", "two","eleven", "one", "three", "two", "eleven", "three", "seven", "eleven"]
print(count_frequency(mylist))