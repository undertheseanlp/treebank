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
            ann_file.write(u"T%d\tToken %d %d\t%s\n" % (token_id, start, end, tag))
            token_id += 1
            start = end + 1


if __name__ == '__main__':
    input_file = join(dirname(__file__), "raw", "vinews", "21395276.txt")
    output_folder = join(dirname(__file__), "brat")
    auto_annotation(input_file, output_folder)
