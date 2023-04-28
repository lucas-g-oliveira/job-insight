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


def is_valid(value):
    return str(value).isdigit()


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    if not is_valid(salary):
        raise ValueError()
    values = []
    for data in job:
        max = data["max_salary"]
        min = data["min_salary"]
        if not is_valid(max) or not is_valid(min):
            raise ValueError()
        elif float(min) >= float(max):
            raise ValueError()
        else:
            values.append({max: int(max), min: int(min)})
    return all(
        [
            value["max_salary"] <= salary <= value["min_salary"]
            for value in values
        ]
    )


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
