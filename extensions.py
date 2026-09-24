# Request and format file name from user
filename = input("File name: ").strip().lower()

# Map extension to associated media type (mime)
if filename.endswith(".gif"):
    mime = "image/gif"
elif filename.endswith(".jpg") or filename.endswith(".jpeg"):
    mime = "image/jpeg"
elif filename.endswith(".png"):
    mime = "image/png"
elif filename.endswith(".pdf"):
    mime = "application/pdf"
elif filename.endswith(".txt"):
    mime = "text/plain"
elif filename.endswith(".zip"):
    mime = "application/zip"
else:
    mime = "application/octet-stream"

print(mime)
