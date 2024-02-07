import pnap_audit_api

# Smoke test only for local testing

def setup_configuration():
    client_id = "YOUR_ID"
    client_secret = "YOUR_SECRET"
    access_token = "YOUR_ACCESS_TOKEN"
    api_url = "https://api-dev.phoenixnap.com/audit/v1"
    token_url = "https://auth-dev.phoenixnap.com/auth/realms/BMC/protocol/openid-connect/token"
    scopes = ["bmc", "bmc.read"]

    # Create Configuration instance
    configuration = pnap_audit_api.Configuration()
    configuration.host = api_url
    configuration.client_id = client_id
    configuration.client_secret = client_secret
    configuration.token_url = token_url
    configuration.scopes = scopes
    configuration.access_token = access_token

    return configuration

def test_smoke():
    configuration = setup_configuration()

    api_client = pnap_audit_api.ApiClient(configuration)
    api_instance = pnap_audit_api.EventsApi(api_client)

    result = api_instance.events_get()
    print(result)

if __name__ == "__main__":
    test_smoke()
