import re
s = "Briefly, MCF-7 idential cells grown as described above were treated with a range of LTX-diol or iso-LTX-diol."
r = re.compile(r'([A-Z][^ ]*)(?=\s+(?:[^A-Z]\S*\s+){1,4}cells?)')

m = r.match(s)
print(m)
x = r.findall(s)
print(x)