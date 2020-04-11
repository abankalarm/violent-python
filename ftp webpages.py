import ftplib


def returndefault(ftp):
    try:
        dirlist = ftp.nlst()
    except:
        dirlist = []
        print("[-]could not list directory contents")
        print("[-]skipping to next target")
        return
    retlist = []
    for filename in dirlist:
        fn = filename.lower()
        if ".php" in fn or ".htm" in fn or ".asp" in fn:
            print("[+]found default pages" + filename)
            retlist.append(filename)
    return retlist

host = "192.168.95.179"
password = "guest"
username = "guest"
ftp = ftplib.FTP(host)
ftp.login(username,password)
returndefault(ftp)
