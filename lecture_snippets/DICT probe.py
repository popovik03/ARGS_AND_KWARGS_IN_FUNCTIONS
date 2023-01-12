# # a = ["Moskva", "Peter", "Penza"]
# a = [["Moskva", 494], ["Piter", 812],  ["Penza", 8412]]
# d = {
#     "Moskva": 495,
#     "Peter": 812,
#     "Penza": 8412
# }
# print(d)
# t=dict(a)
# r = dict(moskva=495, piter = 812, penza = 8412)
# q = dict.fromkeys(["a", 'b', 'c'], 100)
# print(r)
# print(t)
# print(q)
#
# person = {}
# s = "IVANOV IVAN Samara SGU 5 4 5 5 4 3 5"
# s = s.split()
# person["lastName"] = s[0]
# person["firstName"] = s[1]
# person["City"] = s[2]
# person["University"] = s[3]
# person["Grades"] = []
# for i in s[4:]:
#     person["Grades"].append(int(i))
#
#
# print(s)
# print(person)

d = {
    1: "one",
    2: 'two',
    3: "three"
}

print(d)
del d[1]
print(d)
print(len(d))
print(1 in d)
print(3 not in d)
d[4] = "four"
d[5] = "five"
print(d)
for key in d:
    print(key, d[key])
print(d.get(2))
print(d.setdefault(4))
print(d.setdefault(6, "six"))
print(d)
print(d.items())
# for pair in d.items():
#     print(pair)
for key, value in d.items():
    print(key, value)