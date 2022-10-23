import numpy as np


def compute_life_expectancy_index(observed_life_expectancy) -> float:
    result = (observed_life_expectancy - 20)/(85-20)
    return round(result, 2)


compute_life_expectancy_index(84)


def compute_education_index(mean_years_of_schooling, expected_years_of_schooling) -> float:
    result = ((mean_years_of_schooling/15) +
              (expected_years_of_schooling/18)) / 2
    return round(result, 2)


compute_education_index(13.9, 16.5)


def compute_income_index(observed_value_GNI, threshold_max_GNI) -> float:
    result = (np.log(observed_value_GNI) - np.log(100)) / \
        (np.log(threshold_max_GNI) - np.log(100))
    return round(result, 2)


compute_income_index(66933, 75000)


def compute_material_footprint_index(observed_value_MF, threshold_max_MF, threshold_min_MF) -> float:
    result = (threshold_max_MF-observed_value_MF) / \
        (threshold_max_MF - threshold_min_MF)
    return round(result, 2)


compute_material_footprint_index(31.1, 107.42, 0)


def compute_carbon_dioxide_emissions_index(observed_value_CDE, threshold_max_CDE, threshold_min_CDE) -> float:
    result = (threshold_max_CDE-observed_value_CDE) / \
        (threshold_max_CDE - threshold_min_CDE)
    return round(result, 2)


compute_carbon_dioxide_emissions_index(3.7, 68.72, 0)


def compute_human_development_index(lei, ei, ii) -> float:
    result = ((lei*ei*ii)**(1/3))
    return round(result, 2)


lei = compute_life_expectancy_index(84)
ei = compute_education_index(13.9, 16.5)
ii = compute_income_index(66933, 75000)

compute_human_development_index(lei, ei, ii)


def compute_factor_planetary_preassures(cdei, mfi) -> float:
    result = (cdei + mfi)/2
    return round(result, 2)


mfi = compute_material_footprint_index(31.1, 107.42, 0)
cdei = compute_carbon_dioxide_emissions_index(3.7, 68.72, 0)

compute_factor_planetary_preassures(cdei, mfi)


def compute_sustainable_development(hdi, fpp) -> float:
    result = (hdi*fpp)
    return round(result, 2)


hdi = compute_human_development_index(lei, ei, ii)
fpp = compute_factor_planetary_preassures(cdei, mfi)

compute_sustainable_development(hdi, fpp)
