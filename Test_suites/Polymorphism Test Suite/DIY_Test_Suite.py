#This creates the United States Class
class unitedStates:
    #defines the variables for capital, language, and gdp
    def __init__(item, capital, language, GDP):
        item.capital = capital
        item.language = language 
        item.GDP = GDP
    
    #defines the capital function
    def cap(item):
        print(f"The United States' capital is {item.capital}")
        return item.capital

    #defines the language function
    def lang(item):
        print(f"The United States' primary language is {item.language}")
        return item.language

    #defines the gdp function
    def gdp(item):
        print(f"The United States' GDP is {item.GDP}")
        return item.GDP

#This creates the Germany Class
class germany:
    #defines the variables for capital, language, and gdp
    def __init__(item, capital, language, GDP):
        item.capital = capital
        item.language = language
        item.GDP = GDP
    
    #defines the capital function
    def cap(item):
        print(f"Germany's capital is {item.capital}")
        return item.capital

    #defines the language function
    def lang(item):
        print(f"Germany's primary language is {item.language}")
        return item.language

     #defines the gdp function
    def gdp(item):
        print(f"Germany's GDP is {item.GDP}")
        return item.GDP

def test1():
    print("Test 1:")
    #sets the values for the United States class
    USA = unitedStates("Capital1", "Language1", "GDP1")

    #sets the values for the Germany class
    GER = germany("Capital2", "Language2", "GDP2")

    i = 0
    testcases = [("Capital1", "Language1", "GDP1"), ("Capital2", "Language2", "GDP2")]
    flag = True
    for country in (USA, GER):
        a = country.cap()
        b = country.lang()
        c = country.gdp()
        #print(a)
        #print(b)
        #print(c)
        #print(testcases[i])
        #print((a,b,c))
        if(testcases[i] != (a,b,c)):
            flag = False
        i = i + 1
    
    if(flag == True):
        print("Pass")
    else:
        print("Fail")

test1()