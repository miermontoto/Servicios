if [ "$1" = "flask" ]; then
	docker run --name amigos --rm -d --network pruebas amigos:1.0
   exit 0
fi

if [ "$1" = "nginx" ]; then
	docker run --rm -d --network pruebas --name nginx \
       -v $(pwd)/sitios_nginx:/etc/nginx/conf.d \
       -p 80:80 nginx
	exit 0
fi

if [ "$1" = "maria" ]; then
	sh maria.sh run
	exit $?
fi

echo "Usage: $0 flask|nginx|maria"
exit 1
