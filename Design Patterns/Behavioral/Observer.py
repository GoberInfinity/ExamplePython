"""
Define a one-to-many dependency between objects so that when one object
changes state, all its dependents are notified and updatedautomatically.
"""

import abc


class Subject:
    """
    Know its observers. Any number of Observer objects may observe a
    subject.
    Send a notification to its observers when its state changes.
    """

    def __init__(self):
        self._observers = set()
        self._subject_state = None

    def attach(self, observer):
        observer._subject = self
        self._observers.add(observer)

    def detach(self, observer):
        observer._subject = None
        self._observers.discard(observer)

    def _notify(self):
        for observer in self._observers:
            observer.update(self._subject_state)

    @property #This is a getter, it is used by the setter
    def subject_state(self):
        return self._subject_state

    @subject_state.setter #This is the decorator
    def subject_state(self, arg):
        self._subject_state = arg
        self._notify()


class Observer(metaclass=abc.ABCMeta):
    """
    Define an updating interface for objects that should be notified of
    changes in a subject.
    """

    def __init__(self):
        self._subject = None
        self._observer_state = None

    @abc.abstractmethod # The subclass has to implement the abstract method
    def update(self, arg):
        pass


class ConcreteObserver(Observer):
    """
    Implement the Observer updating interface to keep its state
    consistent with the subject's.
    Store state that should stay consistent with the subject's.
    """
    
    def update(self, arg): #It is called when an update happens 
        self._observer_state = arg
        print(self._observer_state)

subject = Subject()
concrete_observer = ConcreteObserver()
subject.attach(concrete_observer)
subject.subject_state = 123 #It calls update method in the observer
subject.subject_state = 333 #It calls update method in the observer
