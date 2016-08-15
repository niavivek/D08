f = dict(A=1,B=2,C=3)


def reverse_lookup(d, value):
	key_keys = []
	for key in d:
		if d[key] == value:
			key_keys.append(key)
	return key_keys

print(reverse_lookup(f,2))
print(f)