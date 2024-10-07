def add(x,y):
    z=x+y
    return z

print(add(78,36))


def sub(w,q):
    r=q-w
    return r
print(sub(78,98))



def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first + " " + last

full_name=create_name("nick","bob")

print(full_name)
