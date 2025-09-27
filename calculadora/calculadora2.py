num = float(input("introduce un numero").strip())
symbol =input("introduce un simbolo")
num2 = float(input("introduce un numero"))

if symbol=="+":
  print(f"La suma de los numeros es {num+num2}")
elif symbol=="-":
  print(f"La resta de los numeros es {num-num2}")
elif symbol=="*":
  print(f"La multiplicacion de los numeros es {num*num2}")
elif symbol=="/":
  print(f"La division de los numeros es {num/num2}")
else:
  print("No reconozco la operacion")
