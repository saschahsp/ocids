import io
import json

from fdk import response
import sys
sys.path.append('/function')
import scorefn

model = scorefn.load_model()

def handler(ctx, data: io.BytesIO=None):

    try:
        input = json.loads(data.getvalue())['input']
        prediction = scorefn.predict(model, input)
    except (Exception, ValueError) as ex:
        print(str(ex))

    return response.Response(
        ctx, response_data=json.dumps(prediction),
        headers={"Content-Type": "application/json"}
    )