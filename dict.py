dictionary = {'city': 'Москва', 'temperature': '20'}
print(dictionary['city'])
dictionary['temperature'] =int(dictionary['temperature']) - 5
print(dictionary)
print(dictionary.get('country', 'Россия'))
dictionary["date"] = '27.05.2019'
print(dictionary)

