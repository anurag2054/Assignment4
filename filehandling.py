
try:
    x=open('sample.txt', 'r')
    read=x.read()
    print(read)
    x.close()
except FileNotFoundError:
    print("The File 'sample.txt' does not found")
