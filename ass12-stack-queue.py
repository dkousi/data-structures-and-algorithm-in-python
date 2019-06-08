#DSA-Assgn-12
class Stack:
    def __init__(self,max_size):
        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__top=-1
    
    def is_full(self):
        if(self.__top==self.__max_size-1):
            return True
        return False
    
    def is_empty(self):
        if(self.__top==-1):
            return True
        return False
    
    def push(self,data):
        if(self.is_full()):
            print("The stack is full!!")
        else:
            self.__top+=1
            self.__elements[self.__top]=data
    
    def pop(self):
        if(self.is_empty()):
            print("The stack is empty!!")
        else:
            data= self.__elements[self.__top]
            self.__top-=1
            return data
    def display(self):
        if(self.is_empty()):
            print("The stack is empty")
        else:
            index=self.__top
            while(index>=0):
                print(self.__elements[index])
                index-=1
    
    def get_max_size(self):
        return self.__max_size
                                                   
    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__top
        while(index>=0):
            msg.append((str)(self.__elements[index]))
            index-=1
        msg=" ".join(msg)
        msg="Stack data(Top to Bottom): "+msg
        return msg
class Queue:
    def __init__(self,max_size):

        self.__max_size=max_size
        self.__elements=[None]*self.__max_size
        self.__rear=-1
        self.__front=0

    def is_full(self):
        if(self.__rear==self.__max_size-1):
                return True
        return False

    def is_empty(self):
        if(self.__front>self.__rear):
            return True
        return False

    def enqueue(self,data):
        if(self.is_full()):
            print("Queue is full!!!")
        else:
            self.__rear+=1
            self.__elements[self.__rear]=data

    def dequeue(self):
        if(self.is_empty()):
            print("Queue is empty!!!")
        else:
            data=self.__elements[self.__front]
            self.__front+=1
            return data

    def display(self):
        for index in range(self.__front, self.__rear+1):
            print(self.__elements[index])


    def get_max_size(self):
        return self.__max_size

    #You can use the below __str__() to print the elements of the DS object while debugging
    def __str__(self):
        msg=[]
        index=self.__front
        while(index<=self.__rear):
            msg.append((str)(self.__elements[index]))
            index+=1
        msg=" ".join(msg)
        msg="Queue data(Front to Rear): "+msg
        return msg

class Ball:
    def __init__(self,color,name):
        self.__color=color
        self.__name=name
        
    def __str__(self):
        return (self.__color+" "+self.__name)
    
    def get_color(self):
        return self.__color
    
    def get_name(self):
        return self.__name
             
#Implement Game class here
class Game:
    def __init__(self,ball_stack):
        self.ball_container=ball_stack
        self.red_balls_container=Stack(2)
        self.green_balls_container=Stack(2)
        self.blue_balls_container=Stack(2)
        self.yellow_balls_container=Stack(2)
        
    def grouping_based_on_color(self):
        for i in range (self.ball_container.get_max_size()):
            a=self.ball_container.pop()
            if a.get_color()=="Red":
                self.red_balls_container.push(a)
            elif a.get_color()=="Blue":
                self.blue_balls_container.push(a)
            elif a.get_color()=="Yellow":
                self.yellow_balls_container.push(a)
            else:
                self.green_balls_container.push(a)
    def rearrange_balls(self,color):
        if color == "Red":
            for x in range (2):
                ball =self.red_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.red_balls_container.push(b)
            self.red_balls_container.push(a)
        elif color == "Blue":
            for x in range (2):
                ball =self.blue_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.blue_balls_container.push(b)
            self.blue_balls_container.push(a)
        elif color == "Yellow":
            for x in range (2):
                ball =self.yellow_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.yellow_balls_container.push(b)
            self.yellow_balls_container.push(a)
        else:
            for x in range (2):
                ball =self.green_balls_container.pop()
                if ball.get_name() == "A":
                    a = ball
                else:
                    b = ball
            self.green_balls_container.push(b)
            self.green_balls_container.push(a)
    def display_ball_details(self, color):
        pass
#Use different values to test your program
ball1=Ball("Red","A")
ball2=Ball("Blue","B")
ball3=Ball("Yellow","B")
ball4=Ball("Blue","A")
ball5=Ball("Yellow","A")
ball6=Ball("Green","B")
ball7=Ball("Green","A")
ball8=Ball("Red","B")
ball_list=Stack(8)
ball_list.push(ball1)  
ball_list.push(ball2) 
ball_list.push(ball3) 
ball_list.push(ball4) 
ball_list.push(ball5) 
ball_list.push(ball6) 
ball_list.push(ball7) 
ball_list.push(ball8)   

game=Game(ball_list)
game.grouping_based_on_color()
#Create objects of Game class, invoke the methods and test the program
                                                    
