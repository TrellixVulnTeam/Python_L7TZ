import nmap
import json
import re
import ipaddress


sc = nmap.PortScanner();#instancia o nmap
ip_a_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$");#expressões regulares para reorganizar ips
port_r_pattern = re.compile("([0-9]+)-([0-9]+)")
port_i=0
port_m=65535
Open_ports=[]

print ("\n KELSEY CUSTÓDIO MAGALHÃES,2022")

print("Bases de vulnerabilidades consultadas : \n\ncve \nexploitdb \nopenvas \nosvdb \nscipvuldb \nsecurityfocus \nvulscan \nxforce \necuritytracker\n\n")
print ("Argumento : -v para fazer um escaneamento rapido(simples) ")
print ("Argumento : -sL para listas os possíveis  reversos/ips ")
print ("Argumento : -sU para escanear host com UDP ")
print ("Argumento : -sA para descobrir se o alvo é protegido por um firewall")
print ("Argumento : -PN para descobrir quando o alvo é protegido por um firewall")
print ("Argumento : --packet-trace para ver os pacotes")
print ("Argumento : -sS para ")
print ("Argumento : -sS para ")
print ("Argumento : -sS para ")
print ("Argumento : -sS para ")
print ("Argumento : --script=smb-enum-shares.nse ")
print ("Argumento : -sV --script vulscan/vulscan.nse --script-args vulscandb=scipvuldb.csv ")

print("Deseja digite ip ou hostname ? ")#want to type IP or hostname ?
print (" 1 - IP")
print (" 2 - HOSTNAME")
option = input("Qual será a opção ?") #What will be the option ?
if option == '1':
    while True:
        ip_a = input("\nDigite um ip : ")
        if ip_a_pattern.search(ip_a):
            print(f"{ip_a} é um ip valido")
            arg = ip_a
            break
        else:
            print("ip não válido")
            exit()

if option == '2':
    while True:
        hst = input("\nDigite um hostname : ")
        arg = hst
        break

arg1= input("digite o argumento a ser utilizado: ")
if arg == "":
    print("Argumento invalido ");
    exit()
else:
    print("Realizando o scan")
    r = sc.scan(arguments=f'{arg1} ', hosts=f'{arg}')
    js = json.dumps(r, indent=4)
    #with open('../Curso-Udemy/Python-Basico/data.json', 'w') as dj:
        #json.dump(js, dj)
    print (js)