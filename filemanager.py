import os
import pickle


class FileManager:
    def __init__(self):
        self.names = []
        self.items = []
        self.management_names = []
        self.management_items = []
        self.cardkind = ['기타','국민','비씨','농협','하나','신한','현대','롯데','삼성','외환','우리','신협']
        self.payslip = ['김창희', '이의순', '강세분', '장기옥', '서정숙',
                                    '조애영', '송복현', '이서영', '김은영', '정현영', 
                                    '이효숙', '이정연', '윤우숙', '김숙경', '윤혜옥',
                                    '최선희', '정현진', '한수내']
        self.directory = "C:/samusil/"
        self.payslip_dir = "C:/samusil/급여명세서/"
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        if not os.path.exists(self.payslip_dir):
            os.makedirs(self.payslip_dir)
        
        self.names = self.fileload("name.txt")
        self.management_names = self.fileload("storename.txt")
        self.management_items = self.fileload("storeitem.txt")
        self.branch_names = self.fileload("branchname.txt")
        self.branch_percent = self.fileload("branchpercent.txt")
        self.bonsa_percent = self.fileload("bonsapercent.txt")
        
        self.file_name = self.directory + "list.dat"
        if not os.path.exists(self.file_name):
            with open(self.file_name, "wb") as f:
                pickle.dump(self.items, f)

        with open(self.file_name, "rb") as f:
            self.items = pickle.load(f)
            self.items.sort()
    
    def fileload(self, filename):
        with open(self.directory + filename, 'r', encoding="utf-8") as f:
            self.l = f.read().splitlines()
        return self.l
    
    def save(self):
        with open(self.file_name, "wb") as f:
            pickle.dump(self.items, f)