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


def matches_salary_range(job: Dict, salary: Union[int, str]) -> bool:
    try:
        sl = int(salary)
        mx = int(job["max_salary"])
        mn = int(job["min_salary"])
        if mn > mx:
            raise ValueError("salary_min cannot be greater than salary_max")
    except Exception:
        raise ValueError("cannot convert all values to integer")
    return mn <= sl <= mx


def filter_by_salary_range(
    jobs: List[dict], salary: Union[str, int]
) -> List[Dict]:
    valids = []
    for job in jobs:
        try:
            if matches_salary_range(job=job, salary=salary):
                valids.append(job)
        except Exception:
            ''
    return valids
