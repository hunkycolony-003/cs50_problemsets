name = str(input("Enter the file name: "))
result = name.rsplit(sep = ".", maxsplit = 1)
if len(result)== 2:
    name, extension = result
else :
    name = result
    extension = "empty"


#matching the extension
match extension.lower().strip():
    case "gif":
        print("image/gif")
    case "jpg" | "jpeg":
        print("image/jpeg")
    case "png":
        print("image/png")
    case "pdf":
        print("application/pdf")
    case "txt":
        print("text/plain")
    case "zip":
        print("application/zip")
    case _:
        print("application/octet-stream")

