
#--------------------------HELPER FUNCTIONS-----------------------------


#moves ring from the current stack (s_curr), to the new stack (s_new)
def move_ring(s_curr, s_new):
    r_curr = s_curr.pop()
    #if the new stack has a ring on it already
    if(len(s_new)>0):
        r_new = s_new.pop()
        #if the current ring is smaller than the new ring on the new stack
        if(r_curr<r_new):
            s_new.append(r_new)
            s_new.append(r_curr)
        #else trying to put a bigger ring onto a smaller ring, reset the stacks
        else:
            print('Your ring is too big for this stack')
            s_curr.append(r_curr)
            s_new.append(r_new)
    #if no ring on new stack, then add r_curr ring 
    else:
        s_new.append(r_curr)
    


#takes a stack and prints out the stack with the rings on it
def print_ring(s):
    print("   |")
    if(len(s)>0):
        r = s.pop()
        print((3-r)*" " + ("-"*r) + "|" + ("-"*r) )
        print_ring(s)
        s.append(r)




#prints all three stacks with all their rings
def print_stacks(s1, s2, s3):
    print_ring(s1)
    print("\n   |")
    print_ring(s2)
    print("\n   |")
    print_ring(s3)
    print("\n")



#-------------------Initializing variables below--------------
ring1 =1
ring2 =2
ring3 =3

stack1 = []
stack1.append(ring3)
stack1.append(ring2)
stack1.append(ring1)
stack2 = []
stack3 = []

#a win stack to check to see if the user has won
win= []
win.append(ring3)
win.append(ring2)
win.append(ring1)



#----------------------GAME LOOP BELOW-------------------------

#while the user has not won the game
while(stack3!=win):
    print_stacks(stack1, stack2, stack3)

    #get first stack
    s_in1="error"
    while(s_in1=="error"):
        s_in1 = input("Enter the stack number you would like to move a ring from\n")
        
        if(s_in1=="1"):
            s_curr = stack1
        elif(s_in1=="2"):
            s_curr=stack2
        elif(s_in1=="3"):
            s_curr=stack3
        else:
            print("invalid input")
            s_in1=="error"

    #get second stack
    s_in2 = "error"
    while(s_in2=="error"):
        s_in2 = input("Enter the stack number you would like to move this ring to\n")

        if(s_in2=="1"):
            s_new = stack1
        elif(s_in2=="2"):
            s_new=stack2
        elif(s_in2=="3"):
            s_new=stack3
        else:
            print("invalid input")
            s_in2=="error"

    #move the top ring of current stack (s_curr) to the top of the new stack (s_new)
    move_ring(s_curr, s_new)

#when user's stack 3 = win stack, the user has won
print("You win!")


  