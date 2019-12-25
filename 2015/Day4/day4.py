import hashlib
key = 'yzbqklnj'

ans = 1
while 1:
    s_key = (key + str(ans)).encode()
    md5 = hashlib.md5(s_key).hexdigest()
    if md5.startswith('00000'):
        print(ans,md5)
        break
    ans += 1
