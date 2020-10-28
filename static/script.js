function sendFavorite(source, url) {
    fetch(url)
    .then(resp => {
        if (resp.ok) {
            return resp.json();
        } else {
            return {
                status: resp.status, reason: resp.statusText
            }
        }
    })
    .then(json => {
        if (json.status) {console.log(`Request failed with ${json.status} code: ${json.reason}`)}
        else {
            alert(json.message)
            source.textContent = `${json.numLikes} favorites`
        }}
    )}

function markAsCorrect(source, url) {
    fetch(url)
    .then(resp => {
        if (resp.ok) {
            return resp.json();
        } else {
            return {
                status: resp.status, reason: resp.statusText
            }
        }
    })
    .then(json => {
        if (json.status) {console.log(`Request failed with ${json.status} code: ${json.reason}`)}
        else {
            alert(json.message)
            source.textContent = `${json.correct} correct!`
        }}
    )}