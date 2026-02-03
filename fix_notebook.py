import json

with open('lab-001.ipynb', 'r') as f:
    nb = json.load(f)

# Fix cell 2 (index 1) and cell 4 (index 3) to use python instead of java
for idx in [1, 3]:
    if 'vscode' not in nb['cells'][idx]['metadata']:
        nb['cells'][idx]['metadata']['vscode'] = {}
    nb['cells'][idx]['metadata']['vscode']['languageId'] = 'python'

with open('lab-001.ipynb', 'w') as f:
    json.dump(nb, f, indent=2)

# Verify the fix
print("Verification - Cell Languages:")
for i in range(len(nb['cells'])):
    lang = nb['cells'][i]['metadata'].get('vscode', {}).get('languageId', 'N/A')
    print(f"Cell {i+1}: {lang}")
