async function readFileAsDataText(file){
    let res = await new Promise((resolve)=>{
        let reader = new FileReader()
        reader.readAsText(file,'UTF-8')
        reader.onload = (evt)=>{resolve(evt.target.result)}
    })
    return res;
}

function loadJson(file){
    return JSON.parse(file)
}

function createTextPresentationNode(text){
    let h1 = document.createElement('h1')
    let div = document.createElement('div')
    let para = document.createElement('p')
    h1.append(document.createTextNode("TEXTE :"))
    for (let i = 0 ; i < text.length;i++){
        para.appendChild(text[i])
    }
    div.append(h1)
    div.append(para)
    document.body.append(div)
}

function isEntityInTokens(token,json){
    let res = false ; 
    for (attribute in json){
        if (json[attribute].includes(token)==true)
            res=true
    }
    return res;
}

function idk(tokens,json){
    let resArray=[]
    let color=new Map()
    for (let j = 0 ; j < tokens.length ; j++){
        if(isEntityInTokens(tokens[j],json)){
            let typeEntitty =returnKey(tokens[j],json);
            if (!color.has(typeEntitty)){
                let colory = randomHexColor()
                color.set(typeEntitty,colory)
            }
            let el  = document.createElement('em')
            el.className = typeEntitty
            el.style.color = color.get(typeEntitty)
            el.appendChild(document.createTextNode(tokens[j]+" "))
            resArray.push(el)
        }else{
            resArray.push(document.createTextNode(tokens[j]+" "))
        }
    }
    return resArray
}

function addEventToEntity(json){
    for (attribute in json){
        for (let i = 0 ; i < document.getElementsByClassName(attribute).length ; i++){
            document.getElementsByClassName(attribute)[i].addEventListener('click',function (target){
                if(target.target.style.backgroundColor == "white"){
                    target.target.style.backgroundColor = "grey"
                }else{
                    target.target.style.backgroundColor = "white"
                }
            })
        }
        

    }
}

function returnKey(token,json){
    for (attribute in json){
        if (json[attribute].includes(token))
            return attribute
    }
}
function randomHexColor(){
    let n = (Math.random()* 0xfffff * 1000000).toString(16);
    return '#'+n.slice(0,6)
}


function createTable(table, name){
    let tables = document.createElement('table')
    let rowHeader = document.createElement('tr')
    let category = document.createElement('th')
    category.appendChild(document.createTextNode(name))
    rowHeader.appendChild(category)
    tables.appendChild(rowHeader)
    for (let i=0; i < table.length;i++){
        let row = document.createElement('tr')
        let col = document.createElement('td')
        let data = document.createTextNode(table[i])
        col.appendChild(data)
        row.appendChild(col)
        tables.appendChild(row)
    }
    return tables;
}

function generateTable (jsonArray, parent){
    for (element in jsonArray){
        parent.appendChild(createTable(jsonArray[element], element))
    }
}



document.getElementById('valider').addEventListener('click',async ()=>{
    let div = document.createElement('div')
    let file = document.getElementById('form').files[0]
    let content = await readFileAsDataText(file);
    let json = loadJson(content)
    let finalText = idk(json[1],json[0])
    div.className="container";
    generateTable(json[0], div)
    createTextPresentationNode(finalText)
    document.body.appendChild(div)
    addEventToEntity(json[0])
});

