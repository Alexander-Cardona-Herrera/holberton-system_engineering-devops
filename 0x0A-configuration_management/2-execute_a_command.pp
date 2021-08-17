# exceuting a command

exec { 'killmenow':
  command  => 'pkill -9 killmenow',
  provider => shell,
}
