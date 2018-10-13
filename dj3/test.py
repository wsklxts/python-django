# _numbers = ''.join(map(str, range(3, 10)))  # 数字
#
# s=range(3, 10)
# ss=list(range(3, 10))
# ss="".join(str(ss))
# print(ss)
#
# list3=[1,23,4,5]
# str4 = "".join(map(str,list3))
# print(str4)


def check_login(func):
    def inner(request):
            print(request)
            return func(request)
    return inner

# @check_login
def now(a):
    print(a)

now=check_login(now)

now(123)

