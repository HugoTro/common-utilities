from collections import Counter

MAX_N_CHARS = 5
N_MOST_USED = 10

def remove_chars(original: str, to_remove: str | list[str]) -> str:
	ret_str = ''
	for c in original:
		if c not in to_remove:
			ret_str += c
	return ret_str

def main() -> None:
	text_input = input('Paste text to count: ')
	split_text = text_input.split()
	n_chars_punct = len("".join(split_text))
	for i in range(len(split_text)):
		split_text[i] = split_text[i].strip(',.').lower()
	n_chars = len("".join(split_text))

	word_counts = [0 for i in range(MAX_N_CHARS+1)]
	count = Counter()
	count.update(split_text)
	for word in split_text:
		for i in range(MAX_N_CHARS+1):
			if len(word)>i:
				word_counts[i] += 1


	print('Text stats:')
	print(f'\tNumber of characters (spaces included): {len(text_input)}')
	print(f'\tNumber of characters (letters only):')
	print(f'\t\twith punctuation: {n_chars_punct}')
	print(f'\t\twithout punctuation: {n_chars}')
	print('\tNumber of words excluding words shorter than:')
	for i in range(len(word_counts)):
		print(f'\t\t{i} chars: {word_counts[i]}')

	# order words by use frequency
	most_used = [(duo[1], duo[0]) for duo in count.items()]
	most_used.sort(key=lambda v: v[0], reverse=True)
	print('\n\tMost used words in text:')
	for i in range(N_MOST_USED):
		print(f'\t\t{i+1} - "{most_used[i][1]}" with {most_used[i][0]} uses.')

if __name__=='__main__':
	main()