template = []
with open('README.md', 'r') as myfile:
    template=myfile.read()
    print(template)

data = []
with open('./data/data.json', 'r') as myfile:
    data=myfile.read()
    print(data)


output = template.replace('---mark---', data)
file = open('./data/out.md','w')
file.write(output)
file.close()