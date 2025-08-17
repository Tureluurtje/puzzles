import yaml
import json

def yaml_to_json(yaml_file, json_file):


    with open(yaml_file, 'r') as yf:
        yaml_content = yaml.safe_load(yf)

    if not isinstance(yaml_content, dict):
        raise ValueError("YAML root must be a dictionary of word: clue pairs.")
    with open(json_file, 'w') as jf:
        json.dump(
            {
                "solution_phrases": ['tijdschakelaar'],
                "puzzle_entries": [
                    {"word": word, "clue": clue}
                    for word, clue in yaml_content.items()
                ]
            },
            jf,
            indent=4
        )
        

def remove_duplicates_from_yaml(yaml_file, output_file):
    try:
        with open(yaml_file, 'r') as yf:
            yaml_content = yaml.safe_load(yf)

        if not isinstance(yaml_content, dict):
            raise ValueError("YAML root must be a dictionary of word: clue pairs.")

        seen_words = set()
        seen_clues = set()
        cleaned_content = {}

        for word, clue in yaml_content.items():
            if word in seen_words or clue in seen_clues:
                continue
            seen_words.add(word)
            seen_clues.add(clue)
            cleaned_content[word] = clue

        with open(output_file, 'w') as of:
            yaml.dump(cleaned_content, of, default_flow_style=False)
    except ImportError:
        raise ImportError("Please install PyYAML to use this function: pip install pyyaml")


yaml_to_json('puzzle_entries.yaml', 'words.json')
#remove_duplicates_from_yaml('puzzle_entries.yaml', 'cleaned_puzzle_entries.yaml')