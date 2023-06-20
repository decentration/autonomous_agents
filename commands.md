
# Commands

To merge files in a directory into one file:

```
find . -type f ! -name 'merged.txt' \( -name '*.py' -o -name '*.md' \) -exec echo -e '\n==== {} ====' \; -exec cat {} \; -exec echo \; > merged.txt

```

To merge files from a directory and get the name of the directory and append to file name:

```
dir=$(basename $(pwd)); find . -type f ! -name "${dir}_merged.py" \( -name '*.py' -o -name '*.md' \) -exec echo '""""==== {} ====""" ' \; -exec cat {} \; -exec echo \; > "${dir}_merged.py"

```
