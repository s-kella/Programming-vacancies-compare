import requests
from terminaltables import SingleTable
from utils import data_to_table, languages


def predict_rub_salary_hh(salary):
    if salary['from'] != None and salary['to'] != None:
        predict = (salary['from'] + salary['to'])/2
    elif salary['from'] is None:
        predict = salary['to'] * 0.8
    elif salary['to'] is  None:
        predict = salary['from'] * 1.2
    return predict


def get_info_about_vacancy(payload, url, language):
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
    vacancies_found = response.json()['found']
    return average, skipped, vacancies_found, vacancies_with_salary


def find_on_hh():
    url = 'https://api.hh.ru/vacancies/'
    payload = {
        'area': '1',
        'period': '30',
        'text': 'программист'
    }

    vacancies_in_list = []
    for language in languages:
        average, skipped, vacancies_found, vacancies_with_salary = get_info_about_vacancy(payload, url, language)
        languages[language] = {
            'language': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average
        }
        data_to_table(languages[language], vacancies_in_list)
    return SingleTable(vacancies_in_list, 'HeadHunter Moscow').table
