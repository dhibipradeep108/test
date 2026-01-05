import csv
from django.apps import apps
from django.core import serializers
from django.core.serializers.base import DeserializationError

class Serializer(serializers.python.Serializer) :
    def get_dump_object(self, obj) :
        dumped_object = super().get_dump_object(obj)
        row = [dumped_object["model"], str(dumped_object["pk"])]
        row += [str(value) for value in dumped_object["fields"].values()]
        return ",".join(row), dumped_object["model"]
    
    def end_object(self, obj) :
        dumped_object_str, model = self.get_dump_object(obj)
        if self.first :
            fields = [field.name for field in apps.get_model(model)._meta.fields]
            # fields = [field.name for field in obj._meta.fields]
            header = ",".join(fields)
            self.stream.write(f"model,{header}\n")
        self.stream.write(f"{dumped_object_str}\n")
        
    def getvalue(self) :
        return super(serializers.python.Serializer, self).getvalue()

class Deserializer(serializers.python.Deserializer) :
    def __init__(self, stream_or_string, **options) :
        if isinstance(stream_or_string, bytes) :
            stream_or_string = stream_or_string.decode()
        if isinstance(stream_or_string, str) :
            stream_or_string = stream_or_string.splitlines()
        try :
            objects = csv.DictReader(stream_or_string)
        except Exception as exc :
            raise DeserializationError() from exc
        super().__init__(object, **options)
    
    def _handle_object(self, obj) :
        try :
            model_fields = apps.get_model(obj["model"])._meta.fields
            obj["fields"] = {field.name: obj[field.name] for field in model_fields if field.name in obj}
            yield from super._handle_object(obj)
        except (GeneratorExit, DeserializationError) :
            raise
        except Exception as exc :
            raise DeserializationError(f"Error in deserialization object: {exc}") from exc