from db_init import engine, meta

from util import getUniqueGender, getDictFromCsv

import csv, ipaddress

from sqlalchemy import select

from sqlalchemy.dialects.postgresql import insert

if __name__ == '__main__':

    path = "Data.csv"

    mdt = meta.tables

    with engine.connect() as conn:
        
        with conn.begin():

            for i in getUniqueGender(csv_path = path):

                conn.execute(insert(mdt['gender']).values(gender_type = i).on_conflict_do_nothing())
            
            gender_dict = {}

            for i, j in conn.execute(select(mdt['gender'])).all():

                gender_dict[j] = i

            for dict in getDictFromCsv(csv_path = path):

                conn.execute(insert(mdt['user']).values(
                    id = dict['id'],
                    first_name = dict['first_name'],
                    last_name = dict['last_name'],
                    email_address = dict['email'],
                    gender_id = gender_dict[dict['gender']],
                    ip_long = int(ipaddress.ip_address(dict['ip_address'])),
                    ip_str = dict['ip_address'] 
                ).on_conflict_do_nothing())