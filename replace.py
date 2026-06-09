com = input("Ingrese un comentario: ")
com = com.lower().split()
if "malo" in com:
    replace = com.index("malo")
    com[replace] = "***"
    print(" ".join(com))
else:
      print(" ".join(com))