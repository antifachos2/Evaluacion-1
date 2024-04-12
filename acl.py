def identificar_tipo_acl(numero_acl):
    if numero_acl >= 1 and numero_acl <= 99:
        return "ACL Estándar"
    elif numero_acl >= 100 and numero_acl <= 199:
        return "ACL Extendida"
    else:
        return "No corresponde a una lista de acceso"

def main():
    acl1 = "access-list 50 permit any"
    acl2 = "ip access-list 100 permit ip any any"
    acl3 = "ip access-list 20 deny any"

#primera ACL
    partes_acl1 = acl1.split()
    numero_acl1 = int(partes_acl1[1])
    tipo_acl1 = identificar_tipo_acl(numero_acl1)
    print("ACL:", acl1)
    print("Tipo:", tipo_acl1)

 #segunda ACL
    partes_acl2 = acl2.split()
    numero_acl2 = int(partes_acl2[3])
    tipo_acl2 = identificar_tipo_acl(numero_acl2)
    print("\nACL:", acl2)
    print("Tipo:", tipo_acl2)
#tercera ACL
    partes_acl3 = acl3.split()
    numero_acl3 = int(partes_acl3[3])
    tipo_acl3 = identificar_tipo_acl(numero_acl3)
    print("\nACL:", acl3)
    print("Tipo:", tipo_acl3)
