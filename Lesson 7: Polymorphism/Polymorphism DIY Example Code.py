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

    #defines the language function
    def lang(item):
        print(f"The United States' primary language is {item.language}")

    #defines the gdp function
    def gdp(item):
        print(f"The United States' GDP is {item.GDP}")

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

    #defines the language function
    def lang(item):
        print(f"Germany's primary language is {item.language}")

     #defines the gdp function
    def gdp(item):
        print(f"Germany's GDP is {item.GDP}")

#sets the values for the United States class
USA = unitedStates("Washington D.C.", "English", "$20.94 Trillion")

#sets the values for the Germany class
GER = germany("Berlin", "German", "$3.806 Trillion")

#calls the functions for each class
for country in (USA, GER):
    country.cap()
    country.lang()
    country.gdp()
