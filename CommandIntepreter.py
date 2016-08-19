'''
Created on 19/08/2016

@author: AndrewM
'''
from cmd import Cmd
from InterpreterAssignment import Controller
class CommandIntepreter(Cmd):
    '''
    classdocs
    '''
    intro = "(> ^_^ )>---[ Welcome ]"
    prompt = ">>>"
    
    my_controller = Controller.Controller
    
    def __init__(self):
        
        '''
        Constructor
        '''
        ""
        # modified constructor 
        super(CommandIntepreter,self).__init__()
        self.my_controller = None;
    
    def set_controller(self, the_controller):
        self.my_controller = the_controller
        
    def do_test(self,line):
        self.my_controller.say("rawr")
        
    def do_exit(self,line):
        return True

    # stuff to do before running CMD (in the CMD)
    def preloop(self):
        pass
    # stuff to do before closing the CMD (in the CMD)
    def postloop(self):
        pass