

class a:

    name="a"
    def eat(self):
        return "吃"
    def run(self):
        return "走"

aa=a()
aaa=a.eat(a)
print(aaa)
print(dir(a))
print(aa.name)
print(type(aa.name))