import requests
from terminaltables import SingleTable
import utils


def get_info_about_vacancy(payload, url, language):
    page = 0
    payload['text'] = f'программист {language}'
    average = 0
    vacancies_with_salary = 0
    skipped = 0
    pages_number = 1
    while page < pages_number:
        payload['page'] = page
        page += 1
        response = requests.get(url, params=payload)
        response.raise_for_status()
        downloaded_data = response.json()
        vacancies = downloaded_data['items']
        pages_number = downloaded_data['pages']
        for vacancy in vacancies:
            salary = vacancy['salary']
            if salary and salary['currency'] == 'RUR':
                predict = utils.predict_rub_salary(salary['from'], salary['to'])
                average += predict
                vacancies_with_salary += 1
            else:
                skipped += 1
    if vacancies_with_salary != 0:
        average = int(average / vacancies_with_salary)
    vacancies_found = downloaded_data['found']
    return average, skipped, vacancies_found, vacancies_with_salary


def get_data_hh(languages):
    url = 'https://api.hh.ru/vacancies/'
    id_region = '1'
    payload = {
        'area': id_region,
        'period': '30',
        'text': 'программист'
    }
    all_lang_stat = []
    for language in languages:
        average, skipped, vacancies_found, vacancies_with_salary = get_info_about_vacancy(payload, url, language)
        all_lang_stat.append([language, vacancies_found, vacancies_with_salary, skipped, average])
    table = utils.make_a_table(all_lang_stat)
    return table

