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
    vacancies = response.json()['objects']
    return vacancies, response


def get_data_sj(key, languages):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    header = {'X-Api-App-Id': key}
    payload = {'town': 'Москва',
               'catalogues': 48,
               'keywords[0][srws]': 1}
    data_about_languages = []
    for language in languages:
        payload['keywords[0][keys]'] = language
        page = 0
        average = 0
        skipped = 0
        vacancies_with_salary = 0
        while True:
            payload['page'] = page
            vacancies, response = download_vacancies(payload, url, header)
            average, skipped, vacancies_with_salary = process_vacancies(vacancies, average, vacancies_with_salary, skipped)
            page += 1
            if len(vacancies) == 0:
                break   
        if vacancies_with_salary:
            average = int(average / vacancies_with_salary)
        languages[language] = {
            'language': language,
            'vacancies_found': response.json()['total'],
            'vacancies_processed': vacancies_with_salary,
            'skipped': skipped,
            'average_salary': average,
        }
        data_about_languages = utils.join_data_for_table(languages[language], data_about_languages)
    return SingleTable(data_about_languages, 'SuperJob Moscow').table

