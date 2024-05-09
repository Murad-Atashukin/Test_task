from dataclasses import dataclass
from dataclasses_json import DataClassJsonMixin


@dataclass
class ConfigurationModel(DataClassJsonMixin):
    start_url: str
