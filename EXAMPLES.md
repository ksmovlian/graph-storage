# Examples:

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "ea846905f2a146c0acdfb48b4b79ff4a",
            "parent": "eb17b279d87c46c090dec77564d28ebf"
        },
        {
            "id": "eb17b279d87c46c090dec77564d28ebf",
            "parent": null
        }
    ]
}
```

Creates simple graph

![simple graph](images/simple_graph.png)

So we can return it in next views

GET /trees/eb17b279d87c46c090dec77564d28ebf

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a"]
    ]
}
```

or 

GET /trees/ea846905f2a146c0acdfb48b4b79ff4a

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a"]
    ]
}
```

if we add one more related node

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "520e8908527644b09153ecf17d57bbdc",
            "parent": "ea846905f2a146c0acdfb48b4b79ff4a"
        }
    ]
}
```

now our graph looks like this:

![simple graph](images/simple_graph_3.png)

and GET /trees/ea846905f2a146c0acdfb48b4b79ff4a now return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"]
    ]
}
```

Create more complex graph

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "5c6fed252c614ed2b3861c5fcb3afd8",
            "parent": "ea846905f2a146c0acdfb48b4b79ff4a"
        }
    ]
}
```

and we got 

![simple graph](images/complex_graph.png)

in this case GET /trees/ea846905f2a146c0acdfb48b4b79ff4a now return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"],
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "5c6fed252c614ed2b3861c5fcb3afd8"]
    ]
}
```
and GET /trees/520e8908527644b09153ecf17d57bbdc now return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"]
    ]
}
```

add one more node 

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "7a17889bcee840508fb2c8c565231069",
            "parent": "eb17b279d87c46c090dec77564d28ebf"
        }
    ]
}
```
graph:

![simple graph](images/complex_graph_1.png)

GET /trees/eb17b279d87c46c090dec77564d28ebf now return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"],
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "5c6fed252c614ed2b3861c5fcb3afd8"],
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069"]
    ]
}
```

but GET /trees/ea846905f2a146c0acdfb48b4b79ff4a still return 


```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"],
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "5c6fed252c614ed2b3861c5fcb3afd8"]
    ]
}
```

and GET /trees/7a17889bcee840508fb2c8c565231069 return only

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069"]
    ]
}
```

Lest create another chain

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "1c31b3c9c9634c1b8fcaaddc0acf936e",
            "parent": "7b3e74249395450ca419a91fde658eb7"
        },
        {
            "id": "468046efaa2f4158a0dbc79d53213bc6",
            "parent": 7b3e74249395450ca419a91fde658eb7
        }
    ]
}
```

In this case originally we don't have 7b3e74249395450ca419a91fde658eb7 but some of nodes related with it so we assume that this node should be exist:

And we got 

![simple graph](images/complex_graph_2.png)

and GET /trees/7b3e74249395450ca419a91fde658eb7 return 

```
{
    "trees": [
        ["7b3e74249395450ca419a91fde658eb7", "1c31b3c9c9634c1b8fcaaddc0acf936e"],
        ["7b3e74249395450ca419a91fde658eb7", "468046efaa2f4158a0dbc79d53213bc6"]
    ]
}
```

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "7b3e74249395450ca419a91fde658eb7",
            "parent": "7a17889bcee840508fb2c8c565231069"
        }
    ]
}
```

combine 2 our chains into one tree

![simple graph](images/complex_graph_3.png)

and 

GET /trees/eb17b279d87c46c090dec77564d28ebf should return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "520e8908527644b09153ecf17d57bbdc"],
        ["eb17b279d87c46c090dec77564d28ebf", "ea846905f2a146c0acdfb48b4b79ff4a", "5c6fed252c614ed2b3861c5fcb3afd8"],
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069", "7b3e74249395450ca419a91fde658eb7", "1c31b3c9c9634c1b8fcaaddc0acf936e"],
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069", "7b3e74249395450ca419a91fde658eb7", "468046efaa2f4158a0dbc79d53213bc6"]
    ]
}
```

GET /trees/7b3e74249395450ca419a91fde658eb7 should return

