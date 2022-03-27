import sqlalchemy

metadata_obj = sqlalchemy.MetaData()

credits_table = sqlalchemy.Table(
    "credits",
    metadata_obj,
    sqlalchemy.Column("ssn", sqlalchemy.String, primary_key=True),
    sqlalchemy.Column("first_name", sqlalchemy.String),
    sqlalchemy.Column("last_name", sqlalchemy.String),
    sqlalchemy.Column("address", sqlalchemy.String),
    sqlalchemy.Column("assessed_income", sqlalchemy.Integer),
    sqlalchemy.Column("balance_of_debt", sqlalchemy.Integer),
    sqlalchemy.Column("hashed_password", sqlalchemy.String),
    sqlalchemy.Column("complaints", sqlalchemy.Boolean)
)