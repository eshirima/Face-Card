from parse_rest.datatypes import Object as ParseObject
from parse_rest.connection import register

def getParseProfile():

    APPLICATION_ID = "qDhmrRCHGBWBI8lO1WcSvuN6wO0xthwIgDYHjurj"
    REST_API_KEY = "CEnjtpu3TqH2PlUkKAlDOnzNktELtVjw4c6A2XYb"
    MASTER_KEY = "hglyfhRqtj9xwcY33QMBEyX8Uhy24WOsWdyOJAYf"
    
    register(APPLICATION_ID, REST_API_KEY)
    
    class KentScan(ParseObject):
        pass
    
    all_profiles = KentScan.Query.all()
    lis = []
    for a in all_profiles:
        dic = {}
        if (hasattr(a, 'firstName') and (hasattr(a, 'lastName') ) ):
            dic['name'] = a.firstName + ' ' + a.lastName
        else:
            dic['name'] = ""
        if (hasattr(a, 'emailAddress')):
            dic['email'] = a.emailAddress
        else:
            dic['email'] = ""
        if (hasattr(a, 'age')):
            dic['age'] = a.age
        else:
            dic['age'] = ""
        lis.append(dic)
    return lis

if __name__ == "__main__":
    print getParseProfile()
    
