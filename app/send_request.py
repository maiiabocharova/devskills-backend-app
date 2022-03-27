BASE_URL = 'https://infra.devskills.app/api/credit-data/'

async def send_request(ssn, session):
    result = {}
    for endpoint in [
            f'personal-details/{ssn}',
            f'assessed-income/{ssn}',
            f'debt/{ssn}'
        ]:
        async with session.get(BASE_URL+endpoint) as resp:
            if resp.status != 200:
                break
            result.update(
                await resp.json()
                )
    return result