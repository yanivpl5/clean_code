
try:
    filePath = "/var/log/somelog.log"
    open(filePath)
except FileNotFoundError:
    print("Unexpected error")
