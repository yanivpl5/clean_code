
try:
    filePath = "/var/log/somelog.log"
    open(filePath)
except FileNotFoundError:
    print("Failed to open file from path", filePath)
