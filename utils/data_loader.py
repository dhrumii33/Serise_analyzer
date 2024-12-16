from glob import glob 
import pandas as pd
import pathlib

def load_subtitles_dataset(dataset_path):
    # Convert to Path object correctly
    dataset_path = pathlib.Path(dataset_path)
    subtitles_paths = list(dataset_path.glob('*.ass'))

    scripts = []
    episode_num = []

    for path in subtitles_paths:
        with open(path, 'r', encoding='utf-8') as file:
            lines = file.readlines()
            lines = lines[27:]
            lines = [",".join(line.split(',')[9:]) for line in lines]
        
        lines = [line.replace('\\N',' ') for line in lines]
        script = " ".join(lines)

        episode = int(str(path).split('-')[-1].split('.')[0].strip())

        scripts.append(script)
        episode_num.append(episode)

    df = pd.DataFrame.from_dict({"episode":episode_num, "script":scripts})
    return df