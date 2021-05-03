def alphabet_position(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    i = 1
    alpha_dict = {}
    string_num = [x for x in text.lower() if x in alphabet]

    for x in range(len(alphabet)):
        alpha_dict[alphabet[x]] = i
        i += 1

    return ' '.join([str(alpha_dict[string_num[z]]) for z in range(len(string_num)) if string_num[z] in alpha_dict])
