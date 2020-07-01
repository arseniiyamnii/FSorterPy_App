class rcparser():
    def __init__(self, path_to_organizerc):
        self.path_to_organizerc=path_to_organizerc
    
    def check_rc(dirrectory):
        '''this function must return existense rc file in some dirrectory
            dirrectory starts from /, not from home.'''
        try:
            f = open(dirrectory)
            exist = True
            f.close()
        except IOError: 
            exist = False
        return exist
    
    def get_path_to_organizerc(self):
        return self.path_to_organizerc
