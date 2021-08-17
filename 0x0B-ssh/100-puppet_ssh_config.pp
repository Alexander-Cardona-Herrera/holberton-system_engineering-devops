# changing the configuration 

file_line {'ssh_config password':
  path    => '/etc/ssh/ssh_config',
  line    => '    PasswordAuthentication no',
  replace => 'true'
}

file_line {'ssh_config identity':
  path    => '/etc/ssh/ssh_config',
  line    => '    IdentityFile ~/.ssh/holberton',
  replace => 'true'
}
