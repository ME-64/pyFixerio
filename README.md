# pyFixerio
*A Python wrapper for fixer.io API endpoints.*

This wrapper only uses the free version of the API, but delivers similar functionality
to paid versions. Namely, the wrapper deals with fixer.io's restrictions on:
    - Base currency is only allowed to be 'EUR'
    - No access to the time series API

#### Basic usage

```python
>>> from pyfixerio.pyfixerio import Fixerio

>>> fx = Fixerio('ACCESS_KEY')

>>> fx.current('EURUSD')

### {'EURUSD', 1.1423}

>>> fx.historical('USDGBP', '2019-01-05')

### {'2019-01-05': {'USDGBP': 0.8432'}}

```

#### TODO:

- Validate access key
- When converting / dividing to find base rate - round currency decimal places
- Implement creation of new acc for API key (?)
- Implement option to choose free api as default
