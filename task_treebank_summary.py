from os import listdir
from jinja2 import Template
from os.path import dirname, join


def count_sentences(treebank_folder):
    files = listdir(treebank_folder)
    files = [join(treebank_folder, file) for file in files]
    lines = [len(open(file, "r").read().strip().split("\n\n")) for file in files]
    total = sum(lines)
    return total


if __name__ == '__main__':
    current_directory = dirname(__file__)
    template = open(join(current_directory, "report.template")).read().decode("utf-8")
    template = Template(template)
    treebank_folder = join(current_directory, "treebank")
    num_documents = len(listdir(treebank_folder))
    num_sentences = count_sentences(treebank_folder)
    content = template.render(num_documents=num_documents, num_sentences=num_sentences)
    report_file = join(current_directory, "README.md")
    open(report_file, "w").write(content.encode("utf-8"))
