Format = int(input("Enter Bit Format 4/8 :"))
if(Format==4):
    a,b,c,d = input().split()
    a,b,c,d = int(a),int(b),int(c),int(d)
    ans= a*8 + b*4 + c*2 + d*1
    print("In Binary Form : ", ans)
elif(Format==8):
    a,b,c,d,e,f,g,h = input().split()
    a,b,c,d,e,f,g,h  = int(a),int(b),int(c),int(d),int(e),int(f),int(g),int(h)
    ans= a*128 + b*64 + c*32 + d*16+e*8 + f*4 + g*2 + h*1
    print("In Binary Form : ", ans)


    


    

   