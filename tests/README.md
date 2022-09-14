# Tests

## Setup

To run tests you'll need to run an instance of [mockserver](https://github.com/mock-server/mockserver) running at port 1080. This can be done using [Docker](https://www.docker.com/):
- [Install docker](https://www.docker.com/get-started/)
- Start `mockserver`:
   ```
   docker run --name mockserver -d --rm -p 1080:1080 mockserver/mockserver:5.13.0
   ```

To view mockserver logs:
```
docker logs -f mockserver
```

Or you can use *Mockserver-UI* which will be launched automatically at [localhost:1080/mockserver/dashboard](localhost:1080/mockserver/dashboard).

Alternatively, you can also run an instance of [portainer](https://www.portainer.io/) by running:
```
docker run -d -p 9000:9000 --restart always -v /var/run/docker.sock:/var/run/docker.sock -v /opt/portainer:/data portainer/portainer
```
This will provide a GUI at [localhost:9000](localhost:9000) where one can start, stop, and view logs for `mockserver`.

## Running

Each python script in this directory contains tests for a specific api. To test an API, it needs to be installed on your system.
```sh
python3 -m pip install -e ../pnap_network_api/
```

Then, you need to download the test dependencies:
```sh
pip install -r requirements.txt
```

Once this is done, you can then run the respective test script:
```sh
python pnap_network_api_test.py
```