"""

https://py.checkio.org/en/mission/ground-for-the-house/

It was a long trip to the island, so you’ve decided to pass the time sitting in the captain's cabin and splitting the 
treasures remained to be found. Aside from that, a couple of weeks before you left for the expedition, you’ve managed 
to negotiate with several very wealthy people and approximately knew how much you could get by selling the Hypercube.

Purchasing land in a picturesque place have been one of your long-held wishes. You’ve dreamed of building a house there 
and breeding the rare species. All of this requires a considerable amount of money that are likely to come into your 
possession in the near future.
As the input data you will get the multiline string consists of '0' & '#'. where '0' means the empty piece of the ground 
and the '#' is the piece of your house. Your task is to count the minimal area of the rectangle ground which is enough 
for the building."""

def house(plan):
    try:
        house_new = []
        house_edit = plan.splitlines()

        for i in house_edit:
            if len(i) > 0:
                house_new.append(i)

        deliter(house_new)

        house_rotade = list(zip(*house_new[::-1]))
        house_final = []

        for i in house_rotade:
            if len(i) > 0:
                house_final.append(i)

        deliter(house_final)

        return len(house_final) * len(house_final[0])
    except:
        return 0

def deliter(list):
    while not '#' in list[0]:
        list.pop(0)
    while not '#' in list[-1]:
        list.pop(-1)
    return list

if __name__ == '__main__':
    print("Example:")
    print(house('''
0000000
##00##0
######0
##00##0
#0000#0
'''))

    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert house('''
0000000
##00##0
######0
##00##0
#0000#0
''') == 24

    assert house('''0000000000
#000##000#
##########
##000000##
0000000000
''') == 30

    assert house('''0000
0000
#000
''') == 1

    assert house('''0000
0000
''') == 0

    assert house('''
0##0
0000
#00#
''') == 12

    print("Coding complete? Click 'Check' to earn cool rewards!")





