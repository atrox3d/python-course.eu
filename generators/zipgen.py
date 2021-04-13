#!/usr/bin/env python3

def zipgen():
	count=0
	while True:
		try:
			if count % 2 == 0:
				char = "first"[count]
				#yield "second"[count]
			else:
				char = "second"[count]
				#yield "first"[count]
			
			print("count : %d, yield : %s" % (count, char))
			yield char
		except:
			return
		count += 1

if __name__ == "__main__":
	out = ""
	for char in zipgen():
		out = out + char
	print(out)
