import yaml
from jinja2 import Environment, FileSystemLoader

# Load the YAML data
with open('home.yaml', 'r') as file:
    yaml_data = yaml.safe_load(file)

# Create a Jinja2 environment and load the template file
env = Environment(loader=FileSystemLoader('.'))
template = env.get_template('template.html')

# Render the template with the loaded YAML data
rendered_html = template.render(yaml_data)

# Write the rendered HTML to a file
with open('home.html', 'w') as file:
    file.write(rendered_html)