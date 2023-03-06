from veep.client import ref
from veep.main import Veep

APP = Veep()


@APP.client.route(
    "/",
    template="""\
<div>
    {{message}}
    <button @click="count++">
        You clicked me {{count}} times.
    </button>
</div>""",
)
def home():
    count = ref(0)
    message = "Hello World"
    return {
        "count": count,
        "message": message,
    }


@APP.server.get("/cats")
def cats():
    return [
        {"name": "Felix", "age": 3},
        {"name": "Garfield", "age": 4},
        {"name": "Tom", "age": 5},
        {"name": "Sylvester", "age": 6},
    ]
