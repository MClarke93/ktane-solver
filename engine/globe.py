import itertools, os

# ---------------------------------------------------------------------------------------------------------------------------
# GLOBAL DICTIONARIES, LISTS & VARIABLES
# ---------------------------------------------------------------------------------------------------------------------------

LETTERLIST = "abcdefghijklmnopqrstuvwxyz"
NUMBERLIST = "0123456789"

# ---------------------------------------------------------------------------------------------------------------------------
# GLOBAL "ANSWER DICTIONARIES" (for use with globe.question)
# ---------------------------------------------------------------------------------------------------------------------------

MODULEDICT = {py[:-3]:py[:-3] for py in os.listdir("modules") if py[-3:] == ".py"}

INDICATORDICT = {"*b":"BOB","*bo":"BOB","*bob":"BOB","*c":"CAR","*ca":"CAR","*car":"CAR","*cl":"CLR","*clr":"CLR","*f":"FRK",
"*fr":"FRK","*frk":"FRK","*frq":"FRQ","*i":"IND","*in":"IND","*ind":"IND","*m":"MSA","*ms":"MSA","*msa":"MSA","*n":"NSA",
"*ns":"NSA","*nsa":"NSA","*s":"SIG","*si":"SIG","*sig":"SIG","*sn":"SND","*snd":"SND","*t":"TRN","*tr":"TRN","*trn":"TRN",
"b":"bob","B":"BOB","bo":"bob","BO":"BOB","bob":"bob","BOB":"BOB","c":"car","C":"CAR","ca":"car","CA":"CAR","car":"car",
"CAR":"CAR","cl":"clr","CL":"CLR","clr":"clr","CLR":"CLR","f":"frk","F":"FRK","fr":"frk","FR":"FRK","frk":"frk","FRK":"FRK",
"frq":"frq","FRQ":"FRQ","i":"ind","I":"IND","in":"ind","IN":"IND","ind":"ind","IND":"IND","m":"msa","M":"MSA","ms":"msa",
"MS":"MSA","msa":"msa","MSA":"MSA","n":"nsa","N":"NSA","ns":"nsa","NS":"NSA","nsa":"nsa","NSA":"NSA","s":"sig","S":"SIG",
"si":"sig","SI":"SIG","sig":"sig","SIG":"SIG","sn":"snd","SN":"SND","snd":"snd","SND":"SND","t":"trn","T":"TRN","tr":"trn",
"TR":"TRN","trn":"trn","TRN":"TRN"}

PORTDICT = {'d':'dvid','dv':'dvid','dvi':'dvid','dvid':'dvid','dvi-d':'dvid','p':'parallel','pa':'parallel','par':'parallel',
'para':'parallel','paral':'parallel','parall':'parallel','paralle':'parallel','parallel':'parallel','ps':'ps2','ps2':'ps2',
'ps/2':'ps2','r':'rj45','rj':'rj45','rj4':'rj45','rj45':'rj45','rj-45':'rj45','s':'serial','se':'serial','ser':'serial',
'seri':'serial','seria':'serial','serial':'serial','st':'stereorca','ste':'stereorca','ster':'stereorca','stere':'stereorca',
'stereo':'stereorca','stereor':'stereorca','stereorc':'stereorca','stereorca':'stereorca','rc':'stereorca','rca':'stereorca',
'e':'empty','em':'empty','emp':'empty','empt':'empty','empty':'empty','n':'empty','no':'empty','non':'empty','none':'empty',
'':'empty'}

MONTHDICT = {"1":1,"j":1,"ja":1,"jan":1,"janu":1,"janua":1,"junuar":1,"january":1,"2":2,"f":2,"fe":2,"feb":2,"febr":2,
"febru":2,"februa":2,"februar":2,"february":2,"3":3,"m":3,"ma":3,"mar":3,"marc":3,"march":3,"4":4,"a":4,"ap":4,"apr":4,
"apri":4,"april":4,"5":5,"may":5,"6":6,"ju":6,"jun":6,"june":6,"7":7,"jul":7,"july":7,"8":8,"au":8,"aug":8,"augu":8,
"augus":8,"august":8,"9":9,"s":9,"se":9,"sep":9,"sept":9,"septe":9,"septem":9,"septemb":9,"septembe":9,"september":9,"10":10,
"o":10,"oc":10,"oct":10,"octo":10,"octob":10,"octobe":10,"october":10,"11":11,"n":11,"no":11,"nov":11,"nove":11,"novem":11,
"novemb":11,"novembe":11,"november":11,"12":12,"d":12,"de":12,"dec":12,"dece":12,"decem":12,"decemb":12,"decembe":12,
"december":12}

