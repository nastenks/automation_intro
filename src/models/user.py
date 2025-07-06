from dataclasses import dataclass

@dataclass
class User:
    full_name: str
    
    @classmethod
    def from_json(cls, data):
        return cls(
            full_name=data.get('data', {}).get('username', {}).get('full', '')
        )