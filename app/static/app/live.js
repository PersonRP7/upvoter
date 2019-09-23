function create_text(){
    let body = document.getElementsByClassName('body')[0];
    let paragraph = document.createElement('p');
    let text = document.createTextNode('Text');
    paragraph.appendChild(text)
    body.appendChild(paragraph)
}

create_text()