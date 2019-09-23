

// function create_text(){
//     let body = document.getElementsByName('body')[0];
//     alert(body)
//     // let paragraph = document.createElement('p');
//     // let text = document.createTextNode("A text");

//     // paragraph.appendChild(text);
//     // body.appendChild(paragraph);
// }

// export {create_text}

const get_instance = ($number) => {
    const instance = document.getElementById($number).textContent.trim()
    alert(instance)
}

export { get_instance }