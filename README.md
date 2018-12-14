# A Tiny package for cXense API

Make cXense API simple.

## Requirements
```
Python 3.6 above  (did't test in other versions)
```

## Installation
```sh
pip install pyCx
```

## How to use

**Step 1:** create a `Cx` object with `env.yaml` by using `CxConfig`
```python
import os
from pyCx import Cx, CxConfig

# using env.yaml
fp = os.path.abspath('env.yaml')
cx = Cx(CxConfig(fp))

# or just passing dict value
my_cx_config = {
    'site_id': YOUR_ID,
    'username': 'YOUR_USERNAME',
    'secret': 'YOUR_KEY',
    'apiserver': 'https://api.cxense.com',
}
cx = Cx(my_cx_config)
```

and here's `env.yaml` sample:
```yaml
default:
  site_id: YOUR_ID
  username: YOUR_USERNAME
  secret: YOUR_KEY
  apiserver: https://api.cxense.com
```

**Step 2:** send a `/traffic` request by using `CxQuery`
```python
import json
from pyCx import Cx, CxenseURL
from pyCx.helpers import date_range

cx = Cx(my_cx_config)

# get CxQuery object from Cx
query = cx.get_query()

# apply date range for what we want, here will get data from 11/01 to 11/30 (include).
dates = date_range('2018-11-01', '2018-12-01')

# remember do a reset() before a new request.
status, header, content = query.reset() \
    .uri(CxenseURL.TRAFFIC) \
    .add_filter({'type': 'and', 'filters': [{'group': "PREFIX-articleid", 'items': ['123405'], 'type': "keyword"}]}) \
    .add_fields(['events', 'uniqueUsers']) \
    .add_history_fields(['events', 'uniqueUsers']) \
    .add_dates(dates) \
    .send()

# print results
result = json.loads(content.decode('utf-8'))
print(result)
```
- you can find API URI lists from [CxenseURL](https://github.com/kilfu0701/pyCx/blob/master/pyCx/cx_url.py)

## Docs

TODO

## Contributors
[kilfu0701](https://github.com/kilfu0701)

## Lastest Version
0.0.11 (Lastest, 2018/12/13)

[other releases](https://github.com/kilfu0701/pyCx/releases)

## License
MIT
