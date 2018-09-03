class Factory(object):

    @staticmethod
    def create(data):
        raise Exception('Implementation required!')

    @staticmethod
    def raise_exception(type):
        raise Exception('Invalid type (%s) found!' % type)