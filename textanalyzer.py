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

    words_quantity = len(text.split())
    characters_quantity = len(text)
    characters_quantity_nospace = len(text.replace(" ", ""))
    most_used = counts.most_common(1)[0][0]
    average = characters_quantity_nospace / words_quantity

    return [words_quantity, characters_quantity, characters_quantity_nospace, most_used, average]

def space():
    print("\n"*30)

interface = Interface()
space()
interface.display_head()
print()
text = str(input(" +- text: "))
space()
interface.display_text_results(check_text(text)[0], check_text(text)[1], check_text(text)[2], check_text(text)[3], check_text(text)[4])

    


