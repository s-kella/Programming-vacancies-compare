import requests
import os
from dotenv import load_dotenv
from terminaltables import SingleTable


def predict_rub_salary_hh(salary):
    if salary['from'] != None and salary['to'] != None:
        predict = (salary['from'] + salary['to'])/2
    elif salary['from'] is None:
        predict = salary['to'] * 0.8
    elif salary['to'] is  None:
        predict = salary['from'] * 1.2
    return predict


def predict_rub_salary_sj(vacancy):
    frm = vacancy["payment_from"]
    to = vacancy["payment_to"]
    if frm != 0 and to != 0:
        predict = (frm + to)/2
    elif frm == 0:
        predict = to * 0.8
    elif to == 0:
        predict = frm * 1.2
    return predict


def data_to_table(dict):
    dict_to_list = []
    for item in dict:
        dict_to_list.append(dict[item])
    vacancies_in_list.append(dict_to_list)


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
vacancies_in_list = [['language', 'vacancies found', 'vacancies processed', 'skipped', 'average salary']]


def hh():
    url = 'https://api.hh.ru/vacancies/'
    payload = {
        'area': '1',
        'period': '30',
        'text': 'программист'
    }

    for language in languages:
        page = 0
        if 'page' in payload:
            del payload['page']
        payload['text'] = f'программист {language}'
        response = requests.get(url, params=payload)
        response.raise_for_status()
        pages_number = response.json()['pages']
        average = 0
        vacancies_with_salary = 0
        skipped = 0
        while page < pages_number:
        #while page < 7:
            payload['page'] = page
            page += 1
            response = requests.get(url, params=payload)
            response.raise_for_status()
            vacancies = response.json()['items']
            for vacancy in vacancies:
                salary = vacancy['salary']
                if salary is not None and salary['currency'] == 'RUR':
                    predict = predict_rub_salary_hh(salary)
                    average += predict
                    vacancies_with_salary += 1
                else:
                    skipped += 1
        if vacancies_with_salary != 0:
            average = int(average / vacancies_with_salary)
        languages[language] = {
            'language': language,
            'vacancies_found': response.json()['found'],
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average
        }
        data_to_table(languages[language])
    print(SingleTable(vacancies_in_list, 'HeadHunter Moscow').table)
        #print(languages[language])


def sj():
    load_dotenv()
    key = os.getenv("SUPERJOB_KEY")
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': key}

    payload = {'town': 'Москва',
               'catalogues': 48}

    for language in languages:
        payload['keywords[0][srws]'] = 1
        payload['keywords[0][keys]'] = language
        average = 0
        skipped = 0
        vacancies_with_salary = 0
        for page in range(500):
            payload['page'] = page
            response = requests.get(url, headers=header, params=payload)
            response.raise_for_status()
            vacancies = response.json()['objects']
            if len(vacancies) == 0:
                break
            for vacancy in vacancies:
                if vacancy["payment_from"] != 0 and vacancy["payment_to"] != 0:
                    salary = predict_rub_salary_sj(vacancy)
                    average += salary
                    vacancies_with_salary += 1
                else:
                    skipped += 1
        if vacancies_with_salary != 0:
            average = int(salary / vacancies_with_salary)
        languages[language] = {
            'language': language,
            'vacancies_found': response.json()['total'],
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average,
        }
        data_to_table(languages[language])
    print(SingleTable(vacancies_in_list, 'SuperJob Moscow').table)


if __name__ == '__main__':
    hh()
    vacancies_in_list = [['language', 'vacancies found', 'vacancies processed', 'skipped', 'average salary']]
    sj()



