global config

downloads = {
    '/tmp/packerio.zip': {
        'url': 'https://releases.hashicorp.com/packer/{}/packer_{}_linux_amd64.zip'.format(
            config.get('packer', {}).get('version', '1.5.4')),
        'sha256': config.get('packer', {}).get('checksum',
                                                'c7277f64d217c7d9ccfd936373fe352ea935454837363293f8668f9e42d8d99d'),
    },
}

pkg_apt = {
    'unzip': {
        'installed': True,
    }
}

actions = {
    'unpack_packerio.zip': {
        'command': 'unzip /tmp/packerio.zip',
        'needs': [
            'download:/tmp/packerio.zip',
            'pkg_apt:unzip',
        ],
    },
}

symlink = {
    '/usr/local/bin/packerio': {
        'target': '/opt/packer',
        'needs': [
            'action:unpacker_packerio.zip',
        ],
    },
}