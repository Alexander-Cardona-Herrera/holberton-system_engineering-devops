# exceuting a command

exec { 'killmenow':
  command => 'pkill -3 killmenow',
}
