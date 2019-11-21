#namedtuple 属性调用不变集
# from collections import namedtuple
# Point = namedtuple('Point',['x','y'])
# Circle = namedtuple('Circle', ['x','y','z'])
# p = Point(1,2)
# c = Circle(1,2,34)
# print(p.x,p.y)
# print(c.x,c.y,c.z)

#deque 
# from collections import deque
# q = deque(['a','b','c'])
# q.append('x')
# q.appendleft('c')
# q.pop()
# q.popleft()
# print(q)

#defaultdict自定义定义默认返回函数值
# from collections import defaultdict
# dd = defaultdict(lambda:'N/A')
# dd['key1'] = 'abc'
# print(dd['key1'])
# print(dd['key2'])

#OrderedDcit有顺序的dict
# from collections import OrderedDict
# d = dict([('a',1),('b',2),('c',3)])
# od = OrderedDict([('a',1),('b',2),('c',3)])
# od['z'] = 1
# od['y'] = 2
# a = list([od.keys(),od.values()])
# print(a)

# def login(user,password):
# 	import hashlib
# 	mpassword = hashlib.md5()
# 	mpassword.update(password.encode('utf-8'))
# 	mpassword = mpassword.hexdigest()
	
# 	db = {
#     'michael': 'e10adc3949ba59abbe56e057f20f883e',
#     'bob': '878ef96e86145580c38c87f0410ad153',
#     'alice': '99b1c2188db85afee403b1536010c2c9'
# }
 
# 	if db[user] == mpassword:
# 		print(db[user])
# 		return 1
# 	else:
# 		return False

# user = input('username')
# password =input('password')
# login(user, password)

import hashlib, random

def get_md5(s):
    return hashlib.md5(s.encode('utf-8')).hexdigest()
class User(object):
    def __init__(self, username, password):
        self.username = username
        self.salt = ''.join([chr(random.randint(48, 122)) for i in range(20)])
        self.password = get_md5(password + self.salt)
db = {
    'michael': User('michael', '123456'),
    'bob': User('bob', 'abc999'),
    'alice': User('alice', 'alice2008')
}
user = db['michael']
assert user.password == get_md5(password)
# print(user.password)
# print(get_md5(user.password))





