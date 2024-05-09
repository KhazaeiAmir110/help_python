from jinja2 import Environment, FileSystemLoader, select_autoescape
import data

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape()
)

template = env.get_template('index.html')
template_person = env.get_template('persons.html')


content = data.content

print(template.render(**content))
# print(template_person.render(**content))