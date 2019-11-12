The API will eventuall support:

To prioritize, just push everything into the first route for now.
Each additional route will return a subset of the previous route.

`/api/worlds`
`/api/world/#id`
`/api/world/#id/colonies`
`/api/colony/#id`
`/api/world/#id/colony/#id/ants`
`/api/ant/#id`
`/api/world/#id/colony/#id/tunnels`
`/api/tunnel/#id`
`/api/world/#id/colony/#id/leaves`
`/api/leaf/#id`

```JSON
{
  "id": 1,
  "age": 13,
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
