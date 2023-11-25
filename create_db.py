from main import engine, base

#this will create the phsyical database based on the classes we have created
base.metadata.create_all(engine)
