import random

# 1. Read the quotes from your text file
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# 2. Pick a random quote and format it
selected_quote = random.choice(quotes)
formatted_quote = f'<div align="center">\n  <i>"{selected_quote}"</i>\n</div>'

# 3. Read the current README content
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 4. Bulletproof replacement (No Regex)
start_marker = ""
end_marker = ""

# Check if the markers actually exist to prevent errors
if start_marker in readme and end_marker in readme:
    # Split the file into everything BEFORE the start marker, and everything AFTER the end marker
    top_part = readme.split(start_marker)[0]
    bottom_part = readme.split(end_marker)[1]
    
    # Sandwich the new quote cleanly between the top and bottom parts
    new_readme = top_part + start_marker + "\n" + formatted_quote + "\n" + end_marker + bottom_part
    
    # 5. Save the updated content back to the README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
else:
    print("Error: Could not find the QUOTE_START or QUOTE_END markers in the README.")
