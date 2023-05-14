#!/usr/bin/env python3

class MyString:

  def __init__( self, value='' ):
    self.set_value( value )

  def is_sentence( self ):
    return self._value.endswith( "." )
  
  def is_question( self ):
    return self._value.endswith( "?" )
  
  def is_exclamation( self ):
    return self._value.endswith( "!" )
  
  def count_sentences( self ):
    value = self.value
    for punctuation in [ "!", "?" ]:
      value = value.replace( punctuation, "." )
    
    sentences = [ s for s in value.split( "." ) if s ]

    return len( sentences )

  def get_value( self ):
    return self._value 
  
  def set_value( self, value ):
    if isinstance( value, str ):
      self._value = value
    else:
      print( "The value must be a string." )

  value = property( get_value, set_value )

import re