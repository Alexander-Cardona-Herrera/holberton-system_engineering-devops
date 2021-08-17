file { '0-create_a_file.pp':
    path    => /tmp/holberton,
    content => 'I love Puppet',
    group   => www-data,
    mode    => '0744',
    owner   => www-data,
}
