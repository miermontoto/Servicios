docker stop nginx
docker run --rm -d --network pruebas \
   --name nginx -p 80-81:80-81 \
   -v $(pwd)/html:/usr/share/nginx/html \
   -v $(pwd)/sitios_nginx:/etc/nginx/conf.d \
   -v $(pwd)/html2:/usr/share/nginx/html2 \
   -v $(pwd)/config_nginx:/usr/nginx \
   nginx
