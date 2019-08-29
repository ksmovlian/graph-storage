from flask import Flask, request, jsonify
from graph_storage import GraphStorage
from node_view_model import NodesArray
from marshmallow import ValidationError


app = Flask(__name__)
graph_storage = GraphStorage()
nodes_list_schema = NodesArray()


@app.route('/nodes', methods=['POST'])
def insert_nodes_list():
    request_json = request.get_json()

    try:
        requested_nodes_list = nodes_list_schema.load(request_json)
        print(requested_nodes_list)
    except ValidationError as err:
        return jsonify({'errors': err.messages}), 400

    cyclic_nodes_skipped = graph_storage.add_nodes(requested_nodes_list.get('nodes'))
    if len(cyclic_nodes_skipped) > 0:
        return jsonify({'error': 'Loop relations are not allowed'}), 400

    return '', 201


@app.route('/trees/<node_id>')
def find_chains(node_id):

    node_id_related_chains = graph_storage.find_chains(node_id)
    return jsonify({'trees': node_id_related_chains})


if __name__ == '__main__':
    app.run()
