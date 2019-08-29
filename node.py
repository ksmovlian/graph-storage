class Node:
    def __init__(self, node_dict: dict):
        self.node_id = node_dict['id']
        self.parents = node_dict.get('parents')

    def __repr__(self):
        return self.node_id

    def is_new_node_cyclic(self, node_id_to_node: dict, node_to_check_id: str):
        if node_to_check_id is None:
            return False

        node_to_check = node_id_to_node.get(node_to_check_id)
        if node_to_check is None:
            return False
        elif node_to_check.node_id == self.node_id:
            return True

        for parent in node_to_check.parents:
            if self.is_new_node_cyclic(node_id_to_node, parent):
                return True

        return False
