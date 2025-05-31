import re
pattern = r"\ba\b"
# pattern2 =
text = "The crimson platypus danced gracefully" \
" beneath a sky filled with marshmallow clouds, while a confused squirrel composed jazz on a tiny, golden saxophone."
match = re.finditer(pattern,text)
for i in match:
    print(i.group(),i.span())
