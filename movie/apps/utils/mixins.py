class ActionSerializerMixin:
    action = None
    serializer_class = None
    serializer_classes = None
    
    def get_serializer_class(self):
        if self.action in self.serializer_classes:
            return self.serializer_classes[self.action]
        return self.serializer_class
