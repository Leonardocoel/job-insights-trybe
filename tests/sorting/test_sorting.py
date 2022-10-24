from src.sorting import sort_by


jobs = [
    {
        "min_salary": 1000,
        "max_salary": 3000,
        "date_posted": "2020-05-07",
    },
    {
        "min_salary": 3000,
        "max_salary": 10000,
        "date_posted": "2020-05-02",
    },
    {
        "min_salary": 2000,
        "max_salary": 5000,
        "date_posted": "2020-12-02",
    },
]

jobs_mock = [
    [
        {
            "min_salary": 1000,
            "max_salary": 3000,
            "date_posted": "2020-05-07",
        },
        {
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": "2020-12-02",
        },
        {
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2020-05-02",
        },
    ],
    [
        {
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2020-05-02",
        },
        {
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": "2020-12-02",
        },
        {
            "min_salary": 1000,
            "max_salary": 3000,
            "date_posted": "2020-05-07",
        },
    ],
    [
        {
            "min_salary": 2000,
            "max_salary": 5000,
            "date_posted": "2020-12-02",
        },
        {
            "min_salary": 1000,
            "max_salary": 3000,
            "date_posted": "2020-05-07",
        },
        {
            "min_salary": 3000,
            "max_salary": 10000,
            "date_posted": "2020-05-02",
        },
    ],
]


def test_sort_by_criteria():
    criterias = ["min_salary", "max_salary", "date_posted"]

    for i in range(len(criterias)):
        sort_by(jobs, criterias[i])
        assert jobs == jobs_mock[i]
