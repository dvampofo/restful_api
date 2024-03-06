friends = {"bob", "rolf", "anne"}
abroad = {"bob", "anne"}

local_friends = friends.difference(abroad)
print(local_friends)

art = {"bob", "jen", "rolf", "charlie"}
science = {'bob', "jen", "adam", "anne"}
both = art.intersection(science)
print(both)