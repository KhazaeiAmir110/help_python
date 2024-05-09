from jinja2 import Environment, FileSystemLoader, select_autoescape
import data

env = Environment(
    loader=FileSystemLoader('./templates'),
    autoescape=select_autoescape()
)

template = env.get_template('index.html')


content = data.content

print(template.render(**content))