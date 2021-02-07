def join_data_for_table(info_about_language, data_about_languages):
    if not data_about_languages:
        data_about_languages.append(header_table)
    data_about_languages.append([info_about_language[header] for header in info_about_language])
    return data_about_languages


def predict_rub_salary(frm, to):
    if frm and to:
        predict = (frm + to)/2
    elif not frm:
        predict = to * 0.8
    elif not to:
        predict = frm * 1.2
    return predict


header_table = ['language', 'vacancies found', 'vacancies processed', 'skipped', 'average salary']
