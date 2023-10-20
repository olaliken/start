print("welcome somuch ")
play =input("do you want to play? ").lower()
score =0
if play !='yes'.lower():
    quit()
print('okay lets play welcome:')
ans=input('RAM means? ')
if ans =='random access memory'.lower():
    print("correct")
    score +=1
else:
    print('incorrect')
ans=input('CPU means? ')
if ans =='central processing unit'.lower():
    print("correct")
    score +=1
else:
    print('incorrect')
ans=input('what is your name: ').lower()
if len(ans)>5 and len(ans)<11:
    print("correct")
    score +=1
else:
    print('incorrect')
print(f"YOUR SCORE IS {score} try more next time mr")
print(f"which IS {score/3*100} %")