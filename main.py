password = '1313'
saldo = 10000
x = input("Ingrese su usuario: ")
p = input("Ingrese su contraseña: ") #Se solicita al usuario un usuario y contraseña
if p == password: 
  print ('\n','\n','\n','\t'
 "         Bienvenido",x.upper(),'\n','\n')
  print ("Que operación desea realizar:",'\n','\n'"[r] Retirar",'\n'"[v] Ver saldo",) # Si la contraseña es correcta, el algoritmo dejara ingresar al menu 
  s = input('\n'"Seleccione una opción: ")
  r = ("Retirar")
  v = ("Ver saldo") # Al momento de ingresar el programa mostrara el menu
  if s == 'v':
    print ('\n'"*Saldo disponible: ",saldo) # Si el usuario selleciona s el programa mostrara las opciones
  else:
    s == 'r' # Si el usuario selecciona r el programa dejara mostrara el saldo 
    print ('\n'"Seleccione un monto:",'\n','\n'"[a] 20 Soles",'\n'"[b] 50  Soles",'\n'"[c] 100 Soles",'\n'"[d] 150 Soles",'\n'"[e] 500 Soles",'\n''\n'"[o] → Otra cantidad") # El usuario podrá hacer retiro de saldo y despues se le mostrara el saldo restante
    a = saldo - 20
    b = saldo - 50
    c = saldo - 100
    d = saldo - 150
    e = saldo - 500
    j = input('\n'"Seleccione un monto: ") 
    if j == 'a':
      print ('\n'"*Saldo disponible: ",a)
    elif j== 'b':
      print ('\n'"*Saldo disponible: ",b)
    elif j == 'c':
      print ('\n'"*Saldo disponible: ",c)
    elif j == 'd':
      print ('\n'"*Saldo disponible: ",d)
    else:
      j == 'e'
      print ('\n'"*Saldo disponible: ",e)
else:
  print ("Contraseña incorrecta") # Si el usuario no digito la contraseña correcta 