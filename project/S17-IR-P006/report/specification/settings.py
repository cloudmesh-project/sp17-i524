
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

aws_location = {
    'schema': {
        'region_name': {
            'type': 'string'
        },
        'availability_zone': {
            'type': 'integer'
        },
        'country': {
            'type': 'integer'
        },
        'zone_state': {
            'type': 'string'
        },
        'provider': {
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

aws_flavor = {
    'schema': {
        'name': {
            'type': 'string'
        },
        'extra': {
            'type': 'dict',
            'schema': {}
        },
        'price': {
            'type': 'float'
        },
        'ram': {
            'type': 'integer'
        },
        'bandwidth': {
            'type': 'string'
        },
        'disk': {
            'type': 'integer'
        },
        'id': {
            'type': 'string'
        }
    }
}

aws_node = {
    'schema': {
        'uuid': {
            'type': 'string'
        },
        'state': {
            'type': 'string'
        },
        'name': {
            'type': 'string'
        },
        'public_ips': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        },
        'provider': {
            'type': 'string'
        },
        'private_ips': {
            'type': 'list',
            'schema': {
                'type': 'string'
            }
        }
    }
}



eve_settings = {
    'MONGO_HOST': 'localhost',
    'MONGO_DBNAME': 'testing',
    'RESOURCE_METHODS': ['GET', 'POST', 'DELETE'],
    'BANDWIDTH_SAVER': False,
    'DOMAIN': {
        'aws_image': aws_image,
        'aws_location': aws_location,
        'aws_flavor': aws_flavor,
        'aws_node': aws_node,
    },
}
