function validateForm(event) {
    const url = document.getElementById('url').value.trim();
    const errorMessage = document.getElementById('error-message');

    let [a, b, c, d, e] = url.split('/');
    if ((a === 'https:') && (b === '') && (c === 'www.youtube.com') && (d.startsWith('@')) && (!e || e === 'videos')) {
        errorMessage.classList.add('hidden');
        return true;
    }
    errorMessage.classList.remove('hidden');
    event.preventDefault();
    return false;
}