# Simple Palindrome check with punctuation ignored.
# This was created as a demonstration for a Quality Matters Presentation.
# There's nothing else to it!

original_text = input("Enter a word or sentence to see if it is a palindrome:\n")

filtered_text = "".join([char for char in original_text if char.isalnum()]).lower()

palindrome_check = filtered_text[::-1]

if palindrome_check == filtered_text:
    print("Yep, that's a palindrome!")
else:
    print("That's not a palindrome, sorry!")
