# list = [50,70,60]
# srt_list= sorted(list)
# max = 0
# for i in range(0,len(srt_list)-1):
#     if (srt_list[i] > max):
#        max = srt_list[i]
# print(max)

list = [30,40,50,20,100]
min = float('inf')
second_min = 0
for i in range(0,len(list)):
    if (list[i] < min):
       second_min = min
       min = list[i] 
print(second_min)

