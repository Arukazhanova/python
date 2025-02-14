# lst=[1,2,3,4,5,6,7,8,9,10]
# target=7
# low,high=0,len(lst)-1
# found=False
# while low<=high:
#     mid=(low+high)//2
#     if lst[mid]==target:
#         found=True
#         break
#     elif lst[mid]<target:
#         low=mid+1
#     else:
#         high=mid-1
# print(found)



# lst=[4,2,8,6,1]
# min=lst[0]
# for x in lst:
#     if x<min:
#         min=x
# print(min)



# lst=[4,-2,8,-6,1]
# result=[]
# for x in lst:
#     if x>=0:
#         result.append(x)
# print(result)



# lst=[4,2,8,6,2]
# shifted=[0]*len(lst)
# for i in range(len(lst)):
#     shifted[(i+1)%len(lst)]=lst[i]
# print(shifted)

# n=64
# is_power_of_two=True
# while n>1:
#     if n%2!=0:
#         is_power_of_two=False
#         break
#     n//=2
# print(is_power_of_two)

# lst=[2,1,9,4,6]
# for i in range(len(lst)):
#     min_index=i
#     for j in range(i+1,len(lst)):
#         if lst[j]<lst[min_index]:
#             min_index=j
#     lst[i],lst[min_index]=lst[min_index],lst[i]
# print(lst)

# lst=[4,2,8,5,2,1,4]
# unique_count=0
# for i in range(len(lst)):
#     is_unique=True
#     for j in range(len(lst)):
#         if i!=j and lst[i]==lst[j]:
#             is_unique=False
#             break
#     if is_unique:
#         unique_count+=1
# print(unique_count)