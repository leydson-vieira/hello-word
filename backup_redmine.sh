#!/bin/bash

echo "$(date +%d-%m-%y) $(date +%H:%M-%S) - Backup iniciado" >> /var/log/backup.log
echo "Copiando base de dados..."

mysqldump --user=root --password=admin43211 --skip-extended-insert redmine > /home/infra/testebkp.sql

echo "Base de dados - OK"
echo
echo "Copiando diretório de arquivos..."

cp -r /opt/redmine/redmine-3.2.3/files /home/infra/

echo "Arquivos - OK"
echo 
cd /home/infra/

echo "Compactando backup..."

tar -czf /backup/redmine-$(date +%d-%m-%y).tar.gz files testebkp.sql

echo "Backup compactado - OK"
echo
echo "Removendo arquivos temporários..."

rm -r files/ testebkp.sql

echo "Remoção de arquivos - OK"
echo
echo "Backup Finalizado!"
echo

find /backup -name *.tar.gz -mtime +5 -exec rm {} ';'

echo -e "$(date +%d-%m-%y) $(date +%H-%M-%S) - Backup finalizado\n" >> /var/log/backup.log
