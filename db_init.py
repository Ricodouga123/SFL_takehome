from sqlalchemy import ForeignKey, create_engine, MetaData, Table, Column, Integer, String

engine = create_engine('sqlite:///sfl_db.db')

meta = MetaData()

for table in engine.table_names():

    table = Table(table, meta, autoload = True, autoload_with = engine)

if __name__ == '__main__':


    gender = Table('gender', meta,
        Column('id', Integer, primary_key = True),
        Column('gender_type', String(25), nullable = False, unique = True)
    )

    user = Table( 'user', meta, 
        Column('id', Integer, primary_key = True),
        Column('first_name', String(16), nullable = False),
        Column('last_name', String(16), nullable = False),
        Column('email_address', String(60), nullable = False),
        Column('gender_id', ForeignKey("gender.id"), nullable = True),
        Column('ip_long', Integer, nullable = False),
        Column('ip_str', String(25), nullable = False)
    )

    meta.create_all(engine)