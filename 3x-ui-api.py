from py3xui import AsyncApi, Client
import asyncio
import uuid
import json
import random
from py3xui.inbound import Inbound, Settings, Sniffing, StreamSettings
from datetime import datetime, timedelta
from pprint import pprint

SETTING_FILE_PATH = "settings.json"


class Settings:
    def __init__(self, data):
        self.ip_or_url = data["ip_or_url"]
        self.port = data["port"]
        self.path = data["path"]
        self.username = data["username"]
        self.password = data["password"]

        self.host_with_port_and_path = f"http://{self.ip_or_url}:{self.port}/{self.path}"



async def get_settings_for_all_servers(file_path: str = SETTING_FILE_PATH) -> list[Settings]:
    with open(file_path, "r") as file:
        data = json.load(file)
    return [Settings(server_config) for server_config in data] 


async def initialize_api(Settings: Settings) -> AsyncApi:
    api = AsyncApi(Settings.host_with_port_and_path, Settings.username, Settings.password)
    await api.login()
    return api


async def initialize_apis(settings: list[Settings]) -> list[AsyncApi]:
    settings = await get_settings_for_all_servers()
    api_list = []
    for setting in settings:
        api = await initialize_api(setting)
        api_list.append(api)
    return api_list


async def create_inbound(api: AsyncApi, port: int = 1234):
    settings = Settings()
    sniffing = Sniffing(enabled=True)

    tcp_settings = {
        "acceptProxyProtocol": False,
        "header": {"type": "none"},
    }
    stream_settings = StreamSettings(security="reality", network="tcp", tcp_settings=tcp_settings)

    inbound = Inbound(
        enable=True,
        port=port,
        protocol="vless",
        settings=settings,
        stream_settings=stream_settings,
        sniffing=sniffing,
        remark="generated_by_api",
    )
    await api.inbound.add(inbound)





async def create_client_connection(api: AsyncApi, expire_time_in_day: int = 31, inbound_number: int = 1)  -> tuple[Client, Inbound]:
    inbounds = await api.inbound.get_list()
    used_ports = [inbound.port for inbound in inbounds]
    # i need only 1 free port, only single one non used ports, no list
    non_used_ports = [port for port in range(1234, 65535) if port not in used_ports]

    if len(inbounds) == 0:
        await create_inbound(api, non_used_ports.pop(0))
    
    if len(inbounds) < inbound_number:
        inbound_number = 1

    if not any([_.remark == "generated_by_api" for _ in inbounds]):
        await create_inbound(api, non_used_ports.pop(0))
        inbounds = await api.inbound.get_list()
        inbound_number = len(inbounds)
    else:
        inbound_number = [i for i, _ in enumerate(inbounds) if _.remark == "generated_by_api"][0] + 1


    email = f"generated_{uuid.uuid4()}@generated.com"
    id = str(uuid.uuid4())

    expiry_date = datetime.now() + timedelta(days=expire_time_in_day)
    expiry_time = int(expiry_date.timestamp() * 1000)

    new_client = Client(
        id=id,
        email=email,
        enable=True,
        expiry_time=expiry_time
    )

    await api.client.add(inbound_number, [new_client])
    return new_client, inbounds[inbound_number-1]
    
        




async def main():
    api_list: list[AsyncApi] = await initialize_apis(await get_settings_for_all_servers())
    api: AsyncApi = random.choice(api_list)
    # mail = await create_client(api)
    # print(mail)
    # api.database.token
    # print(await api.client.get_by_email(mail))
    inbounds = await api.inbound.get_list()
    print('\n\n\n')
    a = await create_client_connection(api)
    print(a[0].email, a[0].id, a[1].port, a[1].id)


asyncio.run(main())