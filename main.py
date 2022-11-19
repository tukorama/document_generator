import pandas as pd
import sys
import jinja2
import os


if __name__ == "__main__":

    template_file : str = sys.argv[1]
    data_csv : str = sys.argv[2]

    template_loader = jinja2.FileSystemLoader(searchpath="./")
    template_env = jinja2.Environment(loader=template_loader)
    template = template_env.get_template(template_file)

    data = pd.read_csv(data_csv).to_dict(orient='records')

    if not os.path.exists("./output"):
        os.makedirs("output")

    for d in data:
        output = template.render(d)
        with open(f"./output/{list(d.values())[0]}.xml", 'wb') as file:
            file.write(output.encode("utf-8"))



