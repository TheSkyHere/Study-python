from _md5 import md5
import random
abc = random.randint(1, 241241255)
print(abc)
a = md5(str.encode("2"+str(abc)))
print(a.hexdigest())