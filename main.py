while True:
  try:
    num = input('Digite um número inteiro de 0 a 999: ')
    if int(num) < 0:
      print('Digite um número inteiro de 0 a 999')
    else:
      break
  except:
    print('Digite um número inteiro de 0 a 999')

