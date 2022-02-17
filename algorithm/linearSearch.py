# dictionary for search 
config = { "server":"127.0.0.1", "port":1080, "encrypt":"aes-256-gcm", "fast-open":True}

def linarsearch():
    count = 0
    for i in config.values():
        count += 1
        if i == 1080:
            print("%5s founded after %5i search" %(i, count))
            return
    print("not founded")

linarsearch()

