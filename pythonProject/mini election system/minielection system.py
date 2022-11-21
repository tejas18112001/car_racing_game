# mini election system

candidate1 = input("Enter the name of the first candidate:")
candidate2 = input("Enter the name of second candidate:")
candidate1_vote = 0
candidate2_vote = 0
no_of_nota_votes = 0

voters_id = [1, 2, 3]
no_of_voters = len(voters_id)
print("Total voters: " ,no_of_voters)

while True:

      voter = int(input("Enter the epic voter id:"))
      while voter in voters_id :
            a=input("Do you want to give vote:")
            if a=='no':
                voters_id.remove(voter)
                break
            elif a=='yes':
                pass
                if voter in voters_id:
                    voters_id.remove(voter)
                    print("you are a voter")

                    print("For give your vote to", candidate1, "press:", '1')
                    print("For give your vote to", candidate2, "press:", '2')

                    a = int(input("Enter your choice:"))

                    if a == 1:
                       print("you have given your vote to first candidate", candidate1)
                       print("thanks to give your vote ")
                       candidate1_vote += 1
                    elif a == 2:
                       print("you have given your vote to second candidate", candidate2)
                       print("thanks for your vote")
                       candidate2_vote += 1
                    else:
                       a != 1 or a != 2
                       b = input("you want to give your vote to nota ")
                       if b == 'yes':
                          print("you have given your vote to nota")
                          print("Thanks for your voting")
                          no_of_nota_votes += 1
                       else:

                          print("select proper selection ")
      if voters_id == []:
              print("voting is over")
            print("Thanks to all voters for the voting")
      if candidate1_vote > candidate2_vote:
                persent = (candidate1_vote / no_of_voters) * 100
                print("{} won election by {} %" .format(candidate1, persent))
                break
      elif candidate2_vote > candidate1_vote:
                persent = (candidate2_vote / no_of_voters) * 100
                print("{} won this election by {} %".format(candidate2, persent))
                break
      else:
                print("Election become tie!! Election commition will conduct re-election ")
                break
