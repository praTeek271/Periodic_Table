from flask import Flask, request
from flask import render_template
import json
import flask
app = Flask(__name__)


@app.route('/')
def hello():
    elem,category=json_exrax()
    return render_template('index.html',elements=elem,category=category)

# def shell_format(shell):
#     str_shells=''
#     for i in shell:
#         str_shells+=str(i)+"\n"
#     return(str_shells)
def json_exrax():
    '''Data Access Section'''
    with open('static/assets/files/periodic_table.json', 'r',encoding="utf8") as f:
        data = json.load(f)
        data=data['elements']
        l=len(data)


#--------------------------------------------------------------------------------------------------|

    #-----------------------------------symbol-----------------------------------|
        symbol=[data[i]['symbol'] for i in range(l)]
    #-----------------------------------name-------------------------------------|
        name=[data[i]['name'] for i in range(l)]
    #-------------------------------atomic_mass----------------------------------|
        atomic_mass=[round(data[i]['atomic_mass'],4) for i in range(l)]
    #---------------------------------atomic_no----------------------------------|
        atomic_no=[data[i]['number'] for i in range(l)]
    #---------------------------------xpos---------------------------------------|
        xpos=[data[i]['xpos'] for i in range(l)]
    #----------------------------------ypos--------------------------------------|
        ypos=[data[i]['ypos'] for i in range(l)]
    #----------------------------------color-------------------------------------|
        color=[data[i]['cpk-hex'] for i in range(l)]
    #---------------------------------category-----------------------------------|
        category=[data[i]['category'] for i in range(l)]
    #------------------------------shell-----------------------------------------|
        shell=[data[i]['shells'] for i in range(l)]
    #------------------------------summary---------------------------------------|
        summary=[data[i]['summary'] for i in range(l)]
    #--------------------------------electronic_config---------------------------|
        ele_conf=[data[i]['electron_configuration'] for i in range(l)]
    #--------------------------------bohr_model_3d---------------------------|
        model_3d=[data[i]['bohr_model_3d'] for i in range(l)]
#--------------------------------------------------------------------------------------------------|


        category=[*set(category)]
        s={}
        elements=[]
        for i in range(l):
            ele=[]
            ele.append(atomic_no[i])
            ele.append(symbol[i])
            ele.append(name[i])
            ele.append(atomic_mass[i])
            ele.append(xpos[i])
            ele.append(ypos[i])
            ele.append(color[i])
            # ele.append(model_3d[i])
            # ele.append(category[i])
            ele.append(shell[i])
            ele.append(summary[i])
            ele.append(ele_conf[i])
            ele.append(model_3d[i])


            elements.append(ele)

            # s[f'{name[i]}']=model_3d[i]

        return(elements,category)
        # return( s)


# if __name__ == '__main__':
#     data=json_exrax()    
#     # csvfile.append(