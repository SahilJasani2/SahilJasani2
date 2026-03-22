import random
import re

# 1. Read quotes from the file
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# 2. Pick a random quote and format the new block
selected_quote = random.choice(quotes)
new_quote_block = f'''<!-- QUOTE START -->
<div align="center">
  <i>{selected_quote}</i>
</div>
<!-- QUOTE END -->'''

# 3. Read the current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 4. Pattern to match everything between the markers (including the markers themselves)
pattern = r'<!-- QUOTE START -->.*?<!-- QUOTE END -->'

# 5. Replace with the new block (using re.DOTALL to match across lines)
new_readme = re.sub(pattern, new_quote_block, readme, flags=re.DOTALL)

# 6. Save the updated README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
