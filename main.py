def count_characters(s):
	characters = {}
	s = s.lower()
	for char in s:
		if char.isalpha() == False:
			continue
		if char in characters:
			characters[char] += 1
		else:
			characters[char] = 1
	character_list = []
	for char, count in characters.items():
		character_list.append((char, count))
	character_list.sort(key=lambda x: x[1], reverse=True)
	return character_list
	

def count_words(s):
	return len(s.split())

def print_report(word_count, character_count):
	print("--- Begin report of books/frankenstein.txt ---")
	print(f"{word_count} words found in the doucment")
	print()
	for char in character_count:
		print(f"The '{char[0]}' character was found {char[1]} times")

def main():
	with open("./books/frankenstein.txt") as f:
		file_contents = f.read()
		word_count = count_words(file_contents)
		character_count = count_characters(file_contents)
		print_report(word_count, character_count)

main()