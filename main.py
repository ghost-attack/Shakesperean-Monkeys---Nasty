import string
import random
import enchant

# dictionary of english words
d = enchant.Dict("en_US")

def generate_random_word(length):
    # generate a random word of a certain length
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))

def generate_string():

    # words can be between 1 and 20 letters
    # some word lengths are also more likely than others (source: English language)
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
    weights = [1, 2, 3, 4, 5, 5, 5, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    lengths = random.choices(numbers, weights=weights, k=3)

    # generate three random words of different lengths
    blank1 = generate_random_word(lengths[0])
    blank2 = generate_random_word(lengths[1])
    blank3 = generate_random_word(lengths[2])

    return "She " + blank1 + " on my " + blank2 + " until I " + blank3 + "."

def main():
    try:
        user_input = input("How many sentences should the monkeys generate?")
        number_of_sentences = int(user_input)
    except ValueError:
        print("Please enter an integer value.")

    if (number_of_sentences > 10000):
        print("This will cook your computer btw.")

    found = False

    # generate random sentences, based on the input from the user
    for _ in range (number_of_sentences):
        print_string = True
        random_string = generate_string()
        words = random_string.split()
        # if all words in the sentence are English words, print
        for word in words:
            if (not d.check(word)):
                print_string = False
                break
        if (print_string):
            found = True
            with open("saved_sentences.txt", "a") as file:
                file.write(random_string + "\n")
            print(random_string)

    if (not found):
        print("Sorry. Monkeys could not generate a comprehensible sentence. :(")

if __name__ == "__main__":
    main()