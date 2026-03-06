from extraction.pdf_reader import extract_text_from_pdf
from utils.text_cleaner import clean_text, chunk_text
from extraction.entity_extractor import extract_entities_and_relations
from graph.graph_builder import GraphBuilder
import json


PDF_PATH = "data/papers/sample_paper.pdf"


def run_pipeline():

    print("Loading PDF...")

    raw_text = extract_text_from_pdf(PDF_PATH)

    cleaned_text = clean_text(raw_text)

    chunks = chunk_text(cleaned_text)

    print("Total chunks:", len(chunks))

    all_entities = set()
    all_relationships = []

    print("\nRunning entity extraction on all chunks...\n")

    for i, chunk in enumerate(chunks):

        print(f"Processing chunk {i+1}/{len(chunks)}")

        result = extract_entities_and_relations(chunk)

        # collect entities
        for entity in result["entities"]:
            all_entities.add(entity)

        # collect relationships
        for rel in result["relationships"]:
            all_relationships.append(rel)

    print("\nExtraction Complete!\n")

    print("Total unique entities:", len(all_entities))
    print("Total relationships:", len(all_relationships))

    print("\nSample entities:")
    print(list(all_entities)[:10])

    print("\nSample relationships:")
    print(all_relationships[:10])

    # SAVE INGESTION RESULTS
    data = {
        "entities": list(all_entities),
        "relationships": all_relationships
    }

    with open("data/graph_data.json", "w") as f:
        json.dump(data, f, indent=2)

    print("\nGraph data saved to data/graph_data.json")

    builder = GraphBuilder()
    builder.build_graph(all_entities, all_relationships)

    print("\nGraph stored in Neo4j!")


if __name__ == "__main__":
    run_pipeline()