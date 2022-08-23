
## Responses

Every response will contain the status flag `s` like: `{"s": 0 or 1, ...}`

If `s` is `0` then there was an error and the request could not be satisfied, otherwise it must be `1`.

If the response have a status flag of 0, then there must be a message or a reason (`msg`) for the fail like:

```json
{
    "s": 0,
    "msg": "Bad API key."
}
```
