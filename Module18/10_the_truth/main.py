import string

coded_text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'


# возвращает строку со сдвигом
def caesar_cipher(coded_string, shift_symbol):
    english_alphabet = string.ascii_lowercase + string.ascii_uppercase
    result = []
    length_1 = len(english_alphabet)
    length_2 = len(string.punctuation)
    for symbol in coded_string:
        if symbol in english_alphabet:  # переставляем буквы
            index = (english_alphabet.index(symbol) + shift_symbol) % length_1
            coded_symbol = english_alphabet[index]
        elif symbol in string.punctuation:  # переставляем символы
            index = (string.punctuation.index(symbol) + shift_symbol) % length_2
            coded_symbol = string.punctuation[index]
        else:
            coded_symbol = symbol
        result.append(coded_symbol)
    return result


decoded_text = caesar_cipher(coded_text, -1)  # осуществляем сдвиг на 1 влево
decoded_text = ''.join(decoded_text)  # преобразуем в строку

shift_in_line = 3  # стартовый сдвиг в словах
decoded_text = decoded_text.split()  # разбиваем на слова
new_decoded_word = []  # дешифрованный текст

for word in decoded_text:
    shift = shift_in_line % len(word)
    new_decoded_word.append(word[-shift:] + word[:-shift])
    if '.' in word:
        shift_in_line += 1
        new_decoded_word.append('\n')  # для форматирования

new_decoded_word = ' '.join(new_decoded_word)  # склеиваем в текст

print(new_decoded_word)
