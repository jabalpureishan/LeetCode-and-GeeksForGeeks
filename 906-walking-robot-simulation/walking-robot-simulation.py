class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        obs,drct,x,y,Max = set(),"n",0,0,0
        for i in obstacles:
            obs.add((i[0],i[1]))
        for i in commands:
            #print("i:",i)
            if i==-1:
                if drct=="n": drct = "e"
                elif drct=="e": drct = "s"
                elif drct=="s": drct = "w"
                elif drct=="w": drct = "n"
            elif i==-2:
                if drct=="n": drct = "w"
                elif drct=="e": drct = "n"
                elif drct=="s": drct = "e"
                elif drct=="w": drct = "s"  
            else:
                #print("before:",x,y)
                currx,curry = x,y
                for k in range(i):
                    
                    if drct=="n": 
                        if (currx,curry+1) in obs:
                            #print("block")
                            break
                        curry += 1 
                    elif drct=="w": 
                        if (currx-1,curry) in obs:
                            #print("block")
                            break
                        currx -= 1 
                    elif drct=="s": 
                        if (currx,curry-1) in obs:
                            #print("block")
                            break
                        curry -= 1 
                    elif drct=="e": 
                        if (currx+1,curry) in obs:
                            ##print("block")
                            break
                        currx += 1 
                    ##print("moving",currx,curry)
                x,y = currx,curry
                ##print("afer:",x,y)
                
                # prevx,prevy = x,y
                # if drct=="n": y += i
                # elif drct=="w": x -= i
                # elif drct=="s": y -= i
                # elif drct=="e": x += i
                # ##print("afer:",x,y)
                # d = dist(x,y,prevx,prevy)
                # for j in obs:
                #     #x==prevx==j[0] and j[1] in range(min(prevy,y)+1,max(prevy,y)) or  y==prevy==j[1] and j[0] in range(min(prevx,x)+1,max(prevx,x)):
                #     if dist(j[0],j[1],prevx,prevy)+dist(x,y,j[0],j[1]) == d: 
                #         x,y = j[0],j[1]
                #         ##print("blocked")
                #         if drct=="n": y -= 1
                #         elif drct=="w": x += 1
                #         elif drct=="s": y += 1
                #         elif drct=="e": x -= 1
                #         ##print("curr",x,y)
                #         break
            ##print("drct",drct)
            Max = max(Max,x*x+y*y)
        return Max

        