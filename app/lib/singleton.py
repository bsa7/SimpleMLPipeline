''' This abstract class implements Singleton pattern '''

class Singleton(type):
  ''' Class with only one instance allowed. '''
  instance = None

  def __call__(cls, *args, **kwargs):
    if cls.instance is None:
      cls.instance = super(Singleton, cls).__call__(*args, **kwargs)
    return cls.instance
