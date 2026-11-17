from collections import Counter

class Interface:
    def __init__(self):
        self.interface_size = 40

    def display_head(self):
        print("+" + "-"*self.interface_size + "+")
        print("| " + " "*(self.interface_size-2) + " |")
        print(f"| {'TEXT ANALYZER':^{self.interface_size-2}} |")
        print("| " + " "*(self.interface_size-2) + " |")
        print("+" + "-"*self.interface_size + "+")

    def display_text_results(self, words, characters, characters_no_space, most_used, average_word):
        self.display_head()
        print("| " + " "*(self.interface_size-2) + " |")
        print(f"| {f'Words: {words}':<{self.interface_size-2}} |")
        print(f"| {f'Characters: {characters}':<{self.interface_size-2}} |")
        print(f"| {f'Characters (no space): {characters_no_space}':<{self.interface_size-2}} |")
        print(f"| {f'Most used word: {most_used}':<{self.interface_size-2}} |")
        print(f"| {f'Average word lenght: {average_word:.1f}':<{self.interface_size-2}} |")
        print("| " + " "*(self.interface_size-2) + " |")
        print("+" + "-"*self.interface_size + "+")
        print()
        input("...")

def check_text(text):
    counts = Counter(text.split())

    # gets the words count
    words_quantity = len(text.split())
    # characters count
    characters_quantity = len(text)
    # characters count without space
    characters_quantity_nospace = len(text.replace(" ", ""))
    # most used words
    most_used = counts.most_common(1)[0][0]
    # calc the word size average
    average = characters_quantity_nospace / words_quantity

    return [words_quantity, characters_quantity, characters_quantity_nospace, most_used, average]

def space():
    print("\n"*30)

# instancing interface
interface = Interface()
space()
interface.display_head()
print()

# get text
text = str(input(" +- text: "))
space()

checked_text_result = check_text(text)

# display the result, function returns a list with the parameters
interface.display_text_results(checked_text_result[0], checked_text_result[1], checked_text_result[2], checked_text_result[3], checked_text_result[4])

    


