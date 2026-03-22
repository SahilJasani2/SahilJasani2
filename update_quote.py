import random
import re

# 1. Read quotes
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# 2. Pick a random quote and format it
selected_quote = random.choice(quotes)
formatted_quote_block = f'''---

<div align="center">
  <i>"{selected_quote}"</i>
</div>

---'''

# 3. Read the current README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 4. Pattern to match the existing quote block (including the surrounding ---)
#    This pattern matches exactly the block shown in your README.
pattern = r'---\n\n<div align="center">\n  <img src="https://quotes-github-readme\.vercel\.app/api\?type=horizontal&theme=dark" alt="Programming Quote" />\n</div>\n\n---'

# 5. Replace with the new block
new_readme = re.sub(pattern, formatted_quote_block, readme, flags=re.DOTALL)

# 6. Save the updated README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(new_readme)
