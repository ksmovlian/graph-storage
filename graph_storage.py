import json
from node import Node


class GraphStorage:
    json_file_name = 'all_nodes.json'

    def __init__(self):
        self.node_id_to_node = {}
        with open(self.json_file_name, 'r') as all_nodes_json:
            try:
                json_object = json.loads(all_nodes_json)

                if 'nodes' not in json_object:
                    return

                for node_dict in json_object['nodes']:
                    self.node_id_to_node[node_dict['id']] = Node(node_dict)

            except (TypeError, ValueError):
                print('Exception, while reading json file.')
                return

    def _add_node(self, new_node_dict: dict):
        node_to_process = self.node_id_to_node.get(new_node_dict['id'])
        node_to_process_valid_parents = []
        new_node_parent = new_node_dict.get('parent')
        if node_to_process is None:
            node_to_process = Node({
                'id': new_node_dict['id'],
                'parents': [] if new_node_parent is None else [new_node_parent]
            })
        elif node_to_process.parents and new_node_parent not in node_to_process.parents:
            node_to_process_valid_parents = node_to_process.parents
            node_to_process.parents += [new_node_parent]
        else:
            node_to_process.parents = [new_node_parent]
            node_to_process.parents = list(filter(None.__ne__, node_to_process.parents))
        if node_to_process.is_new_node_cyclic(self.node_id_to_node, new_node_parent):
            node_to_process.parents = node_to_process_valid_parents
            return False

        if new_node_parent is not None and new_node_parent not in self.node_id_to_node.keys():
            self.node_id_to_node[new_node_parent] = Node({'id': new_node_parent, 'parents': []})

        self.node_id_to_node[node_to_process.node_id] = node_to_process
        return True

    def add_nodes(self, new_nodes_list: list):
        cyclic_nodes = []
        for new_node in new_nodes_list:
            if not self._add_node(new_node):
                cyclic_nodes.append(new_node)

        with open('all_nodes.json', 'w') as all_nodes_json:
            json.dump({'nodes': [node.__dict__ for node in self.node_id_to_node.values()]}, all_nodes_json)

        return cyclic_nodes

    def find_chains(self, node_id):
        are_roots_reached = False
        all_chains = []
        node_id_related_chains = []
        for youngest_node_id in list(self._find_youngest_nodes().keys()):
            all_chains.append([youngest_node_id])

        while not are_roots_reached:
            are_roots_reached = True
            for chain in all_chains:
                base_chain = chain.copy()
                chain_oldest_node_parents = self.node_id_to_node.get(chain[0]).parents
                if not chain_oldest_node_parents:
                    continue
                for index, parent in enumerate(chain_oldest_node_parents):
                    if index == 0:
                        are_roots_reached = False
                        chain.insert(0, parent)
                    else:
                        base_chain.insert(0, parent)
                        all_chains.append(base_chain)

        for built_chain in all_chains:
            if node_id in built_chain:
                node_id_related_chains.append(built_chain)

        return node_id_related_chains

    def _find_youngest_nodes(self):
        youngest_nodes_id_to_object = self.node_id_to_node.copy()
        all_parents_id = []
        for node in youngest_nodes_id_to_object.values():
            if node.parents is not None:
                all_parents_id += [parent for parent in node.parents]

        for parent_id in all_parents_id:
            youngest_nodes_id_to_object.pop(parent_id, None)

        return youngest_nodes_id_to_object
