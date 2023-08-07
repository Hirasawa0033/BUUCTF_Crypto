import hashlib

obj=hashlib.md5()
obj.update("I am the dog of Focalors.".encode("utf-8"))#before hashing, we need to standerdize codes.
#print(obj)
result=obj.hexdigest()
print(result)