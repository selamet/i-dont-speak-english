# i-dont-speak-english

### Setup Repo:
```
  git clone https://github.com/selametsamli/i-dont-speak-english.git
  cd i-dont-speak-english/
  pip3 install -r requirements.txt
  flask db init
  flask db migrate
  python3 wsgi.py

```

### Postgresql conf:
```
  sudo -u postgres psql
  CREATE DATABASE english;
  CREATE USER kullanici_adi WITH PASSWORD 'parola123';
  
  ALTER ROLE kullanici_adi SET client_encoding TO 'utf8';
  ALTER ROLE kullanici_adi SET default_transaction_isolation TO 'read committed';
  ALTER ROLE kullanici_adi SET timezone TO 'Europe/Istanbul';
  
  GRANT ALL PRIVILEGES ON DATABASE english TO kullanici_adi;
  \q
```
