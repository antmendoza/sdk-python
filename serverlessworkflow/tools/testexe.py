from enum import Enum


class Shake(Enum):
    VANILLA = 7
    CHOCOLATE = 4
    COOKIES = 9
    MINT = 3


for shake in Shake:
    print(shake)



def jespintest(sh: Shake):
    print(sh)
    print(sh.name)
    print(sh.value)


jespintest(Shake.VANILLA)