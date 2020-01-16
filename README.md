# pyFixerio
*A Python wrapper for fixer.io API endpoints.*

This wrapper only uses the free version of the API, but delivers similar functionality
to paid versions. Namely, the wrapper deals with fixer.io's restrictions on:
    - Base currency is only allowed to be 'EUR'
    - No access to the time series API

#### Basic usage

```python
>>> from pyfixerio import Fixerio

>>> fx = Fixerio('ACCESS_KEY')

>>> fx.current('EURUSD')

### {'EURUSD', 1.1423}

>>> fx.historical('USDGBP', '2019-01-05')

### {'2019-01-05': {'USDGBP': 0.8432'}}

```

#### TODO:

- Validate access key
- Implement fallback API
- learn proper import methods for 3rd party modules
- Create virtual environment and requirements.txt
- package script for usage on pypi
- implement proper documentation for each method
- When converting / dividing to find base rate - round currency decimal places

