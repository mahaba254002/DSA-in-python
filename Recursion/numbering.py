def ten_1(num):
  if num<1:
    print("End of recursion")
  else:
    ten_1(num-1)
    print(num)

ten_1(10)