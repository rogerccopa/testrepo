from pathlib import Path

# List only files in the current directory
files = [f for f in Path('.').iterdir() if f.is_file()]

print("Files in current directory:")
for file in files:
    print(file)

print("\nFiles in 'src' directory:")
print("another test lien")
