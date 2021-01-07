import time
			
print('Всратий калькулятор')
print()

while True:	
	while True:
		try:
			a = float(input('Давай перше число: '))
			break
		except ValueError:
			print('Ти або числа вводиш, або валиш звідси. Understand?')
			print()
			
	while True:
		try:
			b = float(input('Давай друге: '))
			break
		except ValueError:
			print('До тебе не доходе бачу. ЧИСЛА, алло!')
			print()

	while True:
		what = input('Шо робим? Вибирай +, -, *,/: ')
		if what == '+':
			print('Вичисляю...')
			time.sleep(2)
			c = a + b
			print('Вроді так: ' + str(c))
			break
		elif what == '-':
			print('Думаю...')
			time.sleep(2)
			c = a - b
			print('А ось і відповідь: ' + str(c))
			break
		elif what == '*':
			print('Ща...')
			time.sleep(2)
			c = a * b
			print('Єслі шо, я не приділах: ' + str(c))
			break
		elif what == '/':
			print('Ммм...зараз...')
			time.sleep(2)
			if b == 0:
				try:
					c = a / b
				except ZeroDivisionError:
					print('Ти з якої планети? На 0 ділити не можна.')
			else:
				c = a / b
				print('Вот: ' + str(c))
			break
		else:
			print('Нє, ну ти валянок? Сказано: вибери один з чотирьох варіантів, не більше, не менше.')
			print()
		
	print()
	ans = input('Продолжаєм?\n да +, нє -: ')
	if ans == '+':
		print()
	elif ans == '-':
		break
	else:
		ans1 = input('OMG, хіба так тяжко? Або +, або -, вибери. Будь ласка: ')
		print()
		if ans1 == '+':
			print()
		elif ans1 == '-':
			break
		else:
			print('Ой, та нахрін все!')
			break