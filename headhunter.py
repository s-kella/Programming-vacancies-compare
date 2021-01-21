import requests
from terminaltables import SingleTable
import utils


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
                predict = utils.predict_rub_salary(salary['from'], salary['to'])
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

    data_about_languages = []
    for language in utils.languages:
        average, skipped, vacancies_found, vacancies_with_salary = get_info_about_vacancy(payload, url, language)
        utils.languages[language] = {
            'language': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average
        }
        data_about_languages = utils.join_data_for_table(utils.languages[language], data_about_languages)
    return SingleTable(data_about_languages, 'HeadHunter Moscow').table
