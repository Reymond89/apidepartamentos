from sqlalchemy import Integer, String, Table, Column
from config.db import meta, engine

departamentos =Table("depatamentos", meta,
Column("id", Integer, primary_key=True),
Column("ref", Integer),
Column("name", String(250)))

meta.create_all(engine)