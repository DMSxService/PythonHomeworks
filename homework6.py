my_dict = { 'Константин' : 1973, 'Александр' : 1995, 'Алина' : 1976}
print('Dict:',my_dict)
print('Existing value:',my_dict['Александр'])
print('Not existing value:',my_dict.get('Сергей', "Пациент в списке отсутсвует"))
my_dict.update({'Олег': 1970,
                'Светлана': 1986})
one_key = my_dict.pop('Алина')
print('Deleted value:',one_key)
print('Modified dictionary:',my_dict)
my_set = {12,12,2,2,3, 7.4,8,7.4, True, False, 'sky'}
print('Set:',my_set)
my_set.add(15)
my_set.add((17,19))
my_set.remove(7.4)
print('Modified set:',my_set)