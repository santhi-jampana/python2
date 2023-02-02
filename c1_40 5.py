import time
class I_HUB:
    def __init__(self):
        pass
    def m1(self):
        pass
    @classmethod
    def m2(cls):
        pass
    @staticmethod
    def m3():
        I_HUB.sid=2001
        I_HUB.sname="python"
i1=I_HUB()
i1.m3()
print(I_HUB.__dict__)
time.sleep(2)
print("end of an application")
