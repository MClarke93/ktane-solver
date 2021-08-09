import engine.globe as g

# ---------------------------------------------------------------------------------------------------------------------------
# DEVICE CLASS
# ---------------------------------------------------------------------------------------------------------------------------

class Device:
    # Object for a device and its edgework, modules, calender, etc.
    def __init__(self, **kwargs):
        # moduledict = Dictionary of module names -> booleans; specifies whether a module is present
        # modules/needies/batteries/holders/lits/unlits = Integers; number of modules/needies/batteries/holders/lits/unlits
        # starttime = Integer; devices's start time in minutes
        # serial = String; device's serial number
        # year/month/day/weekday = Integers; the year/month/day/weekday the device was started
        for key in ["moduledict","modules","needies","starttime","serial","batteries","holders","lits","unlits","ports","year","month","day","weekday"]:
            setattr(self, key, None)
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __repr__(self):
        # Canonical representation.
        dict = vars(self)
        string = f"Device("
        for key in dict:
            if dict[key] != None:
                string += f"{key}={repr(dict[key])},"
        return string[:-1]+f")"

    # -------
    # MODULES
    # -------

    def setmodules(self):
        # Asks user for the number of modules on the device.
        self.modules = g.question(question="How many modules are on the device?", answers=g.RANGEDICT(1,200), 
        error="Invalid. Expecting an integer between 1 and 300.")
        return True

    def getmodules(self):
        # Returns the number of modules on the device.
        if self.modules == None:
            self.setmodules()
        return self.modules

    def setneedies(self):
        # Asks the user for the number of needies on the device.
        self.needies = g.question(question="How many needies are on the device?", answers=g.RANGEDICT(0,self.getmodules()), 
        error=f"Invalid. Expecting an integer between 0 and {self.modules}.")
        return True

    def getneedies(self):
        # Returns the number of needies on the device.
        if self.needies == None:
            self.setneedies()
        return self.needies
    
    def getsolvables(self):
        # Returns the number of solvable (non-needy) modules on the device.
        return self.getmodules() - self.getneedies()

    def setmodule(self, module=""):
        # Asks the user if a specific module is present on the device.
        self.moduledict[module] = g.question(question=f"Is there a \"{module}\" on the device?", answers=g.BOOLEANDICT)
        return True

    def getmodule(self, module=""):
        # Returns whether or not a specific module is present on the device.
        if self.moduledict == None:
            self.moduledict = {}
        if module not in self.moduledict:
            self.setmodule(module=module)
        return self.moduledict[module]

    # --------------
    # TIME & STRIKES
    # --------------

    def settime(self):
        # Asks user for the device's start time in minutes.
        self.starttime = g.question(question="What was the device's starting time (in min)?", answers=g.RANGEDICT(0, 600), 
        error="Invalid. Expecting an integer between 0 and 999.")
        return True
    
    def gettime(self):
        # Returns the device's start time in minutes.
        if self.starttime == None:
            self.settime()
        return self.starttime
    
    def getstrikes(self):
        # Returns the device's strike count. Ask the user every time.
        return g.question(question="How many strikes does the device currently have?", answers=g.RANGEDICT(0,99), 
        error="Invalid. Expecting an integer between 0 and 99.")

    # -------------
    # SERIAL NUMBER
    # -------------

    def setserial(self):
        # Asks user for the device's serial number.
        letters = g.LETTERLIST.replace("o","").replace("y","")
        numbers = g.NUMBERLIST
        wildcard = letters + numbers
        while True:
            print("What is the device's serial number? ", end="")
            serial = input().lower()
            if len(serial) != 6:
                print("Invalid. Serial numbers must be 6 characters.")
                continue
            if serial[0] not in wildcard or serial[1] not in wildcard:
                print("Invalid. The 1st and 2nd characters must be alphanumeric excluding O and Y.")
                continue
            if serial[2] not in numbers or serial[5] not in numbers:
                print("Invalid. The 3rd and 6th characters must be numbers.")
                continue
            if serial[3] not in letters or serial[4] not in letters:
                print("Invalid. The 4th and 5th characters must be letters excluding O and Y.")
                continue
            break
        self.serial = serial
        return True

    def getserial(self):
        # Returns the device's serial number.
        if self.serial == None:
            self.setserial()
        return self.serial
    
    def getserialchar(self, chars):
        count = 0
        serial = self.getserial()
        for char in chars:
            count += serial.count(char)
        return count

    # ---------
    # BATTERIES
    # ---------

    def setbatteries(self):
        # Asks the user for the number of batteries and battery holders on the device.
        while True:
            self.batteries, self.holders = g.question(question="How many batteries and holders are on the device? Seperate with a space:", 
            answers=g.RANGEDICT(0,32), error="Invalid. Expecting an integer between 0 and 32.", size=2)
            if self.batteries >= self.holders and self.batteries <= self.holders*2:
                break
            else:
                print("Invalid. Impossible combination of batteries & holders.")
        return True
    
    def getbatteries(self):
        # Returns the number of batteries on the device.
        if self.batteries == None:
            self.setbatteries()
        return self.batteries
    
    def getholders(self):
        # Returns the number of battery holders on the device.
        if self.holders == None:
            self.setbatteries()
        return self.holders
    
    def getaas(self):
        # Returns the number of AA batteries on the device.
        return 2*(self.getbatteries()-self.getholders())

    def getds(self):
        # Returns the number of D batteries on the device.
        return 2*self.getholders()-self.getbatteries()

    # ---------
    # INDICATORS
    # ---------

    def setindicators(self):
        # Asks the user for what indicators are present on the device.
        indicators = g.question(question="How many indicators are on the device?", answers=g.RANGEDICT(0, 16))
        self.lits, self.unlits = ([], [])
        num = 1
        while num <= indicators:
            indicator = g.question(question=f"What is indicator #{num}? Lowercase for unlit, uppercase or * for lit:", 
            answers=g.INDICATORDICT, size=1)
            if indicator in ["BOB","CAR","CLR","FRK","FRQ","IND","MSA","NSA","SIG","SND","TRN"]:
                self.lits.append(indicator.lower())
            elif indicator in ["bob","car","clr","frk","frq","ind","msa","nsa","sig","snd","trn"]:
                self.unlits.append(indicator)
            num += 1
        return True

    def getlitlist(self):
        # Returns the list of lit indicators on the device.
        if self.lits == None:
            self.setindicators()
        return self.lits

    def getunlitlist(self):
        # Returns the list of unlit indicators on the device.
        if self.unlits == None:
            self.setindicators()
        return self.unlits

    def getindicatorlist(self):
        # Returns the list of indicators on the device.
        return self.getlitlist() + self.getunlitlist()

    def getlits(self):
        # Returns the number of lit indicators on the device.
        return len(self.getlitlist())

    def getunlits(self):
        # Returns the number of unlit indicators on the device.
        return len(self.getunlitlist())

    def getindicators(self):
        # Returns the number of indicators on the device.
        return len(self.getindicatorlist())

    def getlit(self, indicator):
        # Returns whether a particular lit indicator is present on the device.
        return indicator.lower() in self.getlitlist()

    def getunlit(self, indicator):
        # Returns whether a particular unlit indicator is present on the device.
        return indicator.lower() in self.getunlitlist()

    def getindicator(self, indicator):
        # Returns whether a particular indicator is present on the device.
        return indicator.lower() in self.getindicatorlist()

    # -----
    # PORTS
    # -----

    def setportplates(self):
        # Asks the user for what port plates are present on the device.
        plates = g.question(question="How many port plates are on the device?", answers=g.RANGEDICT(0, 16))
        self.ports = []
        num = 1
        while num <= plates:
            plate = g.question(question=f"What ports are on port plate {num}? Seperate with a space:", 
            answers=g.PORTDICT, size=0)
            self.ports.append(plate)
            num += 1
    
    def getportplatelist(self):
        # Returns the list of port plates (and ports) present on the device.
        if self.ports == None:
            self.setportplates()
        return self.ports
    
    def getplates(self):
        # Returns the number of port plates present on the device.
        return len(self.getportplatelist())
    
    def getempties(self):
        # Returns the number of empty port plates present on the device.
        num = 0
        for plate in self.getportplatelist():
            if plate == ["empty"]:
                num += 1
        return num

    def getportlist(self):
        # Returns a flattened list of ports present on the device.
        flattened = []
        for plate in self.getportplatelist():
            if plate != ["empty"]:
                for port in plate:
                    flattened.append(port)
        return flattened

    def getports(self):
        # Returns the number of ports present on the device.
        return len(self.getportlist())
    
    def getporttypelist(self):
        # Returns a list of distinct port types present on the device.
        return list(set(self.getportlist()))

    def getporttypes(self):
        # Returns the number of distinct port types present on the device.
        return len(self.getporttypelist())
    
    def getport(self, port):
        # Returns the number of a particular port on the device.
        return self.getportlist().count(port)

    # -----------
    # DATE & TIME
    # -----------

    def setyear(self):
        # Asks the user what year the device was started.
        self.year = g.question(question="During what year was the device started?", answers=g.RANGEDICT(2020, 2030), 
        error="Invalid. Expecting an integer between 2020 and 2030.")
        return True
    
    def getyear(self):
        # Returns what year the device was started on.
        if self.year == None:
            self.setyear()
        return self.year

    def setmonth(self):
        # Asks the user what month the device was started on.
        self.month = g.question(question="During what month was the device started?", answers=g.MONTHDICT)
        return True
    
    def getmonth(self):
        # Returns what month the device was started on. January = 1, December = 12.
        if self.month == None:
            self.setmonth()
        return self.month

    def setday(self):
        # Asks the user what day of the month the device was started on.
        self.day = g.question(question="During what day of the month was the device started?", answers=g.RANGEDICT(1, 31), 
        error="Invalid. Expecting an integer between 1 and 31.")
        return True
    
    def getday(self):
        # Returns what day of the month the device was started on.
        if self.day == None:
            self.setday()
        return self.day

    def setweekday(self):
        # Asks the user what day of the weekk the device was started on.
        self.weekday = g.question("On what day of the week was the device started?", answers=g.WEEKDICT)
        return True
    
    def getweekday(self):
        # Returns what weekday the device was started on. Sunday = 1, Saturday = 7.
        if self.weekday == None:
            self.setweekday()
        return self.weekday

    # ----
    # MISC
    # ----

    def setall(self):
        # Asks the user for all of the device's information.
        self.setmodules()
        self.setneedies()
        self.settime()
        self.setserial()
        self.setbatteries()
        self.setindicators()
        self.setportplates()
        self.setyear()
        self.setmonth()
        self.setday()
        self.setweekday()
        return True
    
    def getall(self):
        # Tests all of the get commands.
        str = f'''
    Modules: {self.getmodules()}, 
    Needies: {self.getneedies()}, 
    Solvables: {self.getsolvables()}, 
    The Bulb?: {self.getmodule(module="The Bulb")}, 
    Start Time: {self.gettime()}, 
    Serial No: {self.getserial()}, 
    Batteries: {self.getbatteries()}, 
    Holders: {self.getholders()}, 
    AAs: {self.getaas()}, 
    Ds: {self.getds()}, 
    Lit Indicators: {self.getlitlist()}, 
    Unlit Indicators: {self.getunlitlist()}, 
    Indicators: {self.getindicatorlist()}, 
    # of Lits: {self.getlits()}, 
    # of Unlits: {self.getunlits()}, 
    # of Indicators: {self.getindicators()}, 
    Lit Bob?: {self.getlit('bob')}, 
    Unlit Bob?: {self.getunlit('bob')}, 
    Bob?: {self.getindicator('bob')}, 
    Plates: {self.getportplatelist()}, 
    # of Plates: {self.getplates()}, 
    Empty plates: {self.getempties()}, 
    Ports: {self.getportlist()}, 
    # of Ports: {self.getports()}, 
    Port types: {self.getporttypelist()}, 
    # of port types: {self.getporttypes()}, 
    Serial Port?: {self.getport('serial')},
    Year: {self.getyear()},
    Month: {self.getmonth()},
    Day: {self.getday()},
    Weekday: {self.getweekday()}.
        '''
        print(str)
