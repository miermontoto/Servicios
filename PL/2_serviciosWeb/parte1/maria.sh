if [ "$1" = "run" ]; then
	docker run --name mariadb -e MYSQL_ROOT_PASSWORD=claveroot \
		-v $(pwd)/basedatos:/var/lib/mysql \
		--rm --network pruebas -d mariadb
	exit 0
fi

if [ "$1" = "client" ]; then
	echo "cmd: mariadb -h mariadb -u root -p"
	echo "pass: claveroot"
	docker run --rm -it --network pruebas mariadb bash
	exit 0
fi

echo "Usage: $0 run|client"
exit 1
