from defender.apps import create_app

# CUSTOMIZE: import model to be used
from defender.models.nfs_model import NeedForSpeedModel

if __name__ == "__main__":
    model = "defender/models/model.keras"

    app = create_app(model)

    import sys
    port = int(sys.argv[1]) if len(sys.argv) == 2 else 8080

    from gevent.pywsgi import WSGIServer
    http_server = WSGIServer(('', port), app)
    http_server.serve_forever()

    # curl -XPOST --data-binary @somePEfile http://127.0.0.1:8080/ -H "Content-Type: application/octet-stream"
