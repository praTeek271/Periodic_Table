from flask import Flask, request
from flask import render_template
import json

app = Flask(__name__)



@app.route('/')
def hello():
    elem=json_exrax()
    return render_template('index.html',elements=elem)


def json_exrax():
    with open('static/periodic_table.json', 'r',encoding="utf8") as f:
        data = json.load(f)
        data=data['elements']
        l=len(data)
        symbol=[data[i]['symbol'] for i in range(l)]
        name=[data[i]['name'] for i in range(l)]
        atomic_mass=[data[i]['atomic_mass'] for i in range(l)]
        atomic_no=[data[i]['number'] for i in range(l)]
        xpos=[data[i]['xpos'] for i in range(l)]
        ypos=[data[i]['ypos'] for i in range(l)
        ]
        # print(f"{name}\n\n{symbol}\n\n{atomic_no}\n\n{atomic_mass}")

        elements=[]
        for i in range(l):
            ele=[]
            ele.append(atomic_no[i])
            ele.append(symbol[i])
            ele.append(name[i])
            ele.append(atomic_mass[i])
            ele.append(xpos[i])
            ele.append(ypos[i])

            elements.append(ele)


        return(elements)


# if __name__ == '__main__':
#     print(json_exrax())