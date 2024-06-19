import socket

def test(host, port, timeout=1):
    addr = (host, port)
    try:
        with socket.create_connection(addr, timeout) as sock:
            print('[+] {}/tcp open'.format(port))
    except Exception as e:
        print('[-] {}/tcp closed ({})'.format(port, e))

def scan(host, ports):
    try:
        ip = socket.gethostbyname(host)
    except Exception as e:
        print('[-] Cannot resolve {} ({})'.format(host, e))
        return
    
    try:
        name = socket.gethostbyaddr(ip)
        print('[+] Scan result of: {}'.format(name[0]))
    except Exception:
        print('[+] Scan result of: {}'.format(ip))
        
    for port in ports:
        print('Scanning port: {}'.format(port))
        test(host, port)

if __name__ == '__main__':
    scan('google.com', [80, 22])
