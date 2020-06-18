from jinja2 import Template
from bingo import Generar
carton = Generar()
template = Template(open('imprimir.j2').read())
print(template.render(carton=carton))