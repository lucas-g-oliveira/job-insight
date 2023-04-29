from typing import Union, List, Dict
import csv


def get_max_salary(path: str) -> int:
    with open(path, "r") as file:
        data = [*csv.DictReader(file)]
        sal = [val["max_salary"] for val in data if val["max_salary"] != ""]
        maxValue = 0
        for value in sal:
            try:
                if int(value) > maxValue:
                    maxValue = int(value)
            except ValueError:
                """"""
        return maxValue


def get_min_salary(path: str) -> int:
    maxSalary = 10000000000000000000
    with open(path, "r") as file:
        data = [*csv.DictReader(file)]
        sal = [val["min_salary"] for val in data if val["min_salary"] != ""]
        minValue = maxSalary
        for value in sal:
            try:
                if int(value) < minValue:
                    minValue = int(value)
            except ValueError:
                """"""
        return minValue


def is_valid(param):
    not_none = param is not None  # que existe
    valid_value = str(param).lstrip("-").isnumeric()  # que é valido
    return all([not_none, valid_value])


def to_int(param):
    try:
        return int(str(param))
    except ValueError('caiu no int'):
        """"""


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    max = 'max_salary'
    min = 'min_salary'
    try:
        sl = int(salary)
        mx = int(job[max])
        mn = int(job[min])
        if mn > mx:
            raise ValueError('salary_min cannot be greater than salary_max')
    except (ValueError, TypeError, KeyError):
        raise ValueError('cannot convert')
    return mn <= sl <= mx


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    """Filters a list of jobs by salary range

    Parameters
    ----------
    jobs : list
        The jobs to be filtered
    salary : int
        The salary to be used as filter

    Returns
    -------
    list
        Jobs whose salary range contains `salary`
    """
    raise NotImplementedError
