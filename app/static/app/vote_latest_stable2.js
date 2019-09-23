import {x} from './helpers.js'
import {get_instance} from './prev_next.js'

(function (window, document, undefined){    
    // alert(x)
    // Upvote / Downvote selectors:
    const upvote = document.getElementById('upvote');
    const downvote = document.getElementById('downvote');
    const object_id = document.getElementById('object_id').textContent.trim();
    // const object_id = document.getElementById('object_id').innerHTML;

    // csrftoken getter
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }
    var csrftoken = getCookie('csrftoken');

    // Voting function

    const vote = ($route) => {
        fetch(`/${$route}/${object_id}/`, {
            method:'post',
            headers:{
              'X-CSRFToken':csrftoken,
              'Content-Type':'application/x-www-form-urlencoded; charset=UTF-8',
              'X-Requested-With':'XMLHttpRequest'
            },
          })
          .then((response) => response.json())
          .then((responseData) => {
          console.log(responseData);
          return responseData;
      })
      .catch(error => console.warn(error));
    }

    // Event listener adder
    const add = ($element, $route) => {
        $element.addEventListener('click', vote.bind(null, $route))
    }

    add(upvote, "upvote")
    add(downvote, "downvote")

})(window, document);