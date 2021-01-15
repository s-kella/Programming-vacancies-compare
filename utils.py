def data_to_table(info_about_language, vacancies_in_list):
    if len(vacancies_in_list) == 0:
        vacancies_in_list.append(header_table)
    dict_to_list = []
    for item in info_about_language:
        dict_to_list.append(info_about_language[item])
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
header_table = ['language', 'vacancies found', 'vacancies processed', 'skipped', 'average salary']