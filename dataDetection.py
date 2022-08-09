import re

dateRegex = re.compile(r'''(
    ([0]{1}[0-9]{1}|[1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})                # DD
    (\/)                                                            # Separator
    ([0]{1}[0-9]{1}|[1]{1}[0-2]{1})                                 # MM
    (\/)                                                            # Separator
    ([1000-2999]{4})                                                # YYYY

)''', re.VERBOSE)


stringVar = 'The date is 31/01/1012'

day = dateRegex.search(stringVar).group(2)
month = dateRegex.search(stringVar).group(4)
year = dateRegex.search(stringVar).group(6)

print(day + '\n' + month + '\n' + year)

##############################################################
print()
##############################################################

dateRegex = re.compile(r'([0]{1}[0-9]{1}|[1-2]{1}[0-9]{1}|[3]{1}[0-1]{1})(\/)([0]{1}[0-9]{1}|[1]{1}[0-2]{1})(\/)([1000-2999]{4})')

stringVar = 'The date is 31/01/1012'

day = dateRegex.search(stringVar).group(1)
month = dateRegex.search(stringVar).group(3)
year = dateRegex.search(stringVar).group(5)

print(day + '\n' + month + '\n' + year)