```
{
    "trees": [
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069", "7b3e74249395450ca419a91fde658eb7", "1c31b3c9c9634c1b8fcaaddc0acf936e"],
        ["eb17b279d87c46c090dec77564d28ebf", "7a17889bcee840508fb2c8c565231069", "7b3e74249395450ca419a91fde658eb7", "468046efaa2f4158a0dbc79d53213bc6"]
    ]
}
```

Lets try create loop

POST /nodes

```
{
    "nodes": [
        {
            "id": "ea846905f2a146c0acdfb48b4b79ff4a",
            "parent": "eb17b279d87c46c090dec77564d28ebf"
        },
        {
            "id": "eb17b279d87c46c090dec77564d28ebf",
            "parent": "ea846905f2a146c0acdfb48b4b79ff4a"
        }
    ]
}
```


it's return

status 400
```
{"error": "Loop relations not allowed"}
```

or we try to add node with loop to our existing schema 

POST /nodes

```
{
    "nodes": [
        {
            "id": "eb17b279d87c46c090dec77564d28ebf",
            "parent": "468046efaa2f4158a0dbc79d53213bc6"
        }
    ]
}
```

![simple graph](images/complex_graph_bad.png)

it's return

status 400
```
{"error": "Loop relations not allowed"}
```

Example of tree with multiple roots:

POST /nodes with body
```
{
    "nodes": [
        {
            "id": "e12afca2cc0c4d6fb2a27119010f1e20",
            "parent": "a0378f4f37c5492091918f53b4da15a5"
        },
        {
            "id": "e12afca2cc0c4d6fb2a27119010f1e20",
            "parent": "c592ff8d473a4924bcd5655ae1c6ffd5"
        }
    ]
}
```
![simple graph](images/multi_root.png)

and GET /trees/e12afca2cc0c4d6fb2a27119010f1e20 return 

```
{
    "trees": [
        ["a0378f4f37c5492091918f53b4da15a5", "e12afca2cc0c4d6fb2a27119010f1e20"],
        ["c592ff8d473a4924bcd5655ae1c6ffd5", "e12afca2cc0c4d6fb2a27119010f1e20"]
    ]
}
```

Lets add more nodes


POST /nodes with body
```
{
    "nodes": [
        {
            "id": "C90A70BD-23D0-4E8A-BA61-518745390EA5",
            "parent": "e12afca2cc0c4d6fb2a27119010f1e20"
        },
        {
            "id": "D483616F-2A54-497E-96B1-1DE919677000",
            "parent": "e12afca2cc0c4d6fb2a27119010f1e20"
        },
         {
            "id": "final",
            "parent": "C90A70BD-23D0-4E8A-BA61-518745390EA5"
        },
        {
            "id": "final",
            "parent": "D483616F-2A54-497E-96B1-1DE919677000"
        }
    ]
}
```

![simple graph](images/multi_comlex_tree.png)

and GET /trees/final return 

```
{
    "trees": [
        ["a0378f4f37c5492091918f53b4da15a5", "e12afca2cc0c4d6fb2a27119010f1e20", "C90A70BD-23D0-4E8A-BA61-518745390EA5", "final"],
        ["c592ff8d473a4924bcd5655ae1c6ffd5", "e12afca2cc0c4d6fb2a27119010f1e20", "C90A70BD-23D0-4E8A-BA61-518745390EA5", "final"],
        ["a0378f4f37c5492091918f53b4da15a5", "e12afca2cc0c4d6fb2a27119010f1e20", "D483616F-2A54-497E-96B1-1DE919677000", "final"],
        ["c592ff8d473a4924bcd5655ae1c6ffd5", "e12afca2cc0c4d6fb2a27119010f1e20", "D483616F-2A54-497E-96B1-1DE919677000", "final"]
    ]
}
```


but and GET /trees/a0378f4f37c5492091918f53b4da15a5 return only 

```
{
    "trees": [
        ["a0378f4f37c5492091918f53b4da15a5", "e12afca2cc0c4d6fb2a27119010f1e20", "C90A70BD-23D0-4E8A-BA61-518745390EA5", "final"],
        ["a0378f4f37c5492091918f53b4da15a5", "e12afca2cc0c4d6fb2a27119010f1e20", "D483616F-2A54-497E-96B1-1DE919677000", "final"]
    ]
}