
aws_image = {
    'schema': {
        'driver': {
            'type': 'string'
        },
        'id': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

aws_volume = {
    'schema': {
        'driver': {
            'type': 'string'
        },
        'id': {
            'type': 'string'
        },
        'size': {
            'type': 'integer'
        }
    }
}

aws_location = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'availability_zone': {
            'type': 'string'
        },
        'country': {
            'type': 'string'
        },
        'zone_state': {
            'type': 'string'
        },
        'id': {
            'type': 'integer'
        },
        'region_name': {
            'type': 'string'
        }
    }
}

aws_flavor = {
    'schema': {
        'disk': {
            'type': 'integer'
        },
        'price': {
            'type': 'float'
        },
        'ram': {
            'type': 'integer'
        },
        'id': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        }
    }
}

aws_keypair = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'fingerprint': {
            'type': 'string'
        }
    }
}

aws_node = {
    'schema': {
        'state': {
            'type': 'string'
        },
        'uuid': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'provider': {
            'type': 'string'
        }
    }
}



eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'BANDWIDTH_SAVER': False,
    'PAGINATION': False,
    'DOMAIN': {
        'aws_image': aws_image,
        'aws_volume': aws_volume,
        'aws_location': aws_location,
        'aws_flavor': aws_flavor,
        'aws_keypair': aws_keypair,
        'aws_node': aws_node,
    },
}
