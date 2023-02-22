from constants import (
    SERVER_HOSTNAME,
    HTTP_PATH,
    ACCESS_TOKEN,
    DB_NAME,
    TABLE_NAME,
)
from databricks import sql

def get_line_data():
    """
    Joins the user and sensor tables, selects specified columns and an aggregated column, returns it as a pandas dataframe

    Returns
    -------
    df : pandas dataframe
        basic query of data from Databricks as a pandas dataframe
    """
    connection1 = sql.connect(
        server_hostname=SERVER_HOSTNAME,
        http_path=HTTP_PATH,
        access_token=ACCESS_TOKEN,
    )
    cursor1 = connection1.cursor()
    cursor1.execute(
         f"SELECT * FROM {DB_NAME}.{TABLE_NAME}"
        )

    df = cursor1.fetchall_arrow()
    df = df.to_pandas()
    cursor1.close()
    connection1.close()
    return df