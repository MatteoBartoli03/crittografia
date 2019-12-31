messaggio = input("Scrivi il messaggio da criptare formato solamente lettere: ").lower()
chiave = int(input("Scrivi la chiave da utilizzare per criptare il messaggio: "))

if chiave > 26:
	chiave -= 26

cifrato = ""

for lettera in messaggio:

	if lettera != " ":
		code = ord(lettera)
		code += chiave

		if code > 122:
			code -= (122-96)

		cifrato += chr(code)

	else:
		cifrato += " "

print(cifrato)