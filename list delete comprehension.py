print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First thing first', '4DX']
del daftar_buku[1]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First thing first', '4DX']
del daftar_buku[0:-2]#START#END
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nPerintah del')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First thing first', '4DX']
del daftar_buku[0::3]#START#END#STEP
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First thing first', '4DX']
daftar_buku_baru = daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru')
daftar_buku = ['Seven Habits', 'How to Influence People', 'First thing first', '4DX']
del daftar_buku[:]
for i in range(0, len(daftar_buku)):
    print(daftar_buku[i])

print('\nMembuat list baru dengan comprehension: ganjil')
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First thing first', '4 4DX']
daftar_buku_baru = daftar_buku[0::2]
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: genap')
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First thing first', '4 4DX']
daftar_buku_baru = daftar_buku[1::2] #start #stop #end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: buang di ujung')
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First thing first', '4 4DX']
daftar_buku_baru = daftar_buku[0:-1:2] #start #stop #end
for i in range(0, len(daftar_buku_baru)):
    print(daftar_buku_baru[i])

print('\nMembuat list baru dengan comprehension: ganjil') #simple
daftar_buku = ['1 Seven Habits', '2 How to Influence People', '3 First thing first', '4 4DX']
print(daftar_buku[0::2])