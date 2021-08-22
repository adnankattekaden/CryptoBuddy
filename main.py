from src.exchanges.wazirx.client import WazirxClient

user = WazirxClient()

print(user.get_global_config())