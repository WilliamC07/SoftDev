# Boilerplate for hosting flask on Apache2 Ubuntu 18.04

### Checklist for deploying
- app.debug = False
- ```sudo systemctl status apache2``` -- make sure apache is running

### Broken, what do?
- Make sure you restarted apache2: ```service apache2 restart```
- config file is right: "/etc/apache2/sites-available/"
- config is active: ```a2ensite <appname/config>
- Installed needed module: 
    ```sh
    sudo apt-get install libapache2-mod-wsgi
    sudo a2enmod wsgi
    sudo service apache2 restart
    ```
