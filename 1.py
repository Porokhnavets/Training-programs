
def are_the_numbers_the_same(element):
    flag = 0
    for num in element:
        if num != element[0]:
            flag = 1
    return flag

def numbers_to_text(string,dictionary):
    new_string = ""
    for element in string:
        count = 0
        flag = are_the_numbers_the_same(element)
        if flag == 0 :
            count = len(element)-1
            if count >= len(dictionary[element[0]]):
                count %= len(dictionary[element[0]])
                new_string += dictionary[element[0]][count]
            else:
                new_string += dictionary[element[0]][count]
        else:
            new_string += ' ' +'none' + ' '
    return new_string

dictionary = {'1':['.',',','?','!',':',';','1'],
              '2':['а','б','в','г','2'],
              '3':['д','е','ж','з','3'],
              '4':['и','й','к','л','4'],
              '5':['м','н','о','п','5'],
              '6':['р','с','т','у','6'],
              '7':['ф','х','ц','ч','7'],
              '8':['ш','щ','ъ','ы','8'],
              '9':['ь','э','ю','я','9'],
              '0':[' ','0']
              }

string = str(input('Введите строку : ')).split(' ')

new_string = numbers_to_text(string,dictionary)

print(new_string)

        

