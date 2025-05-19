#!/usr/bin/env python3
class MyString:
    def __init__(self, value=""):
        self._value = ""  # Private variable to store the value
        self.value = value  # Use the property setter to validate
        
    @property
    def value(self):
        return self._value
        
    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ""
        
    def is_sentence(self):
        return self._value.endswith(".")
    
    def is_question(self):
        return self._value.endswith("?")
    
    def is_exclamation(self):
        return self._value.endswith("!")
    
    def count_sentences(self):
        # Normalize the string by replacing sentence-ending punctuation with a delimiter
        normalized = self._value.replace(".", "|").replace("!", "|").replace("?", "|")
        
        # Split the string by the delimiter and remove any empty parts
        sentences = [s.strip() for s in normalized.split('|') if s.strip()]
        
        return len(sentences)

    
  