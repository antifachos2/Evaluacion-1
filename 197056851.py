vlansw1 = [99, 10, 20, 30]
vlansw2 = [200, 40, 50, 60]

if vlansw1[0] == 99:
	print("las vlans son iguales y cumplen con el requerimiento")
else:
	print("las vlans son diferentes y no cumplen con el requerimiento")

vlanreqsw1 = [10,100,30]

if set(vlansw1[1:]) == set(vlanreqsw1):
	print("las vlans son iguales y cumplen con el requerimiento")
else:
	print("las vlans son diferentes y no cumplen con el requerimiento")

if vlansw2[0] == 99:
	print("las vlans son iguales y cumplen con el requerimiento")
else:
	print("las vlans son diferentes y no cumplen con el requerimiento")

vlanreqsw2 = [40,50,60]

if set(vlansw2[1:]) == set(vlanreqsw2):
	print("las vlans son iguales y cumplen con el requerimiento")
else:
	print("las vlans son diferentes y no cumplen con el requerimiento")
