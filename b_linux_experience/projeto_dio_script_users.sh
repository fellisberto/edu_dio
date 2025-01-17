#!/bin/ban

echo "Criando diretoriós..."

mkdir /publico
mkdir /adm
mkdir /ven
mkdir /sec

echo "Criando grupos de usuários..."

groupadd GRP_ADM
groupadd GRP_VEN
groupadd GRP_SEC

echo "Criando usuários..."

useradd carlos -m -s /bin/bash -p $(openssl passwd -crypt senha 123) -G GRP_ADM
useradd ana -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_ADM 
useradd joao -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_ADM 

# Usuários com o grupo GRP_VEN 
useradd maria -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_VEN 
useradd pedro -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_VEN 
useradd lucas -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_VEN 

# Usuários com o grupo GRP_SEC 
useradd sofia -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_SEC 
useradd miguel -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_SEC 
useradd julia -m -s /bin/bash -p $(openssl passwd -crypt 'senha123') -G GRP_SEC 

echo "Especificando permissões dos diretórios..."
chown root:GRP_ADM /adm
chown root:GRP_VEN /ven
chown root:GRP_SEC /sec

chmod 770 /adm 
chmod 770 /ven 
chmod 770 /sec
chmod 777 /publico

echo "Fim..."