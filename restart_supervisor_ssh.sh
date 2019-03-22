#!/bin/bash

echo
echo "******************************"
echo "*** Restart GCA supervisor ***"
echo "******************************"
echo

if [ "$1" == "-h" ] || [ "$1" == "--help" ]; then
  echo -e "Usage: `basename $0` Insira os finais dos ips dos servidores GCA separados por espaço\n\n"
  exit 0
fi

for HOST in "$@"
do
    ssh leme@172.17.64.$HOST -p 2961 'echo -e "<password>\n" | sudo -S supervisorctl restart all' 1>/dev/null
    if [ $? -eq 1 ]; then
        echo "Houve um problema ao tentar se comunicar com o servidor."
        break
    fi
    echo -e "$HOST - application e celery reiniciados com sucesso.\n"
    sleep 1
done
exit 0
