# exceuting a command

exec { 'killmenow':
  command => 'pkill killmenow',
}
