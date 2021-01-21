import requests
import os
from terminaltables import SingleTable
import utils


def get_info_about_vacancy(payload, url, header):
    average = 0
    skipped = 0
    vacancies_with_salary = 0
    page = 0
    while True:
        payload['page'] = page
        response = requests.get(url, headers=header, params=payload)
        response.raise_for_status()
        vacancies = response.json()['objects']
        for vacancy in vacancies:
            if vacancy["payment_from"] != 0 and vacancy["payment_to"] != 0:
                salary = utils.predict_rub_salary(vacancy["payment_from"], vacancy["payment_to"])
                average += salary
                vacancies_with_salary += 1
            else:
                skipped += 1
        page += 1
        if len(vacancies) == 0:
            break
    if vacancies_with_salary:
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
    data_about_languages = []
    for language in utils.languages:
        payload['keywords[0][keys]'] = language
        average, skipped, vacancies_with_salary, vacancies_found = get_info_about_vacancy(payload, url, header)
        utils.languages[language] = {
            'language': language,
            'vacancies_found': vacancies_found,
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average,
        }
        data_about_languages = utils.join_data_for_table(utils.languages[language], data_about_languages)
    return SingleTable(data_about_languages, 'SuperJob Moscow').table
