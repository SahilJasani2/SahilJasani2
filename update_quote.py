import random
import re

# 1. Read quotes from the file
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# 2. Pick a random quote and format it (inner text only)
selected_quote = random.choice(quotes)
formatted_quote = f'"{selected_quote}"'

# 3. Read the current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 4. Define regex pattern to match the entire quote block
pattern = r'(<div align="center">\n\s*<i>).*?(</i>\n</div>)'

# 5. Replace with the new quote
new_readme = re.sub(pattern, rf'\1{formatted_quote}\2', readme, flags=re.DOTALL)

# 6. Save the updated README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
