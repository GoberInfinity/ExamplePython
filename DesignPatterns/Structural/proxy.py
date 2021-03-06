"""
Provide a surrogate or placeholder for another object to control access
to it or add other responsibilities.
"""

import abc


class Subject(metaclass=abc.ABCMeta):
    """
    Define the common interface for RealSubject and Proxy so that a
    Proxy can be used anywhere a RealSubject is expected.
    """

    @abc.abstractmethod
    def request(self):
        pass


class Proxy(Subject):
    """
    Maintain a reference that lets the proxy access the real subject.
    Provide an interface identical to Subject's.
    """

    def __init__(self, real_subject):
        self._real_subject = real_subject

    def request(self):
        # ... Caching, permissions, logging
        self._real_subject.request()
        # ...


class RealSubject(Subject):
    """
    Define the real object that the proxy represents.
    """

    def request(self):
        print("Expensive operation")


real_subject_eg = RealSubject()
proxy = Proxy(real_subject_eg)
proxy.request()
