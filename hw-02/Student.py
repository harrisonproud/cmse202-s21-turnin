# The Student class (you'll edit and expand on this)
class Student():
    '''
    This class is designed to include information about individual students.
    Currently this class has the following attributes:
    
    year: this is the number of year the student has been in college
    '''
    #year = 1
       
    '''    
    name : this is the student's name
    gpa : this is the student's curret gpa
    '''
    
    def __init__(self, name='', gpa = 0.0, year=1):
        self.name = name
        self.gpa = gpa
        self.year = year
        
    def get_name(self):
        '''
        This function prints the name of the student
        '''
        print("My name is", self.name)
        
    def year(self):
        '''
        This function prints the graduation year of the student
        '''
        print('I have been in college for', self.year,'year(s).')
    
    def enroll(self, class_list=[]):
        '''
        This function take an inputted list of classes and adds them as an attribute
        '''
        self.classes = class_list
    
    def display_courses(self):
        '''
        This function prints out the list of classes
        '''
        print('I am enrolled in these courses:', self.classes)
        
    def years_until_graduation(self):
        '''
        This function returns the number of years until the student is supposed to graduate
        '''
        print('I am supposed to graduate in:', 4-self.year,'years.')
        
class Spartan(Student):
    
    '''
    This class is supposed take in a motto and prints out a statement about your school spirit
    '''
    def set_motto(self, motto=''):
        self.motto = motto
        
    def school_spirit(self):
        print('My name is', self.name)
        print('I am a Spartan. My motto is', self.motto)
        
        