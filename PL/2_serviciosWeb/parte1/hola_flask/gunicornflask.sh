if [ ! -f "Dockerfile" ]; then
    echo "This script must be called from hola_flask root directory"
    exit 1
fi

if [ "$1" = "build" ]; then
    docker build -t gunicornflask:1.0  .
    exit 0
fi

if [ "$1" = "run" ]; then
    docker run -d --rm --name hola-flask \
        --network pruebas gunicornflask:1.0
    exit 0
fi

echo "Usage: $0 build|run"
exit 1
