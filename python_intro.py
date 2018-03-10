divisoria = '-'*50

volume = 80
if volume < 20:
	print('It\s kinda quiet.')
elif 20 <= volume < 40:
	print('It\s nice for a background music.')
elif 40 <= volume < 60:
	print('Perfet, I can hear all the details')
elif 60 <= volume < 80:
	print('Nice for parties')
elif 80 <= volume < 100:
	print('A bit loud!')
else:
	print('My ears are hurting! :(')

print(divisoria)

#funcao para mudar volume do som

def mudarvolume(volume):
	if volume < 20:
		volume = 60
		print('aumentei o som para ' + str(volume))
	elif 80 <= volume < 100:
		print('esta otimo')

mudarvolume(15)

print(divisoria)

def hi(nome):
	print('Hi ' + nome + '!')

garotas = ['Rachel', 'Maria', 'Caroline', 'Marina']
#para cada nome em lista garotas
for nome in garotas:
	hi(nome)
	print('próxima garota')

print(divisoria)

for i in range(1, 6):
	print(i)