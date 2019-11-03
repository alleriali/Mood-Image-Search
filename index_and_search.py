from collections import defaultdict
from typing import List, Dict
from functools import reduce


class Doc:
    def __init__(self, doc_id, entities, non_entities):
        self.doc_id = doc_id
        self.entities = entities
        self.non_entities = non_entities

    def get_id(self):
        return self.doc_id

    def get_entities(self):
        return self.entities

    def get_non_entities(self):
        return self.non_entities


class Query:
    def __init__(self, entities, non_entities):
        self.entities = entities
        self.non_entities = non_entities

    def get_entities(self):
        return self.entities

    def get_non_entities(self):
        return self.non_entities


def generate_index_keys(doc):
    doc_id = doc.get_id()
    entities = doc.get_entities()
    non_entities = doc.get_non_entities()
    index_keys = set([])
    for entity in entities:
        index_keys.add("ENTITY:" + entity)
    for non_entity in non_entities:
        index_keys.add("NON_ENTITY:" + non_entity)

    emit_as_pairs = map(lambda index_key: (index_key, doc_id), index_keys)
    return list(emit_as_pairs)


def group_by_key(index: Dict[str, List[int]], key_to_id_pairs: List) -> Dict[str, List[int]]:
    for pair in key_to_id_pairs:
        if pair[0] not in index.keys():
            index[pair[0]] = []
        index[pair[0]].append(pair[1])
    return index


def index(docs):
    index_key_to_candidates = reduce((lambda index_dict, key_to_id_pairs: group_by_key(index_dict, key_to_id_pairs)),
                                     map(generate_index_keys, docs), {})
    return index_key_to_candidates


def search(query, index_key_to_candidates):
    search_keys = set([])
    for entity in query.get_entities():
        search_keys.add("ENTITY:" + entity)
    for non_entity in query.get_non_entities():
        search_keys.add("NON_ENTITY:" + non_entity)

    retrieval_candidates = defaultdict(int)
    for key in search_keys:
        if key in index_key_to_candidates.keys():
            candidates = index_key_to_candidates[key]
            for candidate in candidates:
                retrieval_candidates[candidate] += 1
    return retrieval_candidates

docs: List[Doc] = []
docs.append(Doc(1, ['e1'], ['ne1']))
docs.append(Doc(2, ['e2'], ['ne2']))

key_to_candidates_index = index(docs)
print(key_to_candidates_index)

print(search(Query(['e1'], ['ne1']), key_to_candidates_index))
