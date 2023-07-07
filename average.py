import math
print("be barname mohasebe moadel khosh omadid")
name=input("nam va nam khanevadegi khod ra vared konid :")
riazi=int(input("nomre dars riazi ra vared konid: "))
olom=int(input("nomre dars olom ra vared konid: "))
farsi=int(input("nomre dars farsi ra vared konid: "))
average=(riazi+olom+farsi)/3
if average>=17:
    print("moadle ",name,": ",average,"  (Great)")
if average<17 and average>=12:
    print("moadle ",name,": ",average,"  (Normal)")
if average<12:
    print("moadle ",name,": ",average,"  (Fail)")