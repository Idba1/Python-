def full_name(f_name, l_name):
    name = f"{f_name} {l_name}"
    return name


name = full_name(l_name="chowdhury", f_name="Selim")
# print(name)


def long_name(**kargs):
    print(kargs)


long_name(f="Dr. ", m="Phitron", l="practice")


def mixed_name(first, last, **name_parts):
    print(first, last, name_parts)


mixed_name(first="Dr. ", m="Phitron", last="practice", ll="last last")


def all_types(middle, *args, **kargs):
    print(middle)
    print(args)
    for w in args:
        print(w)
    print(kargs)
    for key,value in kargs.items():
        print(key,value)


all_types("shd", "asf", "dfasd", l="jsdjj", ll="shdj")
