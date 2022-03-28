import nmap

scan = nmap.PortScanner()

scan.scan('www.cooxupe.com.br','1-1000')
scan.command_line('map -sS -sC -Pn --script vuln www.cooxupe.com.br')
