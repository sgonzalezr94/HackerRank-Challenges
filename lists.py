

# Consider a list (list = []). You can perform the following commands:

# insert i e: Insert integer e at position i .
# print: Print the list.
# remove e: Delete the first occurrence of integer e.
# append e: Insert integer  at the end of the list.
# sort: Sort the list.
# pop: Pop the last element from the list.
# reverse: Reverse the list.


from typing import List


class FixedCommandsList:

    def __init__(self):
        self.fixed_list : List = []

    def insert(self,data):
        i,e = data
        self.fixed_list.insert(i,e)
    
    def print(self):
        print(self.fixed_list)
    
    def remove(self,e):
        e = e.pop()
        if e in self.fixed_list:
            self.fixed_list.remove(e)
    
    def append(self,e):
        e = e.pop()
        self.fixed_list.append(e)
    
    def sort(self):
        self.fixed_list.sort()

    def pop(self):
        self.fixed_list.pop()
    
    def reverse(self):
        self.fixed_list.reverse()
        

def commandSwitcher(commands_list):
    switcher = {
            'insert' : commands_list.insert,
            'print' : commands_list.print,
            'remove' : commands_list.remove,
            'append' : commands_list.append,
            'sort' : commands_list.sort,
            'pop' : commands_list.pop,
            'reverse' : commands_list.reverse
        }
    return switcher

def switch(command,switcher):
    return switcher.get(command)


    

if __name__ == '__main__':
    N = int(input())
    CommandsList = FixedCommandsList()
    com_switcher = commandSwitcher(CommandsList)
    for i in range(0,N):
        command_and_parameters = input().split(" ")
        command = command_and_parameters[0]
        parameters = list(map(int,command_and_parameters[1:]))
        selection = switch(command,com_switcher)(parameters) if parameters else switch(command,com_switcher)()
        

    