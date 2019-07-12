from flask import Flask, request, jsonify
from graph_storage import GraphStorage

app = Flask(__name__)
graph_storage = GraphStorage()


@app.route('/nodes', methods=['POST'])
def hello_world():
    request_json = request.get_json()
    requested_nodes_list = request_json.get('nodes')
    if requested_nodes_list is None:
        return jsonify({'error': 'No nodes sent in the request'}), 400

    cyclic_nodes_skipped = graph_storage.add_nodes(requested_nodes_list)
    if len(cyclic_nodes_skipped) > 0:
        return jsonify({'error': 'Loop relations are not allowed'}), 400

    return '', 201


@app.route('/trees/<node_id>')
def find_chains(node_id):

    node_id_related_chains = graph_storage.find_chains(node_id)
    return jsonify({'trees': node_id_related_chains})


if __name__ == '__main__':
    app.run()
