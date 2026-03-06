import os
from dotenv import load_dotenv
from graph.neo4j_client import Neo4jClient

load_dotenv()


class GraphBuilder:

    def __init__(self):

        self.db = Neo4jClient(
            os.getenv("NEO4J_URI"),
            os.getenv("NEO4J_USER"),
            os.getenv("NEO4J_PASSWORD")
        )

    def build_graph(self, entities, relationships):

        for entity in entities:
            self.db.create_entity(entity)

        for rel in relationships:

            if len(rel) == 3:
                source, relation, target = rel

                self.db.create_relationship(source, relation, target)