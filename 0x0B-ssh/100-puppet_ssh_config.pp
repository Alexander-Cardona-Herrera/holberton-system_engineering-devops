# changing the configuration 

file_line {'ssh_config':
  path	=> '/etc/ssh/ssh_config',
  line	=> 'PasswordAuthentication no',
}

file_line {'ssh_config':
  path	=> '/etc/ssh/ssh_config',
  line	=> 'IdentityFile ~/.ssh/holberton',
}
