# 나는 친구가 적다 (Small)

import re

line = input()
regrex = re.compile("[^0-9]")
line = "".join(regrex.findall(line))
keyword = input()

if keyword in line:
    print(1)
else:
    print(0)
