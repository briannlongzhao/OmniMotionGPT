import os
import json
from tqdm import tqdm
from spacy import load
NLP = load("en_core_web_sm")

texts_dir = "/viscam/projects/animal_motion/briannlz/motion-diffusion-model/dataset/HumanML3D/texts"
json_path = "./subjects.json"


def find_subject(text):
    doc = NLP(text)
    subjects = [tok for tok in doc if "subj" in tok.dep_]
    return subjects


if __name__ == "__main__":
    all_subjects = {}
    for text_file in tqdm(os.listdir(texts_dir)):
        if not text_file.endswith(".txt"):
            continue
        text_id = text_file.replace(".txt", '')
        text_file_path = os.path.join(texts_dir, text_file)
        with open(text_file_path, 'r') as f:
            lines = f.readlines()
        file_subjects = []
        for line in lines:
            line = line.split('#')[0].strip()
            if len(line) == 0:
                continue
            subjects = find_subject(line)
            file_subjects.append(str(subjects))
        all_subjects[text_id] = file_subjects
    with open(json_path, 'w') as json_file:
        json.dump(all_subjects, json_file, indent=4)


