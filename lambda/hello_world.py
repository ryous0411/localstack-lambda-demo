def lambda_handler(event, context):
    name: str = event.get("PathParameters")

    if name:
        return {
            "message": f"Hello {name}"
        }

    return {
        "message": "Hello World!"
    }
