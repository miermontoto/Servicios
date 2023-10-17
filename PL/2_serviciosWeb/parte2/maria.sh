if [ "$1" = "run" ]; then
	docker stop basedatos
	docker run --name basedatos \
		-e MYSQL_ROOT_PASSWORD=claveroot \
		-e MYSQL_USER=amigosuser \
		-e MYSQL_DATABASE=amigosdb \
		-e MYSQL_PASSWORD=amigospass \
		-v $(pwd)/basedatos:/var/lib/mysql \
		--rm --network pruebas -d mariadb
	exit 0
fi

if [ "$1" = "client" ]; then
	echo "cmd: mariadb -h basedatos -u amigosuser -p amigosdb"
	echo "pass: amigospass"
	docker run -it --rm --network pruebas mariadb bash
	exit 0
fi

echo "Usage: $0 run|client"
exit 1
