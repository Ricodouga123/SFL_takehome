from db_init import engine, meta

from sqlalchemy import text, select

import pprint

with engine.connect() as conn:

    result = conn.execute(select(meta.tables['user']))

    pprint.pprint(result.all())