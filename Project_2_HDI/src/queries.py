ranking_per_cdei_query = """
        select
            inputs.carbon_dioxide_emission as carbon_dioxide_emission,
            oco.ranking as onu_ranking,
            ocr.ranking as revised_ranking
        from inputs
            join outputs_countries_onu as oco on inputs.entity_name = oco.entity_name
            join outputs_countries_revised as ocr on inputs.entity_name = ocr.entity_name
    """

compare_sdi_query = """
select 
    oco.entity_name as entity_name,
    oco.sustainable_development_index as onu_sustainable_development_index,
    ocr.sustainable_development_index as revised_sustainable_development_index
from outputs_countries_onu as oco 
join outputs_countries_revised as ocr on ocr.entity_name= oco.entity_name
ORDER BY oco.sustainable_development_index DESC
"""
