import re
import numpy as np
import sys as sys 
import robo_possib as rp 

 

print("*******chat with me !************")
print("yes ?  (enter exit for exiting)")
user=""
while user!="exit":
    user=input("You :  ")
  
    found = False
    for a in rp.greetings_with_quest :
        if re.search(a,user):
            found = True
            print(f"robo : ",np.random.choice(rp.greetings_with_quest_respo))
        else:
            break
    for b in rp.greetings:
        if re.search(b,user):
            found = True
            print(f"robo : ",np.random.choice(rp.greetings_respo))
        else:
            break
    for c in rp.personal:
        if re.search(c,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.personal_respo))
        else:
            break
    for d in rp.living:
        if re.search(d,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.living_respo))
        else:
            break
    for e in rp.relevant:
        if re.search(e,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.relevant_respo)) 
        else:
            break
    for f in rp.rude_words:
        if re.search(f,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.rude_words_respo)) 
        else:
            break
    for g in rp.love_words:
        if re.search(g,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.love_words_respo)) 
        else:
            break
    for h in rp.sad_words:
        if re.search(h,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.sad_words_respo))
        else:
            break
    for i in rp.about_robo:
        if re.search(i,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.about_robo_respo)) 
        else:
            break
    for j in rp.repeat_same:
        if re.search(j,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.repeat_same))
        else:
            break
    for l in rp.exit_words:
        if re.search(l,user):
            found = True
            print(f"robo : " ,"ok ! if u need me u can call me anytime " )
            sys.exit()
        else:
            break
    for k in rp.good_words:
        if re.search(k,user):
            found = True
            print(f"robo : " ,np.random.choice(rp.good_words_respo)) 
        else:
            break
    for m in rp.creator:
         if re.search(m,user):
             found = True
             print(f"robo : " ,np.random.choice(rp.creator_respo))
         else:
             break
      
    if found==False:
         print(f"robo : " ,np.random.choice(rp.invalid_respo))
            
 
         
         
           
      
              
    
       
        
        
        
        
        
        