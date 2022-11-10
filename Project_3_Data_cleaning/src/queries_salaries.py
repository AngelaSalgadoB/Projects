best_payed_titles_query2 = """
SELECT 
    title, 
    AVG(base_salary) 'average_salary'
FROM
    salaries
GROUP BY title DESC
ORDER BY AVG(base_salary) DESC;
    """


best_salaries_in_company = """
SELECT 
    company, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
GROUP BY company
ORDER BY AVG(base_salary) DESC;
    """

gender_male_best_salaries_in_company = """
SELECT 
    company,
    gender, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Male'
GROUP BY company
ORDER BY AVG(base_salary) DESC;
    """

gender_male_female_best_salaries_in_company = """
SELECT 
    company,
    gender, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Male' OR gender = 'Female'
GROUP BY company
ORDER BY AVG(base_salary) DESC;
    """

gender_female_best_salaries_in_company = """
SELECT 
    company,
    gender, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Female'
GROUP BY company
ORDER BY AVG(base_salary) DESC;
    """

gender_salary = """
SELECT 
    gender,
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender = 'Male' OR gender = 'Female' OR gender= 'Other'
GROUP BY gender
ORDER BY AVG(base_salary) DESC;
    """

years_of_experience_salary= """
SELECT 
    years_of_experience, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
GROUP BY years_of_experience
ORDER BY AVG(base_salary) DESC;
    """

years_at_company_salary= """
SELECT 
    years_at_company, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
GROUP BY years_at_company
ORDER BY AVG(base_salary) DESC;
    """

gender_male_years_at_company_salary= """
SELECT 
    years_at_company, 
    gender,
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Male'
GROUP BY years_at_company
ORDER BY AVG(base_salary) DESC;
    """

gender_female_years_at_company_salary= """
SELECT 
    years_at_company, 
    gender,
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Female'
GROUP BY years_at_company
ORDER BY AVG(base_salary) DESC;
    """

gender_male_years_of_experience_salary= """ 
SELECT 
    years_of_experience,
    gender, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Male'
GROUP BY years_of_experience
ORDER BY AVG(base_salary) DESC;
    """

gender_female_years_of_experience_salary= """ 
SELECT 
    years_of_experience,
    gender, 
    AVG(base_salary) AS 'average_salary'
FROM
    salaries
    WHERE gender= 'Female'
GROUP BY years_of_experience
ORDER BY AVG(base_salary) DESC;
    """

male_female_average_salary= """
select
    p.company,
    AVG(base_salary)
from (
        SELECT
            company,
            gender,
            base_salary
        from salaries
        where
            gender = 'Male'
            or gender = 'Female'
    ) p
GROUP BY p.company
ORDER BY AVG(base_salary) DESC;
"""