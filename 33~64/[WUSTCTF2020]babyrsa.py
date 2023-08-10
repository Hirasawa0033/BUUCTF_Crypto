import gmpy2
from Crypto.Util.number import *
c = 28767758880940662779934612526152562406674613203406706867456395986985664083182
n = 73069886771625642807435783661014062604264768481735145873508846925735521695159
e = 65537
p = 189239861511125143212536989589123569301
q = 386123125371923651191219869811293586459
phi = (p-1)*(q-1)
d = gmpy2.invert(e,phi)
message = pow(c,d,n)
print(long_to_bytes(message))