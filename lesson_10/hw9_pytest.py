
def certain_user_added_to_0_people_records(records, user):
    records.insert(0, user)
    return records


def swap_users(records, index1, index2):
    records[index1], records[index2] = records[index2], records[index1]
    return records


def all_people_age_30_or_more_by_indexes(records, indexes):
    subset_records = [records[i] for i in indexes]
    if all(person[2] >= 30 for person in subset_records):
        answer = f'All people in modified list with records indexes {indexes} have age >=30'
    else:
        answer = f'Not all people in modified list with records indexes {indexes} have age >=30'
    return answer


def sum_el_array(array):
    summ_numbers = []
    for string in array:
        try:
            string_parts = string.split(',')
            res = sum([int(part) for part in string_parts])
        except (ValueError, AttributeError):
            res = '"Не можу це зробити"'
        finally:
            summ_numbers.append(res)
    return summ_numbers


def find_substring(string1, string2):
    return string1.find(string2)