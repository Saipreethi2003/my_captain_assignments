t = "Hello, Welcome.\ Hi, Welcome."
x = t.capitalize()
print(x)
y = t.casefold()
print(y)
z = t.center(20)
print(z)
a = t.count("Welcome")
print(a)
b = t.encode()
print(b)
c = t.endswith(".")
print(c)
print(t.expandtabs())
d = t.find("Welcome")
print(d)
txt = "For only {price:.2f} dollars!"
print(txt.format(price = 49))
e = t.index("Welcome")
print(e)
f = t.isalnum()
print(f)
g = t.isalpha()
print(g)
h = t.isascii()
print(h)
text = "\u0033"
i = text.isdecimal()
print(i)
abc = "50800"
j = abc.isdigit()
print(j)
txt = "Demo"
k = txt.isidentifier()
print(x)
k = txt.islower()
print(k)
l = txt.isupper()
print(l)
m = abc.isnumeric()
print(m)
greet = "Hello my FRIENDS"
n = greet.lower()
print(n)
o = greet.upper()
print(o)
num = "50"
p = num.zfill(10)
print(p)
txt = "Hello! Are you #1?"
q = txt.isprintable()
print(q)
space = "   "
r = space.isspace()
print(r)
s = t.istitle()
print(s)
names = ("John", "Peter", "Vicky")
t = "#".join(names)
print(t)
col = "pink"
u = col.ljust(20)
print(u, "is my favorite color")
txt = "     mango     "
x = txt.lstrip()
print("of all fruits", x, "is my favorite")
txt = "Hello Sam!"
mytable = txt.maketrans("S", "P")
print(txt.translate(mytable))
v = t.partition("Hi")
print(v)
w = col.replace("pink", "peach")
print(w)
mydict = {83:  80}
print(txt.translate(mydict))
A = t.title()
print(A)
B = txt.swapcase()
print(B)
txt = "     grapes     "
x = txt.strip()
print("of all fruits", x, "is my favorite")
C = t.startswith("Hello")
print(C)
txt = "Thank you for coming\nWelcome to our home"
D = txt.splitlines()
print(D)
txt = "welcome to the jungle"
E = txt.split()
print(E)
F = t.rfind("Hello")
print(F)




