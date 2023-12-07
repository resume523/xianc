import re
from datetime import datetime
import random
import inspect
# odds=[1,3,5,7,9,11,13,15,17,19,21,23,25,27,29,31,33,35,37,39,41,43,45,47,49,51,53,55,57,59]
# # right_this_minite=datetime.today().minute
# # if right_this_minite in odds:
# #     print("this minute seems a little odds")
# # else:
# #     print("not an odds minute")
# tt=random.sample(odds,10)
# print(tt)
# print(tt[0])
# print(tt[1])
# print(tt[2])
def add(x,y,z):
    f=inspect.currentframe()
    print(f.f_back)
    print(inspect.getframeinfo(f.f_back)[3])
    print(inspect.getframeinfo(f.f_back))
    for line in inspect.getframeinfo(f.f_back)[3]:
        print(line)
        print(re.findall(r"(\(.*?\))",line)[0])
add(1,2,3)