import requests
import os
from terminaltables import SingleTable
from utils import data_to_table, languages


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


def get_info_about_vacancy(payload, url, header):
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
    vacancies_found = response.json()['total']
    return average, skipped, vacancies_with_salary, vacancies_found


def find_on_sj():
    key = os.getenv("SUPERJOB_KEY")
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': key}
    payload = {'town': 'Москва',
               'catalogues': 48,
               'keywords[0][srws]': 1}
    vacancies_in_list = []
    for language in languages:
        payload['keywords[0][keys]'] = language
        average, skipped, vacancies_with_salary, vacancies_found = get_info_about_vacancy(payload, url, header)
        languages[language] = {
            'language': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average,
        }
        data_to_table(languages[language], vacancies_in_list)
    return SingleTable(vacancies_in_list, 'SuperJob Moscow').table
