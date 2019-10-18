The API will eventuall support:

To prioritize, just push everything into the first route for now.
Each additional route will return a subset of the previous route.

/colonies
/colony/#id
/colony/#id/ants
/colony/#id/ant/#id
/colony/#id/tunnels
/colony/#id/tunnel/#id
/colony/#id/leaves
/colony/#id/leaf/#id

```JSON
{
  "colonies": [
    {
      "id": 1,
      "ants": [
        {
          "id": 1,
          "pos": [
            10,
            12
          ],
          "size": 5,
          "carrying": false,
          "type": "worker"
        },
        {
          "id": 2,
          "pos": [
            20,
            30
          ],
          "size": 5,
          "carrying": false,
          "type": "queen"
        }
      ],
      "leaves": [
        {
          "id": 1,
          "pos": [
            20,
            30
          ]
        }
      ],
      "tunnels": []
    }
  ]
}
```
