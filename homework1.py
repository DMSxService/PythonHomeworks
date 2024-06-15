example = "Топинамбур"                               # 1.
print(example[0])                                    # 2.
print(example[-1])                                   # 3.
LenStr = len(example)                                # 4.
HalfStr = int(LenStr/2)                              # Чётные хх хх, xxx xxx, не чётные xx x xx, xxx x xxx
RenDiv = LenStr%2
RenDiv2 = HalfStr%2
if (RenDiv == 0 and RenDiv2 == 1) or (RenDiv == 1 and RenDiv2 == 0): print(example[HalfStr::])
elif (RenDiv == 1 and RenDiv2 == 1) or (RenDiv == 0 and RenDiv2 == 0) : print(example[(HalfStr+1)::])
print(example[::-1])                                  # 5.
print(example[1::2])                                  # 6.