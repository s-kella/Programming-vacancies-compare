import superjob
import headhunter
import os
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    languages = ['JavaScript', 'Java', 'python', 'ruby', 'PHP', 'c++', 'c#', 'c', 'go', 'Objective-C', 'Scala', 'Swift', 'TypeScript']
    key_sj = os.getenv("SUPERJOB_KEY")
    print(superjob.get_data_sj(key_sj, languages))
    print(headhunter.get_data_hh(languages))






