# Write a function that takes camel-cased strings (i.e.
# ThisIsCamelCased), and converts them to snake case (i.e.
# this_is_camel_cased). Modify the function by adding an argument,
# separator, so it will also convert to the kebab case
# (i.e.this-is-camel-case) as well.


def convert_string(txt, seperator):
    txt = list(txt)
    temp = str(txt[0]).lower()
    txt = txt[1:]
    for i in txt:
        if i.isupper():
            ind = txt.index(i)
            txt[ind] = txt[ind].lower()
            txt.insert(ind, seperator)
    txt.insert(0, temp)
    txt = "".join(txt)
    print(txt)


string1 = "ThisIsCamelCased"
convert_string(string1, "_")
convert_string(string1, "-")
convert_string(string1, "+")
