sentence = input('Enter a phrase: ').strip()
sentence = sentence.replace(' ', '').lower()
reversed_sentence = sentence[::-1]
print(f'The inverse of "{sentence}" is "{reversed_sentence}"')
print(f'That\'s why the typed sentence is', end=' ')
if sentence != reversed_sentence:
    print('NOT', end=' ')
print('a palindrome')
