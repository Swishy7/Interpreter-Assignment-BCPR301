from cmd import Cmd
import controller


class CommandInterpreter(Cmd):
    """
    classdocs
    """
    intro = "(> ^_^ )>---[ Welcome ]"
    prompt = ">>>"

    #my_controller = Controller.Controller

    def __init__(self):

        '''
        Constructor
        '''
        ""
        # modified constructor, therefore have to call super
        super(CommandInterpreter, self).__init__()
        self.my_controller = None

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
                    [ loaded in another session, loads from the ]
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

    def do_get_average_price(self, line):
        """
        (> ^_^)>---[ Display the average price of the loaded products ]
        """
        self.my_controller.get_average_price()

    def do_get_max_price(self, line):
        """
        (> ^_^)>---[ Displays the highest price ]
        """
        self.my_controller.get_max_price()

    def do_get_min_price(self, line):
        """
        (> ^_^)>---[ Displays the lowest price ]
        """
        self.my_controller.get_min_price()

    def do_get_min_views(self, line):
        """
        (> ^_^)>---[ Displays the product with the least views]
        """
        self.my_controller.get_min_views()

    def do_get_max_views(self, line):
        """
        (> ^_^)>---[ Displays the product with the most views]
        """
        self.my_controller.get_max_views()

    def do_get_average_views(self, line):
        """
        (> ^_^)>---[ Displays the average views across all loaded products]
        """
        self.my_controller.get_average_views()

    def do_set_file_name(self, name):
        """
        (> ^_^)>---[ Sets name of file that gets saved when calling save_data ]
        """
        self.my_controller.set_file_name(name)

    def do_exit(self, line):
        """
        (> ^_^ )>---[ Exit the Program ]
        """
        return True

    # stuff to do before closing the CMD (in the CMD)
    def postloop(self):
        pass
