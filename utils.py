from terminaltables import SingleTable
import copy


def predict_rub_salary(frm, to):
    if frm and to:
        predict = (frm + to)/2
    elif not frm:
        predict = to * 0.8
    elif not to:
        predict = frm * 1.2
    return predict


def make_a_table(all_lang_stat, title):
    result = [copy.deepcopy(header_table)]
    result.extend(all_lang_stat)
    table = SingleTable(result, title).table
    return table


header_table = ['language', 'vacancies found', 'vacancies processed', 'skipped', 'average salary']
