from pathlib import Path

# List all .txt files recursively
txt_files = list(Path('.').rglob("*.txt"))

print("\n.txt files recursively:")
for file in txt_files:
    print(file)

print("one remote change")
print("another dev changed this remote repo")
