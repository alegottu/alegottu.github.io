from markdown import Markdown
from jinja2 import Environment, FileSystemLoader
from pathlib import Path
import json

def run():
    template_env = Environment(loader=FileSystemLoader(searchpath='./'))
    template = template_env.get_template('postlayout.html')

    pathlist = Path('_posts').glob('*.md')
    posts = dict()
    for file in pathlist:
        md = Markdown(extensions=['meta'])
        post = md.convert(file.read_text())
        posts[post] = md.Meta

    for post, config in posts.items():
        with open(f"posts/{config['file'][0]}.html", 'w') as output:
            output.write(
                template.render(
                    title=config['title'][0],
                    date=config['date'][0],
                    excerpt=config['excerpt'][0],
                    post=post
                )
            )

    template = template_env.get_template('bloglayout.html')
    listitems = ''
    for post, config in posts.items():
        listitems += f"<li><a href='posts/{config['file'][0]}.html'>{config['title'][0]}: {config['date'][0]}</a></li>\n"

    with open(f"projects.html", 'w') as output:
        output.write(
            template.render(
                items=listitems
            )
        )

if __name__ == "__main__":
    run()
