# automation to find a replace of a bad file extension
exec {'fix phpp':
    command  => 'sudo sed -i "s/phpp/php/" /var/www/html/wp-settings.php',
    provider => shell
}
