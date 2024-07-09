# list = [50,70,60]
# srt_list= sorted(list)
# max = 0
# for i in range(0,len(srt_list)-1):
#     if (srt_list[i] > max):
#        max = srt_list[i]
# print(max)

list = [50,70,20]
max = 0
second_max = 0
for i in range(0,len(list)):
    if (list[i] > max):
       second_max = max
       max = list[i] 
print(second_max)
