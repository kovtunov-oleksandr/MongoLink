from typing import Dict, Type


class SingletonMeta(type):
    """A metaclass that creates a singleton class. The singleton class can only have one instance."""

    __instances: Dict[type, type] = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            cls.__instances[cls] = super().__call__(*args, **kwargs)
        return cls.__instances[cls]

    @classmethod
    def get_instance(mcs, instance_cls: Type):
        """Get instance of singleton class"""
        if instance_cls not in mcs.__instances:
            raise ValueError(f"Instance of {instance_cls} is not created")
        return mcs.__instances[instance_cls]
