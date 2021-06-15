import time
class AbstractReestr():

    nRecords = int()
    nReestrs = int()

    def __init__(self):
        self.date_for_name = time.strftime("%Y%m%d")
        self.date_for_reestr = time.strftime("%d/%m/%Y")
        self.prefix = "Z_"
        pass

    def create_name(self):
        print("create file name")
        pass

    def create_header(self):
        print("create reestr's header")
        pass

    def create_middle(self):
        print("create body of reestr")
        pass

    def create_footer(self):
        print("create reestr's footer")
        pass

    def make_reestr(self):
        self.reestr_name = self.create_name()
        self.create_header()
        self.create_middle()
        self.create_footer()
        pass


class Reestr(AbstractReestr):
    org_id_name = "org_ids.txt"
    org_id_list = list()
    def __init__(self, nFiles = 1, nRecords = 1):
        AbstractReestr.__init__(self)

        self.nReestrs = nFiles
        self.nRecords = nRecords

        fout = open(self.org_id_name, "r")
        content = fout.read()
        fout.close()
        self.org_id_list = content.strip().split('\n')

    def create_name(self, num = 0):
        s = self.prefix
        s = s + self.date_for_name
        s = s + ('_%010d' % int(self.org_id_list[0]))
        s = s + ('_%03d.txt' % num)
        return s
        pass

    def create_header(self):
        return "START\t%s\t\n" % self.date_for_reestr
        pass

    def create_middle(self, nRecords = 1):
        s = ""
        for item in range(0, self.nRecords):
            s = s + ("1\tПаспорт\t2\tИжевск, ул. Циолковского 9-66\t%d\t\n" % item)
        return s

    def create_footer(self):
        return "%d\tSTOP" % self.nRecords

    def make_reestr(self):
        file_name = self.create_name()
        freestr = open(file_name, 'w', encoding='utf-8')
        s = self.create_header() + self.create_middle(4) + self.create_footer()
        freestr.write(s)
        freestr.close()

    def enumerator(self):
        pass

    def list_org_id(self):
        pass
