import re
import arrow
now = arrow.utcnow().shift(hours = 1)

result = []
# # b = a.shift(hours = 1)
# #
# #
# # time = "6'"
# #
# # judge = re.findall("(\d+)\'",time)
# #
# # print(judge)
# #
# # if judge:
# #
# #     minutes = int(judge[0])
# #
# #     b = b.shift(minutes = minutes )
# #
# #     b = str(b.hour)+":"+str(b.minute)
# #     print(b)
# # else:
# #     print('none')


time = "19'"
judge = re.findall("(\d+)\'", time)

if judge:
    minutes = int(judge[0])
    b = now.shift(minutes=minutes)
    time = str(b.hour) + ":" + str(b.minute)
result.append(time)

print(result)