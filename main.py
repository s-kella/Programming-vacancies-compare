import superjob
import headhunter
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    languages = {
        'JavaScript': 0,
        'Java': 0,
        'python': 0,
        'ruby': 0,
        'PHP': 0,
        'c++': 0,
        'c#': 0,
        'c': 0,
        'go': 0,
        'Objective-C': 0,
        'Scala': 0,
        'Swift': 0,
        'TypeScript': 0
    }
    key_sj = os.getenv("SUPERJOB_KEY")
    print(superjob.get_data_sj(key_sj, languages))
    print(headhunter.get_data_hh(languages))






