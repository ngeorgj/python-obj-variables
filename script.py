# This function returns all the declared values not callables from a class
#
# @ ngeorg - 23/05


class DummyClass:
    name = "this is a variable"
  
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

dc.as_json() # returns '{"name": "this is a variable"}'
