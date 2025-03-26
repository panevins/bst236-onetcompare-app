from OnetWebService import OnetWebService
from onet_credentials import get_credentials
import pandas as pd

def get_user_input(prompt):
    result = ''
    while (len(result) == 0):
        result = input(prompt + ': ').strip()
    return result

def check_for_error(service_result):
    if 'error' in service_result:
        print(f"Error: {service_result['error']}")
        return True
    return False

# This function will return the rows of the table (e.g., skills) specified by the filter
# Returns only the relevant columns
def get_rows(onet_service, table_id, **query_params):
    rows_rslt = onet_service.call(f'/database/rows/{table_id}', **query_params)
    if check_for_error(rows_rslt):
        return None
    rows_df = pd.DataFrame(rows_rslt['row'])
    rows_df = rows_df[['element_name', 'data_value', 'lower_ci_bound', 'upper_ci_bound']]
    return rows_df

#this function gets unique labels from a table that are a combination of scale and element
# it returns a list of unique labels for the specified column (default is 'element_scale') 
def get_elements(onet_service, table_id, colname='element_scale', **query_params):
    rows_rslt = onet_service.call(f'/database/rows/{table_id}', **query_params)
    if check_for_error(rows_rslt):
        return None
    unique_elements = set()
    for row in rows_rslt['row']:
        if colname in row:
            unique_elements.add(row[colname])
    return list(unique_elements)


if __name__ == "__main__":
    # Get credentials from cache or prompt user
    username, password = get_credentials()
    onet_ws = OnetWebService(username, password)

    vinfo = onet_ws.call('about')
    check_for_error(vinfo)
    print("Connected to O*NET Web Services version " + str(vinfo['api_version']))
    print("")
    
    job_code = get_user_input('ID for table query (skills, knowledge, abilities, interests, work_values, work_styles)')
    
    # Example: Make a filtered API call with query parameters
    # Scale ID IM/LV for SKA, OI for interests, EX for work values, IM for work styles
    query_params = { 'filter':  'scale_id.eq.IM' } #"onetsoc_code.eq.11-1011.00",
    #rows_rslt = get_elements(onet_ws, job_code, 'element_id', '')
    rows_rslt = get_elements(onet_ws, job_code, **query_params)
    print(rows_rslt)