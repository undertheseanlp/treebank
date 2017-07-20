from os import listdir
from underthesea import pos_tag, word_sent
from os.path import join, dirname, basename
import io


def auto_annotation(input_file, output_folder="."):
    file_id = basename(input_file).split(".")[0]
    texts = open(input_file).read().strip().decode("utf-8").split("\n")
    content = u"\n".join([u" ".join(word_sent(text)) for text in texts])
    output_text_file = join(output_folder, "%s.txt" % file_id)
    io.open(output_text_file, "w", encoding="utf-8").write(content)

    start = 0
    end = 0
    output_annotation_file = join(output_folder, "%s.ann" % file_id)
    ann_file = io.open(output_annotation_file, "w", encoding="utf-8", newline="\n")
    token_id = 1
    for text in texts:
        tokens = pos_tag(text)
        for token in tokens:
            word, tag = token
            end = start + len(word)
            ann_file.write(u"T%d\t%s %d %d\t%s\n" % (token_id, tag, start, end, word))
            token_id += 1
            start = end + 1
        start += 1


def get_annotated_files(brat_folder):
    files = [f[2:] for f in listdir(brat_folder) if f.startswith("p_") and f.endswith(".txt")]
    return set(files)


if __name__ == '__main__':
    folder = join(dirname(__file__), "raw", "vinews")
    files = set(listdir(folder))
    brat_folder = join(dirname(__file__), "brat")
    annotated_files = get_annotated_files(brat_folder)
    un_annotated_files = files - annotated_files
    for file in un_annotated_files:
        input_file = join(folder, file)
        output_folder = join(dirname(__file__), "brat")
        auto_annotation(input_file, output_folder)
