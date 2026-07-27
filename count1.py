### m05/count1.py

replace_count = 0

def my_replace(s, old, new):
    """Returns a string replacing all instances of old with new.
       Updates global variable replace_count. """
    global replace_count
    i = 0           # tracks where we are in the input string
    j = len(old)    # skip-ahead amount for index calculations
    new_s = s[0:0]  # the new string we're building

    while i < len(s):
        if s[i:i+j] == old:
            replace_count += 1
            new_s = new_s + new
            i += j
        else:
            new_s = new_s + s[i:i+1]
            i += 1

    return new_s


def main():
    my_book = input('What book would you like to read? ')
    print()   # print a blank line

    with open('txts/' + my_book) as my_open_book:
        while True:
            the_line = my_open_book.readline()

            # Having some fun with text substitution
            the_line = my_replace(the_line, 'Cat', '\N{cat face with wry smile}')
            the_line = my_replace(the_line, 'Hat', '\N{top hat}')

            print(the_line, end='')

            # Check for EOF
            if the_line == '':
                break

    print(replace_count, "replacements made")

if __name__ == '__main__':
    main()