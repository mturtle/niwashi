# niwashi
monitor, control, and tend to registered devices.  Attempt to emulate jake wright's cool home automation series.

## Usage

All responses will have the form
```json
{
    "data": "mixed type holding the content of the response",
    "message": "description of what happened"
}```

subsequent response definitions will only detail the expected value of the data field

### List all devices

**Definition**

`GET /devices`

**Response**

- `200 OK` on success

```json
[
    {
        "identifier": "floor-lamp",
        "name": "floor lamp",
        "device_type": "switch",
        "controller_gateway": "10.0.0.212"
    },
    {
        "identifier": "tv",
        "name": "living room tv",
        "device_type": "tv",
        "controller_gateway": "10.0.0.214"
    }
]

### Register a new device

**Definition**

`POST /devices`

**Arguments**
- `"identifier":string` a globally unique identifier for the device
- `"name":string` friendly device name
- `"device_type":string` the device type as understood by the client
- `"controller_gateway":string` the IP address of the device controller

If a device with the gien identifier already exists, the existing device will be overwritten

**Response**

- `201 Created` on success

### Lookup device details

`GET / device/<identifier>`

**Arguments**
- `"identifier":string` unique device identifier

**Response**

- `200 OK` on success
- `404 Not Found` if device not found


