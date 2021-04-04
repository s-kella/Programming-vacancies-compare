import requests
from terminaltables import SingleTable
import utils


def process_vacancies(vacancies, average, vacancies_with_salary, skipped):
    for vacancy in vacancies:
        if vacancy["payment_from"] or vacancy["payment_to"]:
            salary = utils.predict_rub_salary(vacancy["payment_from"], vacancy["payment_to"])
            average += salary
            vacancies_with_salary += 1
        else:
            skipped += 1   
    return average, skipped, vacancies_with_salary


def download_vacancies(payload, url, header):
    response = requests.get(url, headers=header, params=payload)
    response.raise_for_status()
    downloaded_data = response.json()
    vacancies = downloaded_data['objects']
    return vacancies, response, downloaded_data


def get_language_stat(language, payload, url, header):
    payload['keywords[0][keys]'] = language
    page = 0
    average = 0
    skipped = 0
    vacancies_with_salary = 0
    while True:
        payload['page'] = page
        vacancies, response, downloaded_data = download_vacancies(payload, url, header)
        average, skipped, vacancies_with_salary = process_vacancies(vacancies, average, vacancies_with_salary, skipped)
        page += 1
        if len(vacancies) == 0:
            break
    if vacancies_with_salary:
        average = int(average / vacancies_with_salary)
    return [language, downloaded_data['total'], vacancies_with_salary, skipped, average]


def get_data_sj(key, languages):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': key}
    id_field_of_work = 48
    id_in_which_block_search = 1
    all_lang_stat = []
    payload = {'town': 'Москва',
               'catalogues': id_field_of_work,
               'keywords[0][srws]': id_in_which_block_search}
    for language in languages:
        all_lang_stat.append(get_language_stat(language, payload, url, header))
    table = utils.make_a_table(all_lang_stat)
    return table

