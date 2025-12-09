# -Python-Program-to-Remove-Punctuation-from-a-Given-Text
⭐ Python Program to Remove Punctuation from a Given Text While working with text data, especially in Natural Language Processing (NLP) or data preprocessing, we often need to clean the text by removing punctuation marks. Python’s RE module (Regular Expressions) module provides a very simple and efficient way to do this.
Approach:

We can use the re.sub() function to replace all punctuation characters with an empty string.

The pattern r'[^\w\s]' removes everything except:

\w → alphabets, digits, and underscore
\s → whitespace
So effectively, all punctuation marks are removed.

Explanation:

re.sub(pattern, replacement, text) replaces the matched characters with the given replacement.
r'[^\w\s]' matches every character that is not:
a word character (A–Z, a–z, 0–9, _)
a whitespace
Hence, punctuation such as .,!?;:'"-()[]{}@#% is removed.

Example

Input:

Hello, world! Welcome to github.

Output:

Hello world Welcome to github

Use Cases:
Cleaning text for NLP applications.
Preparing data before sentiment analysis.
Removing noise from user input.
Preprocessing tweets, reviews, or messages.
Conclusion:

Removing punctuation is an essential preprocessing step in many text-based applications. Using Python’s RE module, this task becomes simple, powerful, and efficient.