WEEKDICT = {"1":1,"s":1,"su":1,"sn":1,"sun":1,"sund":1,"sunda":1,"sunday":1,"2":2,"m":2,"mo":2,"mon":2,"mond":2,"monda":2,
"monday":2,"3":3,"t":3,"tu":3,"te":3,"tue":3,"tues":3,"tuesd":3,"tuesda":3,"tuesday":3,"4":4,"w":4,"we":4,"wed":4,"wedn":4,
"wedne":4,"wednes":4,"wednesd":4,"wednesda":4,"wednesday":4,"5":5,"th":5,"tr":5,"thu":5,"thr":5,"thur":5,"thurs":5,"thursd":5,
"thursda":5,"thursday":5,"6":6,"f":6,"fr":6,"fri":6,"frid":6,"frida":6,"friday":6,"7":7,"sa":7,"st":7,"sat":7,"satu":7,
"satur":7,"saturd":7,"saturda":7,"saturday":7}

BOOLEANDICT = {'y':True,'ye':True,'yes':True,'t':True,'tr':True,'tru':True,'true':True,'1':True,'n':False,'no':False,
'f':False,'fa':False,'fal':False,'fals':False,'false':False,'0':False}

MORSEDICT = {".-":"a","-...":"b","-.-.":"c","-..":"d",".":"e","..-.":"f","--.":"g","....":"h","..":"i",".---":"j","-.-":"k",
".-..":"l","--":"m","-.":"n","---":"o",".--.":"p","--.-":"q",".-.":"r","...":"s","-":"t","..-":"u","...-":"v",".--":"w",
"-..-":"x","-.--":"y","--..":"z","-----":"0",".----":"1","..---":"2","...--":"3","....-":"4",".....":"5","-....":"6",
"--...":"7","---..":"8","----.":"9","a":"a","b":"b","c":"c","d":"d","e":"e","f":"f","g":"g","h":"h","i":"i","j":"j","k":"k",
"l":"l","m":"m","n":"n","o":"o","p":"p","q":"q","r":"r","s":"s","t":"t","u":"u","v":"v","w":"w","x":"x","y":"y","z":"z",
"0":"0","1":"1","2":"2","3":"3","4":"4","5":"5","6":"6","7":"7","8":"8","9":"9"}

def RANGEDICT(start, end):
    dict = {}
    for num in range(start, end+1):
        dict[str(num)] = num
    return dict

def SIMPLEDICT(str):
    return {char:char for char in str}

# ---------------------------------------------------------------------------------------------------------------------------
# GLOBAL METHODS
# ---------------------------------------------------------------------------------------------------------------------------

def question(question, answers, error=None, size=1, delim=None):
    # Asks the user a question until a valid answer is given.
    # Answers is a DICTIONARY where keys are valid user inputs, and values are what's returned.
    # Error is the error message. If ERROR is none, one will be automatically generated.
    # Size is the number of space seperated answers to expect from the user. Size <= 0 means 'any size'.
    # Delim is the delimiter used to seperate answers when size is not 1. '' will split every character.
    while True:
        print(f"{question} ", end="")
        userinputs = input()
        if size != 1:
            if delim == '':
                userinputs = list(userinputs)
            else:
                userinputs = userinputs.split(sep=delim)
            if len(userinputs) == 0:
                userinputs = [""]
        else:
            userinputs = [userinputs]
        response = []
        for userinput in userinputs:
            if userinput not in answers:
                userinput = userinput.lower()
                if userinput not in answers:
                    if error:
                        print(f"{error}")
                    else:
                        valids = f""
                        for key in answers:
                            valids += f"{key}, "
                        print(f"Invalid. Expected: {valids[:-2]}")
                    break
            response.append(answers[userinput])
        if len(response) == len(userinputs) and (len(response) == size or size <= 0):
            if size != 1:
                return response
            return response[0]
        else:
            if size > 1:
                print(f"Invalid. Expecting {size} values.")
