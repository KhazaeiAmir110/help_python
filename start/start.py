from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape()
)

template = env.get_template('index.html')

content = {
    'name':'Amir',
    'age':20,
    'list':[1,2,3,4,5,6,7,8,9],
    'dict':[
        {'name':'John', 'age':12},
        {'name':'Aer', 'age':23},
        {'name':'Jan', 'age':19},
        {'name':'are', 'age':40},
        {'name':'John', 'age':42},
    ]
}

print(template.render(**content))