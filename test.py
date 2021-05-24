ims = {
    '0' : 'images/0.jpg',
    '1' : 'images/1.jpeg',
    }

for k, v in ims.items():
	k = int(k)
	print(type(k))
	print(k)

	print(type(v))
	print(v)
	a = 'aa' + v
	print(a)