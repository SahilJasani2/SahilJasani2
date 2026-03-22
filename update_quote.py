import random

# 1. Read the quotes from your text file
with open('quotes.txt', 'r', encoding='utf-8') as f:
    quotes = [line.strip() for line in f if line.strip()]

# Check if quotes exist just in case
if not quotes:
    print("Error: quotes.txt is empty!")
    exit(1)

# Pick a random quote and format it
selected_quote = random.choice(quotes)
formatted_quote = f'<div align="center">\n  <i>"{selected_quote}"</i>\n</div>'

# 2. Read the current README content
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# 3. Find exactly where the markers start and end using precise indices
start_marker = ""
end_marker = ""

start_idx = readme.find(start_marker)
end_idx = readme.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Calculate exactly where the end marker finishes
    end_marker_end_idx = end_idx + len(end_marker)
    
    # Slice the file: keep everything before START, and everything after END
    top_part = readme[:start_idx]
    bottom_part = readme[end_marker_end_idx:]
    
    # Rebuild the file securely
    new_readme = top_part + start_marker + "\n" + formatted_quote + "\n" + end_marker + bottom_part
    
    # 4. Save the updated content back to the README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(new_readme)
        
    print("Successfully updated the quote!")
else:
    print("Error: Could not find the QUOTE_START or QUOTE_END markers in the README.")
    exit(1)
