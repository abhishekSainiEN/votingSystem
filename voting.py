#voting system
 
#canidate name
print("************voting system************\n");
 
canidate1=(input("give name of first canidate:"))
canidate2=(input("give name of second canidate:"))
print("*************************************")
can1_count=0
can2_count=0
 
voter_id=[1,2,3,4,5,6,7,8,9,10]
no_of_voters=len(voter_id)
 
print("no of voter:",no_of_voters)
print("*************************************")
voted=[]
 
while True:
    if voter_id==[]:
        print("vote is over:")
        print("*************************************")
        if(can1_count>can2_count):
            print(f"{canidate1} is winner he win by {can1_count}")
            print("*************************************")
        elif(can2_count>can1_count):
            print(f"{canidate2} is winner he win by {can2_count}")
            print("*************************************")
        elif can1_count==can2_count:
            print("tied")
            print("*************************************")
        break
            
    else:
            voter=int(input("give your voter_id:"))
            if voter in voted:
                print("you already voted:")
                print("*************************************")
            else:
                if voter in voter_id:
                 print("choose 1 for vote canidate1:\nchoose 2 for vote canidate2:");
                 choice=int(input("choose own canidate:"))
                 if choice==1:
                    can1_count+=1
                    print(f"you voted {canidate1} and your voter id is {voter}")
                    print("*************************************")
                 elif choice==2:
                    can2_count+=1
                    print(f"you voted {canidate2} and your voter id is{voter}")
                    print("*************************************")
                 voter_id.remove(voter)
                 voted.append(voter)
                else:
                 print("you are not applicable do vote")
            
             