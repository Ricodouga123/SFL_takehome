from sqlalchemy import create_engine, text

engine = create_engine('sqlite:///sfl_db.db')

with engine.connect() as conn:
    result = conn.execute(text("select 'hello world'"))
    print(result.all())