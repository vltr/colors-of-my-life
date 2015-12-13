# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import os
import json

from mako.template import Template


def create_class_name(name):
    return name.strip('$').strip('@').strip('_').strip(' ')

def main():
    if not os.path.isdir('./build'):
        os.mkdir('./build')
    with open('colors.json', 'r') as f:
        colors = json.loads(f.read()).get('colors')
    new_colors = []
    for c in colors:
        c['class_name'] = create_class_name(c.get('name'))
        new_colors.append(c)
    css_template = Template(filename='./base.css')
    css_dest = os.path.join('./build', 'generated.css')
    if os.path.isfile(css_dest):
        os.remove(css_dest)
    with open(css_dest, 'w') as f:
        f.write(css_template.render(colors=colors))
    html_template = Template(filename='./base.html')
    html_dest = os.path.join('./build', 'index.html')
    if os.path.isfile(html_dest):
        os.remove(html_dest)
    with open(html_dest, 'w') as f:
        f.write(html_template.render(colors=colors))
    print('done?')


if __name__ == '__main__':
    main()
