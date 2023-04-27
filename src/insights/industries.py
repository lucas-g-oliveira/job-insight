from typing import List, Dict
import csv


def get_unique_industries(path: str) -> List[str]:
    with open(path, 'r') as file:
        data = [*csv.DictReader(file)]
    return set([ind['industry'] for ind in data if ind['industry'] != ''])


def filter_by_industry(jobs: List[Dict], industry: str) -> List[Dict]:
    """Filters a list of jobs by industry

    Parameters
    ----------
    jobs : list
        List of jobs to be filtered
    industry : str
        Industry for the list filter

    Returns
    -------
    list
        List of jobs with provided industry
    """
    raise NotImplementedError
