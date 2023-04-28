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
                ''
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
                ''
        return minValue


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    """Checks if a given salary is in the salary range of a given job

    Parameters
    ----------
    job : dict
        The job with `min_salary` and `max_salary` keys
    salary : int
        The salary to check if matches with salary range of the job

    Returns
    -------
    bool
        True if the salary is in the salary range of the job, False otherwise

    Raises
    ------
    ValueError
        If `job["min_salary"]` or `job["max_salary"]` doesn't exists
        If `job["min_salary"]` or `job["max_salary"]` aren't valid integers
        If `job["min_salary"]` is greather than `job["max_salary"]`
        If `salary` isn't a valid integer
    """
    raise NotImplementedError


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
