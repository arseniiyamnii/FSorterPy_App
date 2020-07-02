from shutil import copyfile


class rcparser():
    def __init__(self, path_to_organizerc):
        self.__path_to_organizerc = path_to_organizerc
        self.__paths=[]
        self.__todos=[]
        self.__patterns=[]
        self.__works=[]
    def check_rc(self):
        '''this function must return existense rc file in some dirrectory'''
        try:
            f = open(self.__path_to_organizerc)
            exist = True
            f.close()
        except IOError:
            exist = False
        return exist

    def get_path_to_organizerc(self):
        return self.__path_to_organizerc

    def copy_organizerc(self, path_to_new_organizerc):
        copyfile("./file_sorter/res/.organizerc",
                 path_to_new_organizerc+"/.organizerc")

    def syntax_checking(self):
        with open(self.__path_to_organizerc) as organizerc:
                lines_in_organizerc = organizerc.read().splitlines()
          
        paths_exist = False
        todos_exist = False
        patterns_exist = False
        work_exist = False
        for line in lines_in_organizerc:
            if line == "[paths]":
                paths_exist = True
            if line == "[todos]":
                todos_exist = True
            if line == "[patterns]":
                patterns_exist = True
            if line == "[works]":
                work_exist = True
        syntax_correct = False
        if paths_exist and todos_exist and patterns_exist and work_exist :
            syntax_correct = True
        return syntax_correct
    def parse_organizerc_by_lines(self,field, array):
        field_index = array.index(field)
        returning_array=[]
        for i in range(field_index+1,len(array)):
            if array[i] not in ["[paths]","[todos]","[patterns]","[works]"]:
                returning_array.append(array[i])
            else:
                break
        return returning_array
    
    def parse_paths(self):
        with open(self.__path_to_organizerc) as organizerc:
                lines_in_organizerc = organizerc.read().splitlines()
        self.__paths=self.parse_organizerc_by_lines("[paths]",lines_in_organizerc)
        return len(self.__paths)


    def parse_patterns(self):
        with open(self.__path_to_organizerc) as organizerc:
                lines_in_organizerc = organizerc.read().splitlines()
        self.__patterns=self.parse_organizerc_by_lines("[patterns]",lines_in_organizerc)
        return len(self.__patterns)


    def parse_todos(self):
        with open(self.__path_to_organizerc) as organizerc:
                lines_in_organizerc = organizerc.read().splitlines()
        self.__todos=self.parse_organizerc_by_lines("[todos]",lines_in_organizerc)
        return len(self.__todos)


    def parse_works(self):
        with open(self.__path_to_organizerc) as organizerc:
                lines_in_organizerc = organizerc.read().splitlines()
        self.__works=self.parse_organizerc_by_lines("[works]",lines_in_organizerc)
        return len(self.__works)

    def get_paths_count(self):
        return len(self.__paths)
    def get_patterns_count(self):
        return len(self.__patterns)
    def get_todos_count(self):
        return len(self.__todos)
    def get_works_count(self):
        return len(self.__works)
