"""
Created on 19/08/2016

@author: AndrewM
"""
from cmd import Cmd
from InterpreterAssignment import Controller
class CommandIntepreter(Cmd):
    """
    classdocs
    """
    intro = "(> ^_^ )>---[ Welcome ]"
    prompt = ">>>"
    
    my_controller = Controller.Controller
    
    def __init__(self):
        
        '''
        Constructor
        '''
        ""
        # modified constructor, therefore have to call super
        super(CommandIntepreter,self).__init__()
        self.my_controller = None;
    
    def set_controller(self, the_controller):
        self.my_controller = the_controller
                
    # Gets information from the web   
    def do_get_data(self, line):
        """
        (> ^_^ )>---[ "Dumps" the collected data ]
        """
        self.my_controller.display_data()
    
    # Sets the path for the db
    def do_set_db_path(self, the_path):
        """
        (> ^_^ )>---[ Set the path to be used for saving the database ]
                    [ Type the path name after the command ]
        """
        self.my_controller.set_db_path(the_path)
    
    def do_get_db_path(self, line):
        """
        (> ^_^ )>---[ Get the path which would be used for saving the ]
                    [ data base ]
        """
        self.my_controller.get_db_path()
    
    def do_save_data(self, line):
        """
        (> ^_^ )>---[ Save data gathered from scraping, so it can be ]
                    [ loaded in another session, loads from then ]
                    [ default directory if a path has not been ]
                    [ specified ]
        """
        self.my_controller.save_data()
    
    def do_load_data(self, line):
        """
        (> ^_^ )>---[ Load saved data from another session ]
        """
        self.my_controller.load_data()
        
    def do_scrape_data(self, line):
        """
        (> ^_^ )>---[ Get data from the web ]
        """
        self.my_controller.scrape_data()
        
    def do_exit(self,line):
        """
        (> ^_^ )>---[ Exit the Program ]
        """
        return True

    # stuff to do before running CMD (in the CMD)
    def preloop(self):
        pass
    # stuff to do before closing the CMD (in the CMD)
    def postloop(self):
        pass