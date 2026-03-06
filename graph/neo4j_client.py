from neo4j import GraphDatabase


class Neo4jClient:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_entity(self, name):

        with self.driver.session() as session:
            session.run(
                "MERGE (e:Entity {name:$name})",
                name=name
            )

    def create_relationship(self, source, relation, target):

        with self.driver.session() as session:

            session.run(
                """
                MERGE (a:Entity {name:$source})
                MERGE (b:Entity {name:$target})
                MERGE (a)-[:RELATION {type:$relation}]->(b)
                """,
                source=source,
                target=target,
                relation=relation
            )