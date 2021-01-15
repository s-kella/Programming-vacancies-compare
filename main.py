import superjob
import headhunter
from dotenv import load_dotenv


if __name__ == '__main__':
    load_dotenv()
    print(headhunter.find_on_hh())
    print(superjob.find_on_sj())





