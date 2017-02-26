import string
#List of vowels
VOWELS = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')
#List of words which start with a silent letter
silent_letter = ('aisle','bdellium','chthonic','cnidarian','czar','gnarly','gnat','gnaw','gnome',
                 'gnomon','gnomon sundial','gnomonic','gnomonics','gnomonist','gnostic','gnosticism',
                 'gnotobiotic','gnu','heir','herb','homage','honest','honor','hour','knee','knick-knack',
                 'knight','knob','knur','knurl','mnemonic','pneumonia','pnictogen','psalm','pseudoephedrine',
                 'pseudomonas','psilophyta','psilophyte','psilotaceae','psilotales','psilotum','psittacine',
                 'psoriasis','psychiatry','psychic','psychology','psychos','psychro','psychro-active',
                 'psychro-tolerant','psychro-xerophilous','psychrometer','psychrophile','psychrophilic','psychroteuthis',
                 'psychrotrophic','ptarmigan','ptelea','pteranodon','pteria','pterion','pterodactyl','pterygium','ptosis',
                 'tmesipteris','who','wraith','wrangle','wrangler','wrangling','wrap','wrath','wrathful','wreath','wren',
                 'wrench','wrest','wrested','wrestle','wrestling','wretch','wretched','wright','wrinkle','wrist','writ',
                 'write','writhe','writing','written','wroth','wrought','wry','wryneck','under','xray')
#List of words starting with consonant sounds
consonants = ('europe','european','eustace','eunuch','eulogy','eugenics','euphemism','eucalyptus','euphony','eureka','euphoria')

def convert_word(word):
    first_vowel = -1
    t = 1
    if word!="":
        first_letter = word[0]
    else:
        return ""
    punctuation=[]
    camel_case = ""
    punct = ""
    lower_case = ""
    capital = 0
    if word != "" and word.isdigit():
        return word
    for w in word:
        if w in string.punctuation:
            punctuation.append(w)
            word = word.replace(w,"")
    punct = ''.join(str(e) for e in punctuation)
    if word!="":
        lower_case = word.lower()  #converting word to lower case to compare with the lists silent_letter or consonants
    if lower_case!="" and lower_case in silent_letter:
        return word + "yay" + punct   #if the word begins with silent letter
    if first_letter in VOWELS and lower_case not in consonants:
        return word + "yay" + punct   #if the word begins with vowel and does not begin with consonant sound
    else:
        for x in word:
            if x in VOWELS:
                if first_vowel == -1:
                    first_vowel = t   #Fetching the first vowel from the word
                    break
            t += 1
        if first_vowel!=-1:
            if word != "":
                if word[0].isupper():
                    capital = 1
            prefix = word[:first_vowel-1]   #splitting the word according to the position of the vowel
            stem = word[first_vowel-1:]
            if capital == 1:
                prefix = prefix.lower()
                if stem != "":
                    camel_case = stem[0].upper()
                return camel_case + stem [1:] + prefix + "ay" + punct   #appending the punction characters
            else:
                return camel_case + stem + prefix + "ay" + punct
        else:
            return word + "ay" + punct

def convert_sentence(sentence):
    list_of_words = sentence.split(' ')
    new_sentence = ""
    for word in list_of_words:  #Looping for each word in the given paragraph
        new_sentence = new_sentence + convert_word(word) + " "
    return new_sentence.strip() #Removing any extra spaces at the beginning and end
