# changing the configuration 

file_line {'/etc/ssh/ssh_config':
  line => IdentityFile ~/.ssh/holberton,
  line => PasswordAuthentication no, 
}
