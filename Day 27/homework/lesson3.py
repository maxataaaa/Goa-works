def capitalize_first_letter(sentence):
    words = sentence.split()  # გამოვყენოთ split() ფუნქცია სიტყვების გაყოფისთვის
    capitalized_sentence = ""
    for word in words:
        capitalized_word = word.capitalize()  # სიტყვის დიდი პირველი ასო
        capitalized_sentence += capitalized_word + " "
    return capitalized_sentence.strip()

input_sentence = "hello, this is goa"
result = capitalize_first_letter(input_sentence)
print(result)