# python-obj-variables
A function that gets all values not callables (not functions) from an object in python.

```python
class DummyClass:
    name = "Tobias"
    
    def dummy_function(self):
        return "anything"
        
    def as_json(self):
        values = []
        for key in dir(self):
            if "__" not in key:
                values.append(key)

        dictionary = {}
        for value in values:
            attr = getattr(self, value)
            if not callable(attr):
                dictionary[value] = attr

        return json.dumps(dictionary)
      
dc = DummyClass()

dc.as_json() # returns '{"name": "Tobias"}'
```

Tip: if you declare a value as @property, it will return too because its not considered callable ().
