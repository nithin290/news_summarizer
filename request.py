import requests

url = 'http://localhost:5000/results'
r = requests.post(url, json={'Content': "In addition to that, dump function is used to write the "
                                        "pickled representation of the object (the model in our "
                                        "example) to the open file. Dump format is as below and for "
                                        "further details you can refer to Python docs here. "})

print(r.json())
