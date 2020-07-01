class rcparser():
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
