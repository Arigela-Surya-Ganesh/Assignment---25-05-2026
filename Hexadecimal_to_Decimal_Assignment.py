#Hexadecimal
val = 0x1B
#   1       B(B=11)
#   16^1    16^0
#   16      1*11
# 16+11
print(val) # ----> OutPut = 27

val = 0x2F
#   2       F(F=15)
#   16^1    16^0
#   32      1*15
# 32+15
print(val) # ----> OutPut = 47


val = 0xAC
#   A(A=10)    C(C=12)
#   16^1       16^0
#   16*10      1*12
# 160+12
print(val) # ----> OutPut = 47

val = 0x1D4
#   1            D(D=13)      4
#   16^2         16^1         16^0
#   16*16*1      16*13         1*4
# 256+208+4
print(val) # ----> OutPut = 468

val = 0x3E8
#   3            E(E=14)      8
#   16^2         16^1         16^0
#   16*16*3      16*14        1*8
# 768+224+8
print(val) # ----> OutPut = 468