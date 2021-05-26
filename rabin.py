# Following program is the python implementation of
# Rabin Karp Algorithm given in CLRS book
#TXT = ABCSAAA
#PAT = ABC

# d is the number of characters in the input alphabet
d = 256

# pat -> pattern
# txt -> text
# q -> A prime number

def search(pat, txt, q): #method for seraching
	M = len(pat) #value of length & pattern
	N = len(txt)
	i = 0
	j = 0
	p = 0 # hash value for pattern
	t = 0 # hash value for txt
	h = 1

	# The value of h would be "pow(d, M-1)%q"
	for i in range(M-1):
		h = (h*d)%q

	# Calculate the hash value of pattern and first window
	# of text
	for i in range(M): #untuk kiraan pertama hash value of the first substring
		p = (d*p + ord(pat[i]))%q #256
		t = (d*t + ord(txt[i]))%q #256

	# Slide the pattern over text one by one until loop habis
	for i in range(N-M+1):
		# Check the hash values of current window of text and
		# pattern if the hash values match then only check
		# for characters on by one
		if p==t:
			# Check for characters one by one
			for j in range(M):
				if txt[i+j] != pat[j]:
					break

			j+=1
			# if p == t and pat[0...M-1] = txt[i, i+1, ...i+M-1]
			if j==M:
				print ("Pattern found at index " + str(i))

		# Calculate hash value for next window of text: Remove
		# leading digit, add trailing digit
		#ABC
		# BCS
		if i < N-M:
			t = (d*(t-ord(txt[i])*h) + ord(txt[i+M]))%q ## basically ---> (d*(t-ord(removed char)*h) + ord(added char))%q [untuk slide window baru]
			#to calculate the value of next has window^^
			#d = 256 the no of char.
			#p is the hash value of pattern. t hash value of text substring
			# We might get negative values of t, converting it to
			# positive
			if t < 0:
				t = t+q

# Driver program to test the above function
txt = "algorithmisfun"
pat = "fun"
q = 101 # A prime number
print("For word : ",pat,"\n")
search(pat,txt,q)

