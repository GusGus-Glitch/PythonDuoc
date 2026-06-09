temp = input ("Ingrese la temperatura: ")
unidad = input ("Ingrese su unidad de medida(C, F o K): ").upper()
if unidad != "C" and unidad != "F" and unidad != "K":
   print ("Unidad de medida no válida. Por favor, ingrese C, F o K.")
else:
   if unidad == "C":
      temp_f = (float(temp) * 9/5) + 32
      temp_k = float(temp) + 273.15
      print(f"{temp}°C equivale a {temp_f:.2f}°F y {temp_k:.2f}K.")
   else:
        if unidad == "F":
            temp_c = (float(temp) - 32) * 5/9
            temp_k = temp_c + 273.15
            print(f"{temp}°F equivale a {temp_c:.2f}°C y {temp_k:.2f}K.")
        else:
            if unidad == "K":
                temp_c = float(temp) - 273.15
                temp_f = (temp_c * 9/5) + 32
                print(f"{temp}K equivale a {temp_c:.2f}°C y {temp_f:.2f}°F.")