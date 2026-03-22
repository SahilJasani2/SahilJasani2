import random
import re

# 1. Read the quotes from your text file
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# 2. Pick a random quote and format it in HTML
selected_quote = random.choice(quotes)
formatted_quote = f'<div align="center">\n  <i>"{selected_quote}"</i>\n</div>'

# 3. Read the current README content
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 4. Strictly swap ONLY the text between the START and END markers
new_readme = re.sub(
    r'()[\s\S]*?()',
    rf'\1\n{formatted_quote}\n\2',
    readme
)

# 5. Save the updated content back to the README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
