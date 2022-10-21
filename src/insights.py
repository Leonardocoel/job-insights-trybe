import src.jobs as jobs

# import jobs


def get_unique_job_types(path):
    data = jobs.read(path)
    unique_job_types_list = list(
        dict.fromkeys(row["job_type"] for row in data if row["job_type"] != "")
    )

    return unique_job_types_list


def filter_by_job_type(jobs, job_type):
    result = [job for job in jobs if job["job_type"] == job_type]
    return result


def get_unique_industries(path):
    data = jobs.read(path)
    unique_industries_list = list(
        dict.fromkeys(row["industry"] for row in data if row["industry"] != "")
    )

    return unique_industries_list


def filter_by_industry(jobs, industry):
    result = [job for job in jobs if job["industry"] == industry]

    return result


def get_max_salary(path):
    data = jobs.read(path)
    max_salary_list = max(
        int(row["max_salary"])
        for row in data
        if row["max_salary"] != "" and row["max_salary"] != "invalid"
    )

    return max_salary_list


def get_min_salary(path):
    data = jobs.read(path)
    min_salary_list = min(
        int(row["min_salary"])
        for row in data
        if row["min_salary"] != "" and row["min_salary"] != "invalid"
    )

    return min_salary_list


def matches_salary_range(job, salary):
    if (
        "min_salary" not in job
        or "max_salary" not in job
        or type(job["min_salary"]) is not int
        or type(job["max_salary"]) is not int
        or type(salary) is not int
        or job["min_salary"] > job["max_salary"]
    ):
        raise ValueError()

    return job["min_salary"] <= salary <= job["max_salary"]


def filter_by_salary_range(jobs, salary):
    result = []
    for job in jobs:
        try:
            if matches_salary_range(job, salary) is True:
                result.append(job)
        except ValueError:
            pass

    return result